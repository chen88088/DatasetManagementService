from fastapi import FastAPI
from Routers import Router_for_datasets, Router_for_dataset_versions
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 注册路由
app.include_router(Router_for_datasets.router, prefix="/datasets", tags=["Dataset Categories"])
app.include_router(Router_for_dataset_versions.router, prefix="/datasets", tags=["Versions and Info of Centain Dataset"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或指定 ['http://localhost:5173'] 限制来源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)