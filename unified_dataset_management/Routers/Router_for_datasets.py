from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from Models.datasets import Dataset
from schemas import DatasetCreate, DatasetResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=DatasetResponse)
def create_dataset(dataset: DatasetCreate, db: Session = Depends(get_db)):

    # 檢查是否已存在相同名稱的數據集
    existing_dataset = db.query(Dataset).filter(Dataset.name == dataset.name).first()
    if existing_dataset:
        raise HTTPException(status_code=400, detail=f"Dataset with name '{dataset.name}' already exists.")
    
    db_dataset = Dataset(**dataset.model_dump())
    db.add(db_dataset)
    db.commit()
    db.refresh(db_dataset)

    # 格式化 created_at
    db_dataset.created_at = db_dataset.created_at.isoformat()
    return db_dataset

@router.get("/", response_model=List[DatasetResponse])
def get_datasets(db: Session = Depends(get_db)):
    return db.query(Dataset).all()
