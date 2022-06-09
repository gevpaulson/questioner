from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def project_description():
    """ Метод получения информации о главной странице"""
    return {"message": "My pet project for learning the fastapi"}

