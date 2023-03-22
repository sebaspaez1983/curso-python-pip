import random

class JuegoPiedraPapelTijeras:
    def __init__(self):
        self.opciones = ["piedra", "papel", "tijeras"]
        self.resultado = ""
    
    def jugar(self, jugador):
        # Elige una opción aleatoria para la computadora
        computadora = random.choice(self.opciones)

        # Validación de la entrada del jugador
        if jugador not in self.opciones:
            self.resultado = "Entrada inválida. Inténtalo de nuevo."
            return self.resultado

        # Mostrar las opciones elegidas por el jugador y la computadora
        self.resultado = f"Jugador: {jugador}\nComputadora: {computadora}\n"

        # Comprobar el resultado del juego
        if jugador == computadora:
            self.resultado += "Empate."
        elif (jugador == "piedra" and computadora == "tijeras") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijeras" and computadora == "papel"):
            self.resultado += "Jugador gana."
        else:
            self.resultado += "Computadora gana."
        
        return self.resultado
    
juego = JuegoPiedraPapelTijeras()

while True:
    jugador = input("Elige piedra, papel o tijeras: ").lower()
    resultado = juego.jugar(jugador)
    print(resultado)

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != "s":
        break