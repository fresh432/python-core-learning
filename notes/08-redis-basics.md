# Redis 基础篇学习笔记

## 学习时间
2026-07-24 19:12-22:21（约3小时）

## 一、Redis概述

| 特性 | 说明 |
|------|------|
| **类型** | NoSQL键值对数据库 |
| **存储** | 内存存储，读写速度极快 |
| **用途** | 缓存、消息队列、计数器、排行榜等 |
| **数据结构** | String、Hash、List、Set、SortedSet |

## 二、通用命令

| 命令 | 作用 | 注意 |
|------|------|------|
| `KEYS pattern` | 查看符合模板的所有key | 生产环境禁用，O(n) |
| `DEL key` | 删除指定key | - |
| `EXISTS key` | 判断key是否存在 | 返回0/1 |
| `EXPIRE key seconds` | 设置key有效期 | 到期自动删除 |
| `TTL key` | 查看key剩余有效期 | -1表示无过期，-2表示已删除 |

## 三、5大数据类型

### 1. String（字符串）

| 命令 | 作用 |
|------|------|
| `SET key value` | 添加/修改键值对 |
| `GET key` | 获取value |
| `MSET k1 v1 k2 v2` | 批量添加 |
| `MGET k1 k2` | 批量获取 |
| `INCR key` | 整型自增1 |
| `INCRBY key n` | 整型自增n |
| `SETNX key value` | key不存在才设置（分布式锁） |
| `SETEX key seconds value` | 设置键值对+有效期 |

**用途：** 缓存、计数器、分布式锁、Session

### 2. Hash（散列）

| 命令 | 作用 |
|------|------|
| `HSET key field value` | 添加/修改字段 |
| `HGET key field` | 获取字段值 |
| `HMSET key f1 v1 f2 v2` | 批量添加字段 |
| `HGETALL key` | 获取所有字段和值 |
| `HKEYS key` | 获取所有字段 |
| `HVALS key` | 获取所有值 |
| `HINCRBY key field n` | 字段值自增 |

**用途：** 对象存储（比String JSON更灵活）、购物车

### 3. List（列表）

| 命令 | 作用 |
|------|------|
| `LPUSH key element` | 左侧插入 |
| `LPOP key` | 左侧移除并返回 |
| `RPUSH key element` | 右侧插入 |
| `RPOP key` | 右侧移除并返回 |
| `LRANGE key start end` | 获取范围元素 |
| `BLPOP/BRPOP` | 阻塞式弹出（消息队列） |

**用途：** 消息队列、最新消息列表

### 4. Set（集合）

| 命令 | 作用 |
|------|------|
| `SADD key member` | 添加元素 |
| `SREM key member` | 移除元素 |
| `SCARD key` | 元素个数 |
| `SISMEMBER key member` | 判断是否包含 |
| `SMEMBERS key` | 获取所有元素 |
| `SINTER k1 k2` | 交集 |
| `SDIFF k1 k2` | 差集 |
| `SUNION k1 k2` | 并集 |

**用途：** 共同关注、抽奖、去重

### 5. SortedSet（有序集合）

| 命令 | 作用 |
|------|------|
| `ZADD key score member` | 添加元素（带分数） |
| `ZREM key member` | 移除元素 |
| `ZSCORE key member` | 获取分数 |
| `ZRANK key member` | 获取排名（升序） |
| `ZCARD key` | 元素个数 |
| `ZCOUNT key min max` | 分数范围内个数 |
| `ZRANGE key start end` | 按排名范围获取 |
| `ZREVRANGE key start end` | 按排名范围获取（降序） |

**用途：** 排行榜、延时队列

## 四、Key的层级格式
项目名:业务名:类型:id
例如：fastapi:article:1
fastapi:user:avatar:1

## 五、Python客户端（redis-py）

```python
import redis

# 连接
r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True  # 自动解码为字符串
)

# String
r.set('name', 'Alice')
print(r.get('name'))  # Alice

# Hash
r.hset('user:1', 'name', 'Bob')
r.hset('user:1', 'age', 20)
print(r.hgetall('user:1'))  # {'name': 'Bob', 'age': '20'}

# 设置过期
r.setex('token', 300, 'abc123')  # 5分钟过期
```

## 六、缓存应用场景
| 场景     | 数据类型          | 命令             |
| ------ | ------------- | -------------- |
| 文章列表缓存 | String (JSON) | SET/GET        |
| 用户资料缓存 | Hash          | HSET/HGETALL   |
| 最新评论   | List          | LPUSH/LRANGE   |
| 文章点赞数  | String (INCR) | INCR/GET       |
| 热门文章排行 | SortedSet     | ZADD/ZREVRANGE |

## 下一步
- 高级篇：持久化、缓存问题（穿透/击穿/雪崩）
- 项目集成：FastAPI文章列表缓存


