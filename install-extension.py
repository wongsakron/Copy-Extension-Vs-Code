import subprocess

lst = subprocess.run(['cmd', '/c', 'code --list-extensions'],stdout=subprocess.PIPE,text=True)

f = open("install-extension.txt","w")
[f.write(f'code --install-extension {i}\n') for i in lst.stdout.split()]
f.close()
