import os
import shutil

# Copiar al igual que el comando cp -R en GNU/Linux
#shutil.copytree(src="../clase1/", dst="../clase1copia/")

# Ignorar ficheros .spec al copiar
#shutil.copytree(src="../clase1", dst="../clase1copia", ignore= shutil.ignore_patterns('*.spec'))

# Copiar ficheros situados en el mismo directorio
shutil.copy(src="../clase4/coche.py", dst="../clase4/buga.py")

# Mover (o cambiar de nombre al fichero) al igual que el comando mv en GNU/Linux
shutil.move(src="../clase4/buga.py", dst="buga.py")

# Mover un fichero usando la biblioteca os
os.rename("buga.py", "kk.py")

# Borrar un fichero
os.remove("kk.py")