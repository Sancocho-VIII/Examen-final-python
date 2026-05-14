## PARTE A 
1. D
2. B
3. A
4. B
5. B
6. B
7. B
8. B
9. C
10. C
11. A
12. B
13. C
14. B 
15. B
## PARTE B
### Pregunta 1
Un algoritmo es una serie de instrucciones o pasos para resolver un problema, una analogia para entender los algoritmos es pensar como que son una receta. Para resolver un problema de programacion lo primero que hago es: identificar lo que me pide, planificar una estrategia antes de escribir el codigo, comenzar a escribir el codigo y probarlo regularmante hasta resolver el problema.
### Pregunta 2
En una funcion si usas print(), al llamar la funcion esta solo imprimira el resultado, pero este resultado no se guarda ni puede ser utilizado. Lo usaria cuando la funcion me devuelve un texto el cual no utilizo para operar con el. Por otro lado, el return devuelve el dato al llamar la funcion, y este puede ser utilizado en el codigo. Lo usaria cuando el objetivo de la funcion es retornar un dato usado para calculos o operaciones mas adelante en el codigo.
### Pregunta 3 
El scope o alcance de una variable es en pocas palanbras, hasta donde puede ser utilizada esa variable en el codigo. Por ejemplo, si una variable se crea o se crea dentro de una funcion, esta no puede ser utilizada fuera de ella, a esto se le llama una variable local, es decir, solo la conocen dentro de la funcion. Por otro lado, una variable global puede ser alcanzada en todo el codigo.
### Pregunta 4 
Una lista es usada para guardar muchos elementos en una variable. Estas son mutables y sirven para resolver problemas con un mayor orden. 
###Para agregar elementos con un for:
lista_contar = []
x= int(input("cuantos numeros quieres contar? "))
for i in range(1, x):
	lista_contar.append(i)
###Para recorrer la lista con un for:
lista=[]
for elemento in lista:
	print(elemento)
### Pregunta 5 
El metodo __init__ es utilizado como una funcion para definir cualidades especificas para una clase. Se puede utilizar para aumentar caracteristicas en una clase hija usando __init__ denuevo, y al usar super(), se llaman las clases del init del padre. El self es usado para que al atribuir metodos dentro de una clase, esta sepa siempre que se refiere a la dicha clase, lo cual hace que la herencia sea posible, ya que el metodo siempre va a funcionar con (self).
