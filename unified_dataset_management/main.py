from fastapi import FastAPI
from Routers import Router_for_datasets, Router_for_dataset_versions
from database import Base, engine


# 創建數據庫表
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# 註冊路由
app.include_router(Router_for_datasets.router, prefix="/datasets", tags=["Datasets"])
app.include_router(Router_for_dataset_versions.router, prefix="/datasets_versions", tags=["Dataset Versions"])
