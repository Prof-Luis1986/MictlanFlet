import flet as ft
import subprocess
import os
import time

def main(page: ft.Page):
    # Establecer el tamaño por defecto de la ventana
    page.window.width = 700
    page.window.height = 750
    
    # Obtener el directorio de trabajo actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Rutas absolutas
    audio_base_path = os.path.join(current_dir, "assets/Audios/")
    image_base_path = os.path.join(current_dir, "assets/Imagenes/")
    
    # Verificar rutas absolutas
    print("Ruta audio de fondo:", os.path.join(audio_base_path, "Danza_a_Mictlantecuhtli.mp3"))
    print("Ruta intro audio:", os.path.join(audio_base_path, "Intro.mp3"))
    print("Ruta imagen primer nivel:", os.path.join(image_base_path, "Primer-Nivel.jpeg"))
    
    # Verificar existencia de archivos
    print("Verificando existencia de archivos...")
    for img in ["Primer-Nivel.jpeg", "Segundo-Nivel.jpeg", "Tercer-Nivel.png", "Cuarto-Nivel.jpeg", "Quinto-Nivel.jpeg", "Sexto-Nivel.jpeg", "Septimo-Nivel.jpeg", "Octavo-Nivel.png", "Noveno-Nivel.jpeg"]:
        img_path = os.path.join(image_base_path, img)
        print(f"{img_path}: {'Existe' if os.path.isfile(img_path) else 'No existe'}")
    
    # Se agrega el audio de fondo
    Fondo = ft.Audio(
        src=os.path.join(audio_base_path, "Danza_a_Mictlantecuhtli.mp3"), autoplay=True, volume=1, balance=0
    )
    page.overlay.append(Fondo)

    # Se agrega el audio de intro
    intro = ft.Audio(
        src=os.path.join(audio_base_path, "Intro.mp3"), autoplay=False
    )
    page.overlay.append(intro)

    # Configuración de la página
    page.title = "El Mictlan"
    page.bgcolor = "#000000"
    page.fgcolor = "#FFFFFF"

    # Tamaño uniforme para todas las imágenes
    image_width = 150
    image_height = 150

    # Función para abrir el primer nivel
    def abrir_nivel(nivel):
        def _abrir_nivel(e):
            # Crear archivo de control
            with open("control.txt", "w") as f:
                f.write(f"Nivel{nivel}")
            # Cerrar la aplicación Flet actual
            page.window_close()
            # Esperar un momento para asegurarse de que se cierre
            time.sleep(1)
            # Iniciar el nuevo proceso
            subprocess.Popen(["python3", f"Nivel{nivel}.py"])
        return _abrir_nivel

    # Variable para llevar el estado de reproducción del audio
    audio_playing = False

    # Función para reproducir/pausar el audio
    def toggle_audio(e):
        nonlocal audio_playing
        if audio_playing:
            intro.pause()
            music_button.icon = ft.icons.PLAY_CIRCLE_FILLED_ROUNDED
            music_button.tooltip = "Reproducir Intro"
        else:
            intro.play()
            music_button.icon = ft.icons.PAUSE_CIRCLE_FILLED_ROUNDED
            music_button.tooltip = "Pausar Intro"
        audio_playing = not audio_playing
        music_button.update()

    # Creación de componentes de la interfaz
    niveles = [
        ("Primer Nivel", "Primer-Nivel.jpeg"),
        ("Segundo Nivel", "Segundo-Nivel.jpeg"),
        ("Tercer Nivel", "Tercer-Nivel.png"),
        ("Cuarto Nivel", "Cuarto-Nivel.jpeg"),
        ("Quinto Nivel", "Quinto-Nivel.jpeg"),
        ("Sexto Nivel", "Sexto-Nivel.jpeg"),
        ("Séptimo Nivel", "Septimo-Nivel.jpeg"),
        ("Octavo Nivel", "Octavo-Nivel.png"),
        ("Noveno Nivel", "Noveno-Nivel.jpeg"),
    ]

    controls = []
    for i, (text, img) in enumerate(niveles, start=1):
        btn = ft.ElevatedButton(text=text, on_click=abrir_nivel(i))
        img_path = os.path.join(image_base_path, img)
        img = ft.Image(
            src=img_path,
            width=image_width, height=image_height, fit="contain"
        )
        controls.append(ft.Column(alignment="center", spacing=10, controls=[btn, img]))

    # Botón de música
    music_button = ft.IconButton(
        icon=ft.icons.PLAY_CIRCLE_FILLED_ROUNDED,
        icon_color="blue400",
        icon_size=30,
        tooltip="Reproducir Intro",
        on_click=toggle_audio
    )

    # Añadir el botón de música a la primera fila
    page.add(
        ft.Row(
            alignment="start",  # Alineación a la izquierda
            spacing=20,  # Espaciado entre los controles en la fila
            controls=[music_button]  # Botón de música alineado a la izquierda
        )
    )

    # Añadir los elementos de los niveles
    for i in range(0, len(controls), 3):
        page.add(
            ft.Row(
                alignment="center",
                spacing=20,
                controls=controls[i:i + 3]
            )
        )

ft.app(target=main)
