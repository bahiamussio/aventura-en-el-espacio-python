import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.nivel = 1
        self.experiencia = 0

    def atacar(self):
        return random.randint(10, 20) * self.nivel

    def recibir_dano(self, dano):
        self.salud -= dano
        if (self.salud) <= 0:
            print(f"{self.nombre} ha muerto. Game Over!")
        else:
            print(f"Te quedan {self.salud} puntos de vida.")

    def ganar_experiencia(self, experiencia):
        self.experiencia += experiencia
        if self.experiencia < 0:
            self.experiencia = 0  # Evita que la experiencia baje de 0
        print(f"{self.nombre} ahora tiene {self.experiencia} puntos de experiencia.")
    
        experiencia_necesaria = self.nivel * 100
        while self.experiencia >= experiencia_necesaria:
            self.nivel += 1
            self.experiencia -= experiencia_necesaria
            print(f"¡{self.nombre} ha subido al nivel {self.nivel}! 🚀")
