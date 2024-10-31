from fastapi import FastAPI
from app.routes import router
from app.routes import Cliente, Proyecto, Departamento, Empleado, Tarea, EmpleadoTarea
app = FastAPI()

app.include_router(router)

app.include_router(Cliente.router)
app.include_router(Proyecto.router)
app.include_router(Departamento.router)
app.include_router(Empleado.router)
app.include_router(Tarea.router)
app.include_router(EmpleadoTarea.router)
