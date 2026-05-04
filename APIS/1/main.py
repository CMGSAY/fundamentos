from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Mensaje": "Hola Mundo "}

# lista donde guardamos los datos que se van a ingresar
users = []

# lo  que cree es que aqui creamos la funcion post para que nos cree los usuarios
# y estos se guardan en la lista
@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return{"Mensaje": "Usuario creado"}

# aqui no mucho le entiendo pero se que es para mostrar los usuarios
# pero no entiendo que hace ("/users")
# tampoco en que moometo se llama a la lista para mostar los usuarios
@app.get("/users")
def get_users():
    return users

# aqui tampoco le entiendo pero se que es para mostrar un usuario por su id
# pero en ningun momento se llama a la lista
# y atmpco definimos el id
# esta liena de codigo no la entiendo ((user_id: int)
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return user[user_id]

# aqui se se actualiza el usuario
# aqui creo que se llama al id no?
# yaqui no entiendo user_id: int, user: dict):
@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    users[user_id] = user
    return{"Mensaje": "Usuario actualizado"}

# aqui si se que el pop es para eliminar de la lista 
# pero no entiendo que significa mas el cosigo
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    users.pop(user_id)
    return{"Mensaje": "Usuario eliminado"}