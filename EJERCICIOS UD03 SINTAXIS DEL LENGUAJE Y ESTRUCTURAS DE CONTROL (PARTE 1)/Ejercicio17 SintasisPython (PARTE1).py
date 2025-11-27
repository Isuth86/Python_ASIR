# Ejercicio 17 * Escriba un programa que simule un incio de sesión solicitando el nombre de usuario y contraseña, y mostrar un mensaje en pantalla, inicio correcto/ nombre de usuario incorrecto.
# Credenciales correctas.
usuario_correcto = "admin"
contrasena_correcta = "1234"

# Solicitar datos al usuario.
usuario = input("Introduce tu nombre de usuario: ")
contraseña = input("Introduce tu contraseña: ")

# Comprobar credenciales.
if usuario == usuario_correcto and contraseña == contrasena_correcta:
    print("Inicio de sesión correcto.")
elif usuario != usuario_correcto:
    print("Nombre de usuario incorrecto.")
else:
    print("Contraseña incorrecta.")
