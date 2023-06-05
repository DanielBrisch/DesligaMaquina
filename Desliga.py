import subprocess

comando = "shutdown /s /t 0" 

try: 
    subprocess.Popen("powershell", stdin=subprocess.PIPE, text=True).communicate(comando)
except FileNotFoundError:
    print("error")
