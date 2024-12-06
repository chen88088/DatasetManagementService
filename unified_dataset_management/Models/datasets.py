from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

# Datasets 表
class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    crop_type = Column(String(50))
    region = Column(String(50))
    resolution = Column(String(20))
    channels = Column(Integer)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default="now()")

    versions = relationship("DatasetVersion", back_populates="dataset")