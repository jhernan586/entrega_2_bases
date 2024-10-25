from fastapi import APIRouter

router = APIRouter()

@router.get("/holaMundo/")
def hola_mundo():
    # Primera ruta de prueba
    print("Hola Mundo")
    return ("Hola Mundo")