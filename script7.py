import json
import tkinter as tk

""" def entrada_datos(color_texto, color_fondo, lenguaje, region, sistema, capacidad):
    color_texto = input("color del texot: ")
    color_fondo = input("color del texot: ")
    lenguaje = input("lenguaje: ")
    region = input("regiont: ")
    sistema = input("sistema: ")
    capacidad = input("capacidad: ")

    APP = {
        "color_texto" : entrada_datos(color_texto),
        "color_fondo" : entrada_datos(color_fondo),
        "lenguaje" : entrada_datos(lenguaje),
        "region" : entrada_datos(region),
        "sistema" : entrada_datos(sistema),
        "capacidad" : entrada_datos(capacidad)
    }

app_json = json.dumps(entrada_datos('color_texto', 'color_fondo', 'lenguaje', 'region', 'sistema', 'capacidad'), indent=2, ensure_ascii=False) """
""" 

nombre_texto = input("nombre_texto: ")
color_fondo = input("color_fondo: ")
ancho = float(input("ancho: "))
alto = float(input("alto: "))

CONFIGURADOR = {
    "nombre_texto" : nombre_texto,
    "color_fondo" : color_fondo,
    "ancho" : ancho,
    "alto" : alto,
}

with open("fichero.json", "w", encoding="utf-8") as f:
    json.dump(CONFIGURADOR, f, indent= 2, ensure_ascii=False)

root = tk.Tk()
root.title("Programita")
mainframe = tk.Frame(root,background="black", width=1080, height=1920)
mainframe.grid(column=0, row=0)
root.mainloop() """

VENTANA = "ventana"
NOMBRE = "nombre"
COLOR = "color"
ALTURA = "altura"
ANCHURA = "ancho"


def guardar_configuracion():

    nombre = entrada_nombre.get()
    color = entrada_color.get()
    altura = entrada_altura.get()
    ancho = entrada_ancho.get()

    config = {VENTANA: {NOMBRE: nombre, COLOR: color, ALTURA: altura, ANCHURA: ancho}}

    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    mostrar_ventana()


def mostrar_ventana():
    try:

        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        nombre = config[VENTANA][NOMBRE]
        color = config[VENTANA][COLOR]
        altura = config[VENTANA][ALTURA]
        ancho = config[VENTANA][ANCHURA]

        main_window.title(nombre)
        main_window.geometry(f"{altura}x{ancho}")
        main_window.configure(bg=color)

    finally:

        for widget in main_window.winfo_children():
            widget.destroy()


# ==================================== VENTANA CONFIG

main_window = tk.Tk()
main_window.title("Configurador")
main_window.geometry("500x400")

titulo = tk.Label(main_window, text="Configuración de la ventana:", font=("Arial", 20))

titulo.pack(pady=20)

# ----------------------------------  NOMBRE

tk.Label(main_window, text="Nombre de la ventana:").pack()

entrada_nombre = tk.Entry(main_window)
entrada_nombre.pack()

# ----------------------------------  BG COLOR

tk.Label(main_window, text="Color de fondo:").pack()

entrada_color = tk.Entry(main_window)
entrada_color.pack()

# ---------------------------------- ALTO
#
tk.Label(main_window, text="Altura:").pack()

entrada_altura = tk.Entry(main_window)
entrada_altura.pack()

# ---------------------------------- ANCHO
#
tk.Label(main_window, text="Anchura:").pack()

entrada_ancho = tk.Entry(main_window)
entrada_ancho.pack()

# ---------------------------------- BOTON
#
boton = tk.Button(
    main_window, text="Aplicar configuración", command=guardar_configuracion
)

boton.pack(pady=25)


main_window.mainloop()
