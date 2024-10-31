from fastapi import APIRouter, HTTPException
from app.models import Cliente, Proyecto, Departamento, Empleado, Tarea, EmpleadoTarea 
from app.database import get_db_connection
from typing import List
from fastapi import FastAPI


#router = APIRouter()

#@router.get("/holaMundo/")
#def hola_mundo():
#    # Primera ruta de prueba
#    print("Hola Mundo")
#    return ("Hola Mundo")

router = APIRouter()
app = FastAPI()

# Rutas para Clientes
@app.post("/clientes/", response_model=Cliente)
def create_cliente(cliente: Cliente):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)", 
                   (cliente.nombre, cliente.email, cliente.telefono))
    connection.commit()
    cliente.id_cliente = cursor.lastrowid
    cursor.close()
    connection.close()
    return cliente

@app.get("/clientes/", response_model=List[Cliente])
def get_clientes():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    connection.close()
    return clientes

# Rutas para Proyectos
@app.post("/proyectos/", response_model=Proyecto)
def create_proyecto(proyecto: Proyecto):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO proyectos (nombre, descripcion, fecha_inicio, fecha_fin, id_cliente) VALUES (%s, %s, %s, %s, %s)",
                   (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_fin, proyecto.id_cliente))
    connection.commit()
    proyecto.id_proyecto = cursor.lastrowid
    cursor.close()
    connection.close()
    return proyecto

@app.get("/proyectos/", response_model=List[Proyecto])
def get_proyectos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM proyectos")
    proyectos = cursor.fetchall()
    cursor.close()
    connection.close()
    return proyectos

# Rutas para Departamentos
@app.post("/departamentos/", response_model=Departamento)
def create_departamento(departamento: Departamento):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO departamentos (nombre) VALUES (%s)", (departamento.nombre,))
    connection.commit()
    departamento.id_departamento = cursor.lastrowid
    cursor.close()
    connection.close()
    return departamento

@app.get("/departamentos/", response_model=List[Departamento])
def get_departamentos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM departamentos")
    departamentos = cursor.fetchall()
    cursor.close()
    connection.close()
    return departamentos

# Rutas para Empleados
@app.post("/empleados/", response_model=Empleado)
def create_empleado(empleado: Empleado):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO empleados (nombre, email, telefono, id_departamento) VALUES (%s, %s, %s, %s)", 
                   (empleado.nombre, empleado.email, empleado.telefono, empleado.id_departamento))
    connection.commit()
    empleado.id_empleado = cursor.lastrowid
    cursor.close()
    connection.close()
    return empleado

@app.get("/empleados/", response_model=List[Empleado])
def get_empleados():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    cursor.close()
    connection.close()
    return empleados

# Rutas para Tareas
@app.post("/tareas/", response_model=Tarea)
def create_tarea(tarea: Tarea):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tareas (nombre, descripcion, fecha_inicio, fecha_fin, id_proyecto) VALUES (%s, %s, %s, %s, %s)",
                   (tarea.nombre, tarea.descripcion, tarea.fecha_inicio, tarea.fecha_fin, tarea.id_proyecto))
    connection.commit()
    tarea.id_tarea = cursor.lastrowid
    cursor.close()
    connection.close()
    return tarea

@app.get("/tareas/", response_model=List[Tarea])
def get_tareas():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    cursor.close()
    connection.close()
    return tareas