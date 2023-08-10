from fastapi import APIRouter

router = APIRouter(prefix='/products', tags=['products'], 
                   responses={404: {"message":"No encontrado"}})
#uvicorn products:app --reload

products_list = ["P1","P2","P3"]

@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id : int):
    return products_list[id]
+