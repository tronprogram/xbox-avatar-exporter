import os
import subprocess
import urllib.request

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) + os.sep
GMESH_PATH = os.path.join(CURRENT_DIR, 'gmesh.exe')
MESHEDIT_PATH = os.path.join(CURRENT_DIR, 'meshedit.exe')

GMESH_URL = "https://github.com/PMZeroSkyline/GPA-Mesh/releases/download/Release/gmesh.exe"
MESHEDIT_URL = "https://github.com/Ocublox/xbox-avatar-editor/releases/download/Main/meshedit.exe"

def download_file(url, path):
    print(f"Downloading {url}...")
    urllib.request.urlretrieve(url, path)
    print(f"Downloaded to {path}\n")

def ensure_tools_exist():
    if not os.path.exists(GMESH_PATH) or not os.path.exists(MESHEDIT_PATH):
        print("gmesh.exe / meshedit.exe not found!")
        choice = input("Would you like to download missing files? (y/n): ").lower()
        if choice != 'y':
            exit()
        if not os.path.exists(GMESH_PATH):
            download_file(GMESH_URL, GMESH_PATH)
        if not os.path.exists(MESHEDIT_PATH):
            download_file(MESHEDIT_URL, MESHEDIT_PATH)

def main():
    ensure_tools_exist()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Make sure the exported OBJ has the same name as the CSV.")
        name = input("Enter model name: ")
        temp_obj = f"{name}_temp.obj"
        final_obj = f"{name}_build.obj"

        subprocess.run([GMESH_PATH, "-s", "TEXCOORD", f"{name}.csv", f"{name}.obj", temp_obj])
        subprocess.run([MESHEDIT_PATH, temp_obj, final_obj])

        if os.path.exists(temp_obj):
            os.remove(temp_obj)

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
