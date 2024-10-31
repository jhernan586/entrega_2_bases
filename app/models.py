from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Optional

class Cliente(BaseModel):
    id_cliente: Optional[int]
    nombre: str = Field(description="Nombre completo del cliente(campo requerido)")
    email: str = Field(description="Correo electrónico del cliente(campo requerido)")
    telefono: str

class Proyecto(BaseModel):
    id_proyecto: Optional[int]
    nombre: str = Field(description="Nombre completo del proyecto(camporequerido)")
    descripcion: str = Field(description="Proporciona un descripción detallada(campo requerido)")
    fecha_inicio: date 
    fecha_fin: date
    id_cliente: int

class Departamento(BaseModel):
    id_departamento: Optional[int]
    nombre: str

class Empleado(BaseModel):
    id_empleado: Optional[int]
    nombre: str = Field(description="Nombre completo del empleado(campo requerido)")
    email: str = Field(description="Correo electrónico del empleado(campo requerido)")
    telefono: str
    id_departamento: int

class Tarea(BaseModel):
    id_tarea: Optional[int]
    nombre: str = Field(description="Nombre completo de la tarea a realizar(campo requerido)")
    descripcion: str = Field(description="Especifica la descripcion completa de la tarea(campo requerido)")
    fecha_inicio: date
    fecha_fin: date
    id_proyecto: int

class EmpleadoTarea(BaseModel):
    id_empleado: int
    id_tarea: int