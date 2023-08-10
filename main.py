from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from utils.operation import sum
from routers import user, productsRouter


app = FastAPI()
#app = FastAPI()
app.include_router(productsRouter.router)
app.include_router(user.router)
app.mount("/static", StaticFiles(directory = "static"), name = 'static')

#main:app --reload

@app.get("/")
async def root():  
    return "¡Hola Api!"

@app.get("/sumAct")
async def root(n1: int, n2: int):  # request asyncronic
    return sum(n1, n2)

