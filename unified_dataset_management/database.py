from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL 連接字符串
DATABASE_URL = "postgresql://admin:password@localhost:5432/unified_db"

# 創建數據庫引擎
engine = create_engine(DATABASE_URL)

# 創建會話
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基本模型類
Base = declarative_base()

# 數據庫依賴
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

