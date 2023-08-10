from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():  # request asyncronic
    return "¡Hola Api!"


@app.get("/sumAct")
async def root(n1: int, n2: int):  # request asyncronic
    return n1 * n2


# protocolo http es el usado por fast api
