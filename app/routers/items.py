from fastapi import APIRouter

router = APIRouter(prefix="/celulares", tags=["Celulares"])

@router.get("/")
def listar_celulares():
    return {"celulares": ["Iphone XR", "Android", "Xiamoi 15"]}