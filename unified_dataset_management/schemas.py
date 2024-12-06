from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Dataset 模型
class DatasetBase(BaseModel):
    name: str
    crop_type: Optional[str]
    region: Optional[str]
    resolution: Optional[str]
    channels: Optional[int]
    description: Optional[str]

class DatasetCreate(DatasetBase):
    pass

class DatasetResponse(DatasetBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True

# Dataset Version 模型
class DatasetVersionBase(BaseModel):
    version: str
    storage_url: str
    update_scope: Optional[str]
    features: Optional[str]

class DatasetVersionCreate(DatasetVersionBase):
    dataset_id: int

class DatasetVersionResponse(DatasetVersionBase):
    id: int
    dataset_id: int
    dataset_name: str
    crop_type: Optional[str]
    region: Optional[str]
    created_at: datetime  # 確保這裡是 datetime 類型

    class Config:
        orm_mode = True
