usuarios = []

def agregar_usuario(nombre):
    usuarios.append(nombre)

def listar_usuarios():
    return usuarios

def buscar_usuario(nombre):
    return nombre in usuarios

def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Agregar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Salir")

# Pruebas básicas
print(listar_usuarios())
print(buscar_usuario("Elena"))