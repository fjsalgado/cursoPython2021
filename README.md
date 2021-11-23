# Crear ambiente virtual en Windows para enlazarlo con GitHub
python -m venv CursoPython2021

# Habilitar ejecución scripts en PowerShell
Set-ExecutionPolicy Unrestricted -Scope Process

# Activar entorno virtual
.\Scripts\activate

# Acceder al intérprete de Python
python

# Salir del intérprete
CTRL + Z

# Ver palabras reservadas
>>> import keyword
>>> print(keyword.kwlist)

# Importar módulo de compilación
>>> import py_compile

# Importar módulo de sistema operativo
>>> import os

# Importar módulo de depuración (permite detener la ejecución o hacerla paso a paso)
>>> import pdb

# Ver ruta desde la que estás en el intérprete
os.getcwd()

# Instalar pip (instalador de pkts de python)
python -m pip install

# Instalar módulo pandas (librería para el manejo y análisis de estructuras de datos)
pip install pandas

# Ejecutar un fichero python
python hola.py

# Compilar fichero python (necesita importar módulo de compilación) => Crea un .pyc en __pycache__
>>> import py_compile
>>> py_compile.compile("hola.py")

# Instalar módulo para generar .exe a partir de los de python
pip install pyinstaller

# Generar ejecutable
pyinstaller hola.py

# Ejecutar exe
./dist/hola/hola.exe

# Atributos de un objeto (identidad, tipo, valor)
>>> x ="Hola"
>>> id(x)
>>> type(x)
>>> x

# Datos integrados (lista, set, diccionario...)
>>> list([1,2,3,3]) => [1,2,3,3]
>>> set([1,2,3,3]) => [2,3,1]
>>> frozenset([1,2,3,3]) => [1,3,2] e inmutable

# Listas
>>> [3,6,6] => por defecto crea una lista
>>> list('123') => [1,2,3] ojo
>>> list(['123']) => ['123'] ojo
>>> frutas = ['manzana','pera','banana']
>>> frutas[0] => 'manzana'
>>> frutas[-1] => 'banana', sería igual a frutas[2], el negativo provoca que empiece a contar desde el final
>>> frutas.append('fresa')
>>> frutas.index('fresa')
>>> frutas.insert(1,'mandarina') => Se añade en la posición
>>> frutas.extend(['kiwi','piña']) => Se añaden al final
>>> frutas + ['kiwi','piña'] => Se añaden al final
>>> del frutas[-1] => Borra último elemento
>>> frutas.remove('banana') => Borra elemento
>>> frutas.pop() => Extrae elemento y lo elimina
>>> frutas.pop(2) => Extrae elemento en posición 2
>>> frutas.sort() => Ordena de forma natural (creciente)
>>> frutas.sort(reverse=True) => Ordena de forma decreciente
>>> frutas.reverse() => Invierte ordenación
>>> sorted(frutas) => Ordena pero devuelve copia sin alterar original
>>> sorted(frutas, reverse=True)
>>> len(frutas) => Tamaño de la lista
>>> frutas[:3] => 3 primeras frutas (0..2)
>>> frutas[1:3] => 2 frutas (1..2)
>>> frutas[-3:] => 3 últimas frutas
>>> frutas2 = frutas[:] => Crea una copia de la lista
>>> for fruta in frutas:
>>>     print(fruta)
>>>     print(f"Nombre de la fruta: {fruta}")
>>>     print("Nombre de la fruta:", fruta)

# Tuplas (muy parecidas a las listas pero inmutables)
>>> tupla1 = ('texto1','texto2')
>>> tupla1.append('texto3') => ERROR (son inmutables)

# Diccionarios
>>> mapa = {1:'a',2:'b',3:'c',4:'d'}
>>> mapa[2] => 'b' devuelve error si la clave no existe
>>> mapa.get(2) => 'b' devuelve None si la clave no existe

# Instalar y ejecutar Jupyter (kernel con entorno web)
pip install jupyter
jupiter notebook

# Instalar y ejecutar IPython (shell interactiva para python)
pip install ipython
ipython

# Comandos útiles de IPython
? => introducción a la shell
%quickref => referencia rápida
!dir => para lanzar comandos de windows
!echo "Hoy es martes"
!date => retorna fecha actual
!python hola.py %debug => Ejecuta el fichero y si falla iría al primer error permitiendo depurar
%timeit statement => Mide tiempo de ejecución de la sentencia (se podría usar también con un bloque de código)

# Subir contenido a github
git init
git add -A
git commit -m "Primer commit"
git remote add origin https://github.com/fjsalgado/cursoPython2021.git
git push origin master
git remote set-url origin https://github.com/fjsalgado/cursoPython2021.git => Si se quiere cambiar la URL del repositorio
git remote show origin => Se mostraría el repositorio con el que está vinculado
git fetch origin master => Sincroniza en local con los cambios del repositorio
git pull origin master => Se descarga los cambios hechos en el repositorio
git status => Te da información sobre si hay algo pendiente de subir y la rama a la que se está conectado

# Variables
>>> a1, a2 = 1, 2 => Definición múltiple de variables
>>> a1, a2 = a2, a1 => Intercambio de valores
>>> del a2 => Eliminaría la variable a2
>>> print(f'El texto de a2 es {a2}') => F string permite incluir variables
>>> print('El texto de a2 es', {a2}) => Similar al comando anterior

# Funciones internas (built-in functions)
>>> int('12') => 12
>>> str(3.14) => '3.14'

# Función productiva => Aquella que devuelve algún valor
# Función nula => No devuelve ningún valor

# Módulos => Bibliotecas que suministra python para ampliar funcionalidades (similar a paquetes importados de JAVA)
import math

# OJO los objetos no se liberan (como en JAVA) => Hay que ir borrándolos cuando ya no se usan
del objeto

# Ver lista de métodos de un módulo
>>> import builtins
>>> dir(sys)

# Webserver de python
python -m http.server 8000 => Desde un navegador luego hacer http://localhost:8000

