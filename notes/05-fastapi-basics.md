# FastAPI 基础学习笔记

## 今日进度
- [x] 01-07：框架简介、路由、路径参数、查询参数
- [x] 08-09：请求体参数（Pydantic）
- [x] 10-13：响应类型（JSON、HTML、文件）
- [x] 14：异常响应处理
- [x] 15：中间件

## 核心概念

### 1. 路由
```python
@app.get("/")           # GET 请求
@app.post("/register")  # POST 请求
```
### 2. 路径参数 + 验证
```python
@app.get("/book/{id}")
async def get_book(id: int = Path(..., gt=0, le=100)):
    return {"id": id}
```
### 3. 查询参数 + 默认值
```python
@app.get("/news")
async def get_news(skip: int = Query(0), limit: int = Query(10)):
    return {"skip": skip, "limit": limit}
```
### 4. 请求体（Pydantic）
```python
class User(BaseModel):
    username: str = Field(min_length=2, max_length=10)
    password: str = Field(min_length=3, max_length=20)

@app.post("/register")
async def register(user: User):
    return user
```
### 5. 响应类型
```python
@app.get("/html", response_class=HTMLResponse)   # HTML
@app.get("/file", response_class=FileResponse)   # 文件
@app.get("/news", response_model=News)            # JSON + 模型验证
```
### 6. 异常处理
```python
raise HTTPException(status_code=404, detail="不存在")
```
### 7. 中间件
```python
@app.middleware("http")
async def middleware(request, call_next):
    print("start")
    response = await call_next(request)
    print("end")
    return response
```

## 注意事项
- FileResponse 需要文件真实存在，路径要正确
- response_model 会过滤掉模型中没有的字段
- 中间件执行顺序：自下而上（先定义的会后执行）

