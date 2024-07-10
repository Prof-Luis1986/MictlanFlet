import os
import subprocess
import time
import flet as ft

def main(page: ft.Page):
    # Obtener el directorio de trabajo actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Rutas relativas para los recursos
    audio_base_path = os.path.join(current_dir, "assets/Audios")
    image_base_path = os.path.join(current_dir, "assets/Imagenes")
    
    # Se agrega el audio de fondo
    Fondo = ft.Audio(
        src=os.path.join(audio_base_path, "Danza_a_Mictlantecuhtli.mp3"), autoplay=True, volume=1, balance=0
    )
    page.overlay.append(Fondo)
    
    # Se agrega el audio del séptimo nivel
    SeptimoNivel = ft.Audio(
        src=os.path.join(audio_base_path, "Septimo_Nivel.mp3"), autoplay=False, volume=1, balance=0
    )
    page.overlay.append(SeptimoNivel)
    
    page.title = "El Mictlan-Nivel 7"
    page.bgcolor = "#000000"
    page.fgcolor = "#FFFFFF"
    
    # Tamaño uniforme para todas las imágenes
    image_width = 500
    image_height = 500
    
    img = ft.Image(
        src=os.path.join(image_base_path, "Septimo-Nivel.jpeg"),
        width=image_width, height=image_height, fit="contain"
    )
    
    btnPlay = ft.ElevatedButton("Da Click", on_click=lambda _: SeptimoNivel.play())
    btnVolver = ft.ElevatedButton("Volver", on_click=lambda _: volver_a_main())
    
    def volver_a_main():
        with open(os.path.join(current_dir, "control.txt"), "w") as f:
            f.write("main")
        page.window_close()
        time.sleep(1)
        subprocess.Popen(["python3", os.path.join(current_dir, "main.py")])
    
    page.add(
        ft.Column(
            alignment="center",
            controls=[
                ft.Row(
                    alignment="center",
                    controls=[img]
                ),
                ft.Row(
                    alignment="center",
                    controls=[btnPlay, btnVolver]
                )
            ]
        )
    )

ft.app(target=main)
