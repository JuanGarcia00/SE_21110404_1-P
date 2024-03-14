import json  # Importar el módulo json para trabajar con archivos JSON

# Intentar cargar los conocimientos precargados desde el archivo conocimientos.json
try:
    with open("conocimientos.json", "r") as file:
        conocimientos = json.load(file)
except FileNotFoundError:  # Si el archivo no existe, inicializar con conocimientos predeterminados
    conocimientos = {
        "Hola": "¡Hola! ¿Cómo estás?",
        "Cómo estás?": "Estoy bien, gracias por preguntar.",
        "De qué te gustaría hablar?": "Podemos hablar de cualquier cosa. ¿Tienes algún tema en mente?"
    }

# Función para responder a los mensajes del usuario
def responder(mensaje):
    if mensaje in conocimientos:  # Si el mensaje está en conocimientos, devolver la respuesta correspondiente
        return conocimientos[mensaje]
    else:
        # Solicitar al usuario una nueva respuesta para el mensaje y agregarla a conocimientos
        nuevo_conocimiento = input(f"No sé cómo responder a '{mensaje}'. ¿Qué debería responder? ")
        conocimientos[mensaje] = nuevo_conocimiento
        # Guardar los conocimientos actualizados en el archivo conocimientos.json
        with open("conocimientos.json", "w") as file:
            json.dump(conocimientos, file)
        return "¡Gracias por enseñarme algo nuevo!"  # Devolver un mensaje de agradecimiento

# Función principal del chatbot
def chat():
    print("Bienvenido al ChatBot!")
    while True:
        mensaje_usuario = input("Tú: ")  # Solicitar al usuario un mensaje
        respuesta = responder(mensaje_usuario)  # Obtener la respuesta del chatbot
        print("ChatBot:", respuesta)  # Imprimir la respuesta del chatbot
        if mensaje_usuario.lower() == "adiós":  # Salir del bucle si el usuario escribe "adiós"
            print("Hasta luego!")
            break

# Ejecutar el chatbot
if __name__ == "__main__":
    chat()  # Llamar a la función chat para iniciar la conversación
