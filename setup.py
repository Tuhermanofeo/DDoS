import os
import platform
import time

def instalar_figlet():
    sistema = platform.system().lower()
    print(f"Detectando sistema operativo: {sistema}\n")

    if "android" in os.getenv("PREFIX", ""):
        os.system("pkg install -y figlet")
    elif "linux" in sistema:
        # Intenta con apt o pacman según la distro
        if os.system("sudo apt-get install -y figlet") != 0:
            os.system("sudo pacman -S --noconfirm figlet")
    elif "windows" in sistema:
        os.system("choco install figlet -y")
    else:
        print("Sistema operativo no reconocido. Instala figlet manualmente.")

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# --- Proceso principal ---
print("Instalando dependencias...\n")
instalar_figlet()
limpiar_pantalla()
time.sleep(2)
print("30%")
time.sleep(4)

os.system("pip install -r requirements.txt")
limpiar_pantalla()

print("50%")
os.system("clear")
time.sleep(7)
print("100%")
time.sleep(3)
os.system("clear")

os.system("figlet Welcome to fsociety!")
time.sleep(5)
