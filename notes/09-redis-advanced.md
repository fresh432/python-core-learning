# Redis 高级篇学习笔记

## 学习时间
2026-07-25 19:30-21:29（约2小时）

## 一、Redis持久化

### RDB（Redis Database）

| 特性 | 说明 |
|------|------|
| **原理** | 定时快照，fork子进程保存内存数据到磁盘 |
| **触发** | save命令（阻塞）、bgsave命令（后台）、配置自动触发 |
| **文件** | dump.rdb |
| **优点** | 文件紧凑，恢复速度快，适合备份 |
| **缺点** | 可能丢失最后一次快照后的数据 |

```bash
# 手动触发
SAVE      # 阻塞主进程
BGSAVE    # 后台fork子进程

# 配置自动触发
save 900 1    # 900秒内1次修改则触发
save 300 10   # 300秒内10次修改则触发
save 60 10000 # 60秒内10000次修改则触发
```

### AOF（Append Only File）

| 特性     | 说明                  |
| ------ | ------------------- |
| **原理** | 记录所有写命令，重启时重放恢复     |
| **文件** | appendonly.aof      |
| **优点** | 数据安全性高，最多丢失1秒数据     |
| **缺点** | 文件大，恢复速度慢           |
| **重写** | BGREWRITEAOF 压缩合并命令 |

```bash
# 开启AOF
appendonly yes

# AOF重写（压缩）
BGREWRITEAOF
```

### RDB vs AOF

| 维度   | RDB       | AOF           |
| ---- | --------- | ------------- |
| 文件大小 | 小（二进制压缩）  | 大（文本记录命令）     |
| 恢复速度 | 快（直接加载）   | 慢（逐条执行命令）     |
| 数据安全 | 可能丢最后一次快照 | 最多丢1秒（默认每秒刷盘） |
| 性能影响 | fork时短暂阻塞 | 持续写磁盘，开销较大    |
| 推荐方案 | **两者都用**  | **两者都用**      |

### 生产环境推荐：RDB + AOF 同时开启
- RDB用于快速恢复
- AOF用于数据安全

## 二、缓存三大问题

### 1. 缓存穿透（Cache Penetration）

| 项目     | 说明                       |
| ------ | ------------------------ |
| **现象** | 查询不存在的数据，缓存和DB都没有，每次直达DB |
| **原因** | 恶意攻击、数据确实不存在、非法参数        |
| **危害** | DB压力增大，可能被击垮             |
| **解决** | ① 缓存空值 ② 布隆过滤器 ③ 参数校验    |

```python
# 方案：缓存空值
def get_data(key):
    value = redis.get(key)
    if value == "__NULL__":
        return None  # 空值缓存，直接返回
    if value:
        return value
    
    # 查DB
    value = db.query(key)
    if value is None:
        redis.setex(key, 60, "__NULL__")  # 缓存空值，短期过期
        return None
    
    redis.setex(key, 300, value)
    return value
```

### 2. 缓存击穿（Cache Breakdown）

| 项目     | 说明                              |
| ------ | ------------------------------- |
| **现象** | 热点key过期瞬间，大量请求同时直达DB            |
| **原因** | 热点数据过期、并发量高                     |
| **危害** | 单点DB压力剧增                        |
| **解决** | ① 互斥锁 ② 逻辑过期（不设置TTL）③ 热点key永不过期 |

```python
# 方案：互斥锁
import threading

def get_hot_data(key):
    value = redis.get(key)
    if value:
        return value
    
    # 尝试获取锁
    lock = threading.Lock()
    if lock.acquire(blocking=False):
        try:
            # 双重检查
            value = redis.get(key)
            if value:
                return value
            
            # 查DB并缓存
            value = db.query(key)
            redis.setex(key, 300, value)
            return value
        finally:
            lock.release()
    else:
        # 没拿到锁，等待后重试
        time.sleep(0.1)
        return get_hot_data(key)
```

### 3. 缓存雪崩（Cache Avalanche）

| 项目     | 说明                                |
| ------ | --------------------------------- |
| **现象** | 大量key同时过期，DB压力剧增甚至崩溃              |
| **原因** | 批量设置相同过期时间、Redis宕机                |
| **危害** | 全量请求直达DB，服务雪崩                     |
| **解决** | ① 随机过期时间 ② 多级缓存 ③ 熔断降级 ④ Redis高可用 |

```python
# 方案：随机过期时间
import random

def set_cache(key, value, base_expire=300):
    # 基础过期时间 + 随机偏移（0-60秒）
    expire = base_expire + random.randint(0, 60)
    redis.setex(key, expire, value)
```

## 三、缓存问题对比总结

| 问题     | 现象              | 根本原因      | 解决核心       |
| ------ | --------------- | --------- | ---------- |
| **穿透** | 查不存在数据，DB压力大    | 缓存和DB都没有  | 缓存空值/布隆过滤器 |
| **击穿** | 热点key过期，瞬间DB压力大 | 单个热点key过期 | 互斥锁/逻辑过期   |
| **雪崩** | 大量key过期，DB崩溃    | 批量key同时过期 | 随机过期/多级缓存  |

## 四、项目缓存优化

### 优化 app/core/cache.py
```python
import redis
import json
import random
from typing import Optional

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

def get_cache(key: str) -> Optional[str]:
    """获取缓存"""
    return redis_client.get(key)

def set_cache(key: str, value: str, base_expire: int = 300):
    """
    设置缓存，随机过期时间防止雪崩
    """
    expire = base_expire + random.randint(0, 60)
    redis_client.setex(key, expire, value)

def set_null_cache(key: str, expire: int = 60):
    """缓存空值，防止穿透"""
    redis_client.setex(key, expire, "__NULL__")

def is_null_value(value: str) -> bool:
    """判断是否为空值缓存"""
    return value == "__NULL__"

def delete_cache(key: str):
    """删除缓存"""
    redis_client.delete(key)

def delete_cache_pattern(pattern: str):
    """按模式删除缓存"""
    for key in redis_client.scan_iter(match=pattern):
        redis_client.delete(key)
```

## 五、面试要点

| 问题          | 回答要点                 |
| ----------- | -------------------- |
| Redis持久化方式？ | RDB快照+AOF日志，推荐两者都用   |
| 缓存穿透怎么解决？   | 缓存空值、布隆过滤器、参数校验      |
| 缓存击穿怎么解决？   | 互斥锁、逻辑过期、热点key永不过期   |
| 缓存雪崩怎么解决？   | 随机过期时间、多级缓存、Redis高可用 |



