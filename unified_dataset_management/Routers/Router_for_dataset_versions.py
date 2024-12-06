from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from Models.datasetversion import DatasetVersion
from Models.datasets import Dataset
from schemas import DatasetVersionCreate, DatasetVersionResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=DatasetVersionResponse)
def create_version(version: DatasetVersionCreate, db: Session = Depends(get_db)):
    dataset = db.query(Dataset).filter(Dataset.id == version.dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    db_version = DatasetVersion(**version.dict(), dataset_name=dataset.name, crop_type=dataset.crop_type, region=dataset.region)
    db.add(db_version)
    db.commit()
    db.refresh(db_version)
    return db_version

@router.get("/dataset/{dataset_id}", response_model=List[DatasetVersionResponse])
def get_versions(dataset_id: int, db: Session = Depends(get_db)):
    return db.query(DatasetVersion).filter(DatasetVersion.dataset_id == dataset_id).all()
