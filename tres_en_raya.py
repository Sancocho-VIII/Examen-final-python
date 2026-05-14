from random import randint
tablero=[]
jugada = 0 
class Tablero():
    def __init__(self, posicion):
        posicion=self.posicion
        jugador1= self.jugador1
        jugador2= self.jugador2
        simbolo1= self.simbolo1
        simbolo2= self.simbolo2
        return posicion
    def mostrar_tablero(con_numero=True):
        tablero=[[1,2,3],[4,5,6],[7,8,9]]
        for fila in tablero:
            print(fila)
    def colocar_ficha():
        while True:
          try:
            jugada=int(input("Elige una casilla del 1 al 9"))
            if isinstance(jugada, int) and 1<=jugada<=9:
                break
            else:
                print("Error, ingresa un numero del 1 al 9")
                continue
          except ValueError:
              print("Error, ingresa un numero del 1 al 9")



menu = True
jugar= False
historial = {
    "Utalio": "1" , "hermenegildo": "2"
}
while True:
    if  menu == True:
        print("===TRES EN RAYA===")
        print("1. Jugar    2. Ver historial     3. salir")
        inicio= int(input("Elige una opcion: "))
        if inicio == 1:
            jugar = True
            Tablero.mostrar_tablero()
            menu = False
        elif inicio == 2:
            print(historial)
        elif inicio == 3:
            print("Cerrando el juego...")
            menu = False
        else:
            print("Error, ingrese un numero que este dentro de las opciones")
    if jugar == True:
        Tablero.colocar_ficha()
