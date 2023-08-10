from fastapi import FastAPI

app = FastAPI(prefix='/products')
#uvicorn products:app --reload

products_list = ["P1","P2","P3"]

@app.get("/products/")
async def products():
    return products_list
