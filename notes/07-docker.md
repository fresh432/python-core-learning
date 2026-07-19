# Docker 完整学习笔记

## 学习时间
2026-07-16 19:30 - 2026-07-18 21:46（约8小时教程+实践）

## 学习资源
黑马程序员Docker教程（2019版，28集）

---

## 一、Docker基础概念

| 概念 | 说明 | 类比 |
|------|------|------|
| **镜像（Image）** | 只读模板，包含应用+环境 | 类 |
| **容器（Container）** | 镜像的运行实例 | 对象 |
| **仓库（Repository）** | 存储镜像的地方 | GitHub |
| **Dockerfile** | 构建镜像的脚本 | Makefile |
| **docker-compose** | 多容器编排工具 | 项目管理 |

---

## 二、Docker安装与配置

### 安装
- Windows/Mac：Docker Desktop
- Linux：`yum install docker` / `apt install docker.io`

### 镜像加速器（国内必配）
```json
// /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://docker.mirrors.ustc.edu.cn",
    "https://hub-mirror.c.163.com"
  ]
}
```

#### 踩坑： 国内大部分镜像源已失效，配置耗时约2小时。

## 三、Docker命令

### 1. 服务相关
```bash
systemctl start docker     # 启动
systemctl stop docker      # 停止
systemctl restart docker   # 重启
systemctl status docker    # 查看状态
systemctl enable docker    # 开机启动
```

### 2. 镜像相关
```bash
docker images              # 查看本地镜像
docker images -q           # 只看ID
docker search 镜像名称      # 搜索镜像
docker pull 镜像名称:标签   # 拉取镜像
docker rmi 镜像ID          # 删除镜像
docker rmi $(docker images -q)  # 删除所有
```

### 3. 容器相关
```bash
# 查看容器
docker ps                  # 运行中的
docker ps -a               # 所有

# 创建并启动
docker run -it --name=c1 centos:7 /bin/bash   # 交互式
docker run -id --name=c2 centos:7 /bin/bash   # 守护式

# 参数
-i          # 保持容器运行
-t          # 分配伪终端
-d          # 后台运行
--name      # 命名
-p 宿主机:容器  # 端口映射
-v 宿主机:容器  # 数据卷挂载

# 进入容器
docker exec -it c1 /bin/bash

# 停止/启动/删除
docker stop c1
docker start c1
docker rm c1               # 删除（需先停止）
docker rm -f c1            # 强制删除
docker inspect c1          # 查看详细信息
```

## 四、数据卷

### 概念
- 宿主机目录/文件，挂载到容器
- 容器删除，数据卷数据保留
- 多个容器可共享

### 配置
```bash
# 直接挂载
docker run -v /host/data:/container/data ...

# 数据卷容器（多个容器共享）
# 1. 创建数据卷容器
docker run -it --name=c3 -v /volume centos:7 /bin/bash

# 2. 其他容器挂载
docker run -it --name=c1 --volumes-from c3 centos:7 /bin/bash
```

### 作用
- 容器数据持久化
- 外部机器和容器间通信
- 容器之间数据交换

## 五、Dockerfile

### 常用指令
| 指令        | 作用      | 示例                                    |
| --------- | ------- | ------------------------------------- |
| `FROM`    | 基础镜像    | `FROM python:3.11-slim`               |
| `WORKDIR` | 设置工作目录  | `WORKDIR /app`                        |
| `COPY`    | 复制文件    | `COPY . .`                            |
| `RUN`     | 构建时执行命令 | `RUN pip install -r requirements.txt` |
| `CMD`     | 容器启动时执行 | `CMD ["python", "main.py"]`           |
| `EXPOSE`  | 声明端口    | `EXPOSE 8000`                         |
| `ENV`     | 环境变量    | `ENV PORT=8000`                       |

### 项目实践
#### FastAPI项目Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Go项目Dockerfile（多阶段构建）
```dockerfile
# 构建阶段
FROM golang:1.22-alpine AS builder

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

# 运行阶段
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/main .
EXPOSE 8080
CMD ["./main"]
```

#### 多阶段构建优势： 最终镜像仅包含二进制文件，体积极小。

.dockerignore
```plain
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.env
.git
.gitignore
README.md
tests/
blog.db
*.exe
*.test
*.out
```

## 六、镜像构建与推送
```bash
# 构建
docker build -t myapp:latest .

# 标记
docker tag myapp:latest username/myapp:latest

# 推送到Docker Hub
docker push username/myapp:latest

# 私有仓库
docker tag myapp:latest 192.168.1.100:5000/myapp:latest
docker push 192.168.1.100:5000/myapp:latest
docker pull 192.168.1.100:5000/myapp:latest
```

## 七、docker-compose
### 概念
- 多容器编排工具
- 一个YAML文件定义多个服务
- 一条命令启动/停止所有服务

### FastAPI项目docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - db

  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: blog
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

### Go项目docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - ./data:/data
    restart: unless-stopped
```

### 常用命令
```bash
docker compose up -d        # 后台启动所有服务
docker compose down         # 停止并删除容器
docker compose ps           # 查看运行状态
docker compose logs -f      # 查看日志
docker compose build        # 重新构建镜像
```

## 八、Docker vs 虚拟机
| 维度   | Docker容器       | 虚拟机        |
| ---- | -------------- | ---------- |
| 启动速度 | 秒级             | 分钟级        |
| 资源占用 | 轻量（共享内核）       | 重（独立内核+OS） |
| 性能   | 接近原生           | 有虚拟化损耗     |
| 隔离性  | 进程级            | 系统级        |
| 体积   | MB级            | GB级        |
| 适用场景 | 微服务、CI/CD、开发环境 | 完整系统隔离、多OS |

## 关键教训
| 问题      | 解决                   |
| ------- | -------------------- |
| 国内镜像源失效 | 配置多个镜像源，或自建代理        |
| 容器数据丢失  | 使用数据卷 `-v` 挂载        |
| 镜像体积过大  | 多阶段构建，轻量级基础镜像        |
| 端口冲突    | 修改docker-compose端口映射 |

## 下一步
- 学习Kubernetes（容器编排进阶）
- CI/CD流水线集成Docker
- 云服务器部署实践


