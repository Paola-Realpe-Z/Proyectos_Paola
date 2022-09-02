"""
NOMBRE: Paola Andrea Realpe Zambrano   SEMESTRE: VIII    PROGRAMA: Ing.Sistemas
"""

"""                            CLASE                                """
"""
numeros = [1, 2, 3, 4, 0]
arreglo = [1, "hola", 3, "dfst"]
personajes = ["shu", 200, "reiji", 201, "laito", 202, "kanato", 203, 
              "ayato", 205, "subaru", 206, "carla", 207, "shin", 208, 
              "kou", 209, "asuza", 210]


arregloslice = arreglo[1:3]

arregloslice1 = personajes[1:10]
arregloslice2 = personajes[1:-1]
arregloslice3 = personajes[5:10]


numeros.sort();

nombres = ['shu', 'Laito', 'carla']
nombres.sort();
print(nombres)

arregloextendido = numeros
arregloextendido.extend(personajes)
arregloextendido.index("shu",1)

dir(personajes) """


"""                            TAREA PAOLA                               """

"""Listas"""

familia = ["Liliana", "Paola", "Vilma", "martha", "Milton", "Harry", "olivia"]

codigo = [3, 8, 2, 10, 7, 1, 4, 6, 5, 9]

numRepetidos = [2, 1, 4, 2, 1, 0, 4, 5, 2]

numLetras = ["Alastor", 111, "Charlie", 222, "Vagie", 555, "Valentino", 333,
             "Angel", 666, "Vox", 223, "Niffy", 444, "Husk", 123, "Aine", 45]

"""Slices:  Operación para extraer elementos de una secuencia [inicio:fin]"""

listaslice1 = numLetras[0:10]
listaslice2 = numLetras[5:-5]
listaslice3 = numLetras[10:-1]


"""Sort:  Ordena la lista"""
print("Sort")
codigo.sort();
print(codigo)
print()

numRepetidos.sort();
print(numRepetidos)
print()

"""Distingue entre mayusculas y minusculas"""
familia.sort();
print(familia)
print()

"""No distingue entre mayusculas y minusculas"""
familia.sort(key = str.lower)
print(familia)
print()

"""Index: Devuelve el indice de su primera aparición """
print("Index")
print(numLetras.index("Valentino"))
print()

"""Append: Agrega un elemento al final de la lista """
print("Append")
numLetras.append("Paola")
print(numLetras)
print()

codigo.append("223")
print(codigo)
print()

"""Extend: Extiende la lista agregando un iterable al final """
print("Extend")
listaext = codigo
listaext.extend(familia)
print(codigo)
print()

"""Copy: Copia la lista y hace un duplicado de la misma """
print("Copy")
copiaNuevo = numLetras.copy()
print(copiaNuevo)
print()

"""Count: Cuenta la cantidad de veces que aparece un elemento en una lista """
print("Count")
print(numRepetidos.count(1))
print(numRepetidos.count(2))
print(numRepetidos.count(0))
print()

"""Pop: Devuelve el ultimo elemento de la lista y lo elimina """
print("Pop")
copiaNuevo.pop();
print(copiaNuevo)
print()

"""Remove: Borra un elemento de la lista"""
print("Remove")
copiaNuevo.remove("Charlie");
print(copiaNuevo)
print()

"""Reverse: Invierte el orden en la lista """
print("Reverse")
numRepetidos.reverse();
print(numRepetidos)
print()

"""Insert: Agrega un elemento en un indice """
print("Insert")
numRepetidos.insert(0, "Paola")
print(numRepetidos)
print()

"""Clear: Limpiar o borra la lista """
print("Clear")
numLetras.clear()
print(numLetras)
print()

