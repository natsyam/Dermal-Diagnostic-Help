from datetime import datetime
import os
import shutil

import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session

from yolo_prediction import predict
from sql_app import models
from sql_app.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/upload/")
async def create_upload_file(
    file: UploadFile = File(...), db: Session = Depends(get_db)
):
    try:
        uploads_dir = "uploads"
        # Проверяем и создаем директорию, если необходимо
        os.makedirs(uploads_dir, exist_ok=True)
        # Сохраняем файл
        file_location = f"{uploads_dir}/{file.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)

        prediction = predict(file_location)

        # Сохраняем информацию о файле в базу данных
        db_file = models.MelanomaPhoto(
            upload_time=datetime.utcnow(), class_prediction=prediction
        )
        db.add(db_file)
        db.commit()
        db.refresh(db_file)

        return {"class_prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
