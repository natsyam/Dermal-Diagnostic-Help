from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime


class MelanomaPhoto(Base):
    __tablename__ = "melanoma_photos"

    id = Column(Integer, primary_key=True, index=True)
    upload_time = Column(DateTime, default=datetime.utcnow)
    class_prediction = Column(String)
