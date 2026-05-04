# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# productos = []
# class Producto(BaseModel):
#     nombre: str
#     precio: float
#     stock: int
    

# @app.post("/productos")
# def crear_producto(producto: Producto):
#     productos.append(producto)
#     return{"Mensaje": "Producto creado"}

# @app.get("/productos")
# def get_productos():
#     return productos

# @app.get("/productos/{producto_id}")
# def get_producto(producto_id: int):
#     return productos[producto_id]

# @app.put("/productos/{producto_id}")
# def actuazar_producto(producto_id: int, producto: Producto):
#     productos[producto_id] = producto
#     return{"Mensaje": "Producto actualizado"}

# @app.delete("/productos/{producto_id}")
# def eliminar_producto(producto_id: int):
#     productos.pop(producto_id)
#     return{"Mensaje": "Producto eliminado"}



# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Tareas(BaseModel):
#     titulo: str
#     descriipcion: str
#     completada: bool

# tareas = []

# @app.post("/tareas")
# def crear_tarea(tarea : Tareas):
#     tareas.append(tarea)
#     return{"Mensaje": "Tarea creada"}

# @app.get("/tareas")
# def mostrar_tareas():
#     return tareas

# @app.get("/tareas/{tarea_id}")
# def mostar_tarea_id(tarea_id: int):
#     return tareas[tarea_id]

# @app.put("/tareas/{tarea_id}")
# def modificar_tarea(tarea_id: int, tarea: Tareas):
#     tareas[tarea_id] = tarea
#     return{"Mensaje": "Tarea actualizada"}

# @app.delete("/tareas/{tarea_id}")
# def eliminar_tarea(tarea_id: int):
#     tareas.pop(tarea_id)
#     return{"Mensaje": "Tarea eliminada"}    

# --------------------------------------
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuarios(BaseModel):
    nombre: str
    email: str
    password: str
    edad: str

usuarios = []

@app.post("/usuarios")
def crear_usuarios(usuarios: Usuarios):
    usuarios.append(usuarios)
    return{"Mensaje": "Usuario creado"}
