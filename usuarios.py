# Lista donde se almacenan los usuarios
usuarios = []

# Agrega un usuario a la lista
def agregar_usuario(nombre):
    usuarios.append(nombre)

# Devuelve todos los usuarios registrados
def listar_usuarios():
    return usuarios

# Busca un usuario por nombre
def buscar_usuario(nombre):
    return nombre in usuarios

# Muestra el menú principal
def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Agregar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Salir")

# Pruebas básicas de funcionamiento
mostrar_menu()

agregar_usuario("Elena")

print("Usuarios registrados:", listar_usuarios())
print("¿Existe Elena?", buscar_usuario("Elena"))