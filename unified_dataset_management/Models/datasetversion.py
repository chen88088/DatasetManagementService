from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

# Dataset Versions 表
class DatasetVersion(Base):
    __tablename__ = "dataset_versions"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    dataset_name = Column(String(255))
    version = Column(String(50), nullable=False)
    crop_type = Column(String(50))
    region = Column(String(50))
    storage_url = Column(String(255))
    update_scope = Column(String(255))
    features = Column(Text)
    created_at = Column(TIMESTAMP, server_default="now()")

    dataset = relationship("Dataset", back_populates="versions")