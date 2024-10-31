from fastapi import APIRouter, HTTPException
from app.models import Cliente, Proyecto, Departamento, Empleado, Tarea, Empleado_Tarea 
from app.database import get_db_connection
from typing import List, Optional, Any, Dict 

router = APIRouter()

# Rutas para Clientes
@router.post("/clientes/", response_model=Cliente)
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

@router.get("/clientes/", response_model=List[Cliente])
def get_clientes():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    connection.close()
    return clientes

@router.get("/clientes/{cliente_id}", response_model=Cliente)
def get_cliente(cliente_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (cliente_id,))
    cliente = cursor.fetchone()
    cursor.close()
    connection.close()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.get("/clientes_proyectos/", response_model=List[Dict[str, Any]])
def get_clientes_proyectos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT c.id_cliente, c.nombre AS cliente_nombre, p.id_proyecto, p.nombre AS proyecto_nombre 
        FROM clientes c 
        INNER JOIN proyectos p ON c.id_cliente = p.id_cliente""")   
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

# Rutas para Proyectos
@router.post("/proyectos/", response_model=Proyecto)
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

@router.get("/proyectos/", response_model=List[Proyecto])
def get_proyectos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM proyectos")
    proyectos = cursor.fetchall()
    cursor.close()
    connection.close()
    return proyectos

@router.get("/proyectos/{proyecto_id}", response_model=Proyecto)
def get_proyecto(proyecto_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM proyectos WHERE id_proyecto = %s", (proyecto_id,))
    proyecto = cursor.fetchone()
    cursor.close()
    connection.close()
    if proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto

@router.get("/proyectos_clientes/", response_model=List[Dict[str, Any]])
def get_proyectos_clientes():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.id_proyecto, p.nombre AS proyecto_nombre, c.id_cliente, c.nombre AS cliente_nombre 
        FROM proyectos p 
        LEFT JOIN clientes c ON p.id_cliente = c.id_cliente
    """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

# Rutas para Departamentos
@router.post("/departamentos/", response_model=Departamento)
def create_departamento(departamento: Departamento):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO departamentos (nombre) VALUES (%s)", (departamento.nombre,))
    connection.commit()
    departamento.id_departamento = cursor.lastrowid
    cursor.close()
    connection.close()
    return departamento

@router.get("/departamentos/", response_model=List[Departamento])
def get_departamentos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM departamentos")
    departamentos = cursor.fetchall()
    cursor.close()
    connection.close()
    return departamentos

@router.get("/departamentos/{departamento_id}", response_model=Departamento)
def get_departamento(departamento_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM departamentos WHERE id_departamento = %s", (departamento_id,))
    departamento = cursor.fetchone()
    cursor.close()
    connection.close()
    if departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return departamento

# Rutas para Empleados
@router.post("/empleados/", response_model=Empleado)
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

@router.get("/empleados/", response_model=List[Empleado])
def get_empleados():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    cursor.close()
    connection.close()
    return empleados

@router.get("/empleados/{empleado_id}", response_model=Empleado)
def get_empleado(empleado_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados WHERE id_empleado = %s", (empleado_id,))
    empleado = cursor.fetchone()
    cursor.close()
    connection.close()
    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

#@router.get("/empleados con tareas/", response_model=List[Dict[str, Any]])
#def get_empleados_con_tareas():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT e.id_empleado, e.nombre AS empleado_nombre, COUNT(et.id_tarea) AS total_tareas
        FROM empleados e 
        LEFT JOIN empleado_tarea et ON e.id_empleado = et.id_empleado
        GROUP BY e.id_empleado
    """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results  

# Rutas para Tareas
@router.post("/tareas/", response_model=Tarea)
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

@router.get("/tareas/", response_model=List[Tarea])
def get_tareas():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    cursor.close()
    connection.close()
    return tareas

@router.get("/tareas/{tarea_id}", response_model=Tarea)
def get_tarea(tarea_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tareas WHERE id_tarea = %s", (tarea_id,))
    tarea = cursor.fetchone()
    cursor.close()
    connection.close()
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.get("/total tareas por proyecto/", response_model=List[Dict[str, Any]])
def get_total_tareas_por_proyecto():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.id_proyecto, p.nombre AS proyecto_nombre, COUNT(t.id_tarea) AS total_tareas
        FROM proyectos p 
        LEFT JOIN tareas t ON p.id_proyecto = t.id_proyecto
        GROUP BY p.id_proyecto
    """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

@router.get("/promedio de duracion tareas por proyecto/", response_model=List[Dict[str, Any]])
def get_promedio_duracion_tareas_por_proyecto():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.id_proyecto, p.nombre AS proyecto_nombre, AVG(TIMESTAMPDIFF(DAY, t.fecha_inicio, t.fecha_fin)) AS promedio_duracion
        FROM proyectos p 
        INNER JOIN tareas t ON p.id_proyecto = t.id_proyecto
        GROUP BY p.id_proyecto
    """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

@router.get("/tarea mas larga por proyecto/{proyecto_id}", response_model=Dict[str, Any])
def get_tarea_mas_larga_por_proyecto(proyecto_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT t.id_tarea, t.nombre AS tarea_nombre, MAX(TIMESTAMPDIFF(DAY, t.fecha_inicio, t.fecha_fin)) AS duracion_maxima
        FROM tareas t 
        WHERE t.id_proyecto = %s
        GROUP BY t.id_tarea
        ORDER BY duracion_maxima DESC
        LIMIT 1
    """, (proyecto_id,))
    tarea = cursor.fetchone()
    cursor.close()
    connection.close()
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@router.get("/tarea mas corta por proyecto/{proyecto_id}", response_model=Dict[str, Any])
def get_tarea_mas_corta_por_proyecto(proyecto_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT t.id_tarea, t.nombre AS tarea_nombre, MIN(TIMESTAMPDIFF(DAY, t.fecha_inicio, t.fecha_fin)) AS duracion_minima
        FROM tareas t 
        WHERE t.id_proyecto = %s
        GROUP BY t.id_tarea
        ORDER BY duracion_minima ASC
        LIMIT 1
    """, (proyecto_id,))
    tarea = cursor.fetchone()
    cursor.close()
    connection.close()
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

#@router.get("/promedio tareas por departamento/", response_model=List[Dict[str, Any]])
#def get_promedio_tareas_por_departamento():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT d.id_departamento, d.nombre AS departamento_nombre, AVG(t.total_tareas) AS promedio_tareas
        FROM departamentos d 
        LEFT JOIN (
            SELECT p.id_departamento, COUNT(t.id_tarea) AS total_tareas
            FROM proyectos p 
            LEFT JOIN tareas t ON p.id_proyecto = t.id_proyecto
            GROUP BY p.id_departamento
        ) AS t ON d.id_departamento = t.id_departamento
        GROUP BY d.id_departamento
    """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

# Rutas para EmpleadoTarea
#@router.post("/empleado_tarea/")
#def asignar_empleado_tarea(empleado_tarea: Empleado_Tarea):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO empleado_tarea (id_empleado, id_tarea) VALUES (%s, %s)", 
                   (empleado_tarea.id_empleado, empleado_tarea.id_tarea))
    connection.commit()
    cursor.close()
    connection.close()
    return {"mensaje": "Empleado asignado a la tarea correctamente"}

#@router.get("/empleado_tarea/")
#def obtener_empleados_tarea():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleado_tarea")
    empleado_tarea = cursor.fetchall()
    cursor.close()
    connection.close()
    return empleado_tarea