usuarios = []

def agregar_usuario(nombre):
    usuarios.append(nombre)

def listar_usuarios():
    return usuarios

def buscar_usuario(nombre):
    return nombre in usuarios