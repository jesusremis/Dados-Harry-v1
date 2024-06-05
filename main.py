import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os

# Función para lanzar el dado
def tirar_dado(caras):
    #if not isinstance(caras, int) or caras <= 0: (para añadir una excepción o mensaje si no se selecciona un dado al pulsar en lanzar dado)
    return random.randint(1, caras)

# Función para actualizar el resultado y la imagen
def actualizar_resultado():
    resultado = tirar_dado(selected_caras.get())
    resultado_var.set(f"Resultado: {resultado}")
    
    #Si quieres ocultar la imagen de inicio, como pasaba en la v1
    #imagen_inicial_label.pack_forget()
    
    # Actualizar imagen del dado
    imagen_path = f"imagenes/dado_{selected_caras.get()}.jpg"
    try:
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((180, 180), Image.LANCZOS)
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label.config(image=imagen)
        imagen_label.image = imagen
    except Exception as e:
        print(f"No se pudo cargar la imagen: {e}")
    
    # Actualizar historial
    actualizar_historial(selected_caras.get(), resultado)

# Función para seleccionar el dado
def seleccionar_dado(caras):
    selected_caras.set(caras)

# Función para actualizar el historial
def actualizar_historial(caras, resultado):
    if len(historial) >= 10:
        historial.pop()
    historial.insert(0, f"D{caras}: {resultado}")
    historial_var.set("\n".join(historial))

# Crear la ventana principal
root = tk.Tk()
root.title("DADOS HARRY")
root.geometry("850x500")  # Establecer tamaño inicial de la ventana

# Establecer el icono de la ventana
icon_path = "imagenes/IMG_20200707_201112b.ico"
root.iconbitmap(icon_path)

# Variable para mostrar el resultado y el historial
resultado_var = tk.StringVar()
selected_caras = tk.IntVar()
historial = []
historial_var = tk.StringVar()

# Crear el marco superior para los botones de selección del dado
top_frame = ttk.Frame(root)
top_frame.pack(side="top", fill="x", pady=10)

#Crear los botones para seleccionar el dado
dados = [4, 6, 8, 10, 20, 100]
for dado in dados:
    miniatura_path = f"imagenes/miniatura_dado_{dado}.jpg"
    try:
        miniatura = Image.open(miniatura_path)
        miniatura = miniatura.resize((75, 75), Image.LANCZOS)  # Redimensionar la imagen a 50x50 píxeles
        miniatura = ImageTk.PhotoImage(miniatura)
        boton = ttk.Button(top_frame, image=miniatura, text=str(dado), compound="top", command=lambda d=dado: seleccionar_dado(d))
        boton.image = miniatura  # Mantener una referencia a la imagen
        boton.pack(side="left", padx=5, pady=5)
    except Exception as e:
        print(f"No se pudo cargar la miniatura: {e}")

# Crear los marcos para dividir la ventana
left_frame = ttk.Frame(root, width=400, height=500, padding=(10, 10, 10, 10))
left_frame.pack(side="left", fill="both", expand=True)

right_frame = ttk.Frame(root, width=400, height=500, padding=(10, 10, 10, 10))
right_frame.pack(side="right", fill="both", expand=True)

# Botón para lanzar el dado
boton_lanzar = ttk.Button(left_frame, text="LANZAR DADO", command=actualizar_resultado, style="TButton")
boton_lanzar.pack(pady=10)

# Configuración del estilo del botón
style = ttk.Style()
style.configure("TButton", font=("Times New Roman", 16, "bold"))

# Label para mostrar el resultado
resultado_label = ttk.Label(left_frame, textvariable=resultado_var, font=("Times New Roman", 18, "bold"))
resultado_label.pack(pady=10)

# Label para mostrar la imagen del dado
imagen_label = ttk.Label(left_frame)
imagen_label.pack(pady=10) #Retocada la posición de la imagen del dado

# Cargar y mostrar la imagen con varios dados al inicio
imagen_inicial_path = "imagenes/dados_varios.jpg"
try:
    imagen_inicial = Image.open(imagen_inicial_path)
    imagen_inicial = imagen_inicial.resize((200, 150), Image.LANCZOS)
    imagen_inicial = ImageTk.PhotoImage(imagen_inicial)
    imagen_inicial_label = ttk.Label(root, image=imagen_inicial)
    imagen_inicial_label.image = imagen_inicial  
    imagen_inicial_label.pack(pady=10)
except Exception as e:
    print(f"No se pudo cargar la imagen inicial: {e}")

# Label para mostrar el historial
historial_label = ttk.Label(right_frame, text="ÚLTIMAS TIRADAS", font=("Helvetica", 18, "bold"))
historial_label.pack(pady=10)

historial_text = ttk.Label(right_frame, textvariable=historial_var, font=("Helvetica", 14))
historial_text.pack(pady=10)


# Iniciar la interfaz gráfica
root.mainloop()