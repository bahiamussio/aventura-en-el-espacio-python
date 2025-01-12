import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador

def main():
    nombre_jugador = input("¡Bienvenido a la aventura en el Espacio! 🚀 Por favor, ingresa tu nombre: ")
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Monstruo", 70, 15),
    ]

    enemigos_derrotados = []

    print("¡Comienza la aventura! Buena suerte.")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue

        print(f"Te has encontrado con un {enemigo_actual.nombre} en tu camino ¡CUIDADO!")

        while enemigo_actual.salud > 0:
            accion = input("¿Qué deseas hacer? (atacar/huir): ").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"Has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} puntos de daño.")
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(f"El {enemigo_actual.nombre} te ha atacado y has recibido {dano_enemigo} de daño.")
                    jugador.recibir_dano(dano_enemigo)

                    if jugador.salud <= 0:
                        print("¡Oh no, has perdido :( ")
                        return  # Termina el juego

                else:
                    print(f"¡Has derrotado al {enemigo_actual.nombre}! 🎉")
                    enemigos_derrotados.append(enemigo_actual)
                    enemigos.remove(enemigo_actual)
                    jugador.ganar_experiencia(20)  # Solo gana experiencia si derrota al enemigo

            elif accion == "huir":
                print("¡Has escapado! 😨 Has perdido 10 puntos de experiencia por huir.")
                jugador.ganar_experiencia(-10)  # 🔥 Penaliza restando experiencia
                break  # Sale del combate

            else:
                print("¡Esa no es una acción válida! Intenta de nuevo.")

        continuar = input("¿Quieres seguir explorando? (s/n): ").lower()

        if continuar != "s":
            print("¡Gracias por haber explorado el espacio!")
            break

    if not enemigos:
        print("¡Felicidades, has derrotado a todos tus enemigos! 🏆")

if __name__ == "__main__":
    main()
