from random import randint


def pedir_numero():
    """Lee un entero entre 1 y 100 sin gastar intentos inválidos."""
    while True:
        try:
            numero = int(input("Número del 1 al 100: "))
        except ValueError:
            print("Escribe un número entero.")
            continue

        if 1 <= numero <= 100:
            return numero

        print("El número debe estar entre 1 y 100.")


def jugar(secreto):
    """Juega hasta acertar o agotar diez intentos."""
    intentos = 0

    while intentos < 10:
        numero = pedir_numero()
        intentos += 1

        if numero == secreto:
            print(f"Has ganado. Intentos: {intentos}.")
            return True

        if numero < secreto:
            print("El número buscado es mayor.")
        else:
            print("El número buscado es menor.")

    print(f"Has perdido tras {intentos} intentos. Era {secreto}.")
    return False


def repetir():
    """Pregunta si se quiere jugar otra partida."""
    while True:
        respuesta = input("¿Otra partida? (s/n): ").strip().lower()
        if respuesta in ("s", "n"):
            return respuesta == "s"

        print("Responde s o n.")


def main():
    """Sortea un número por partida y lleva el marcador."""
    jugadas = 0
    ganadas = 0

    while True:
        jugadas += 1

        if jugar(randint(1, 100)):
            ganadas += 1

        print(f"Jugadas: {jugadas}. Ganadas: {ganadas}.")

        if not repetir():
            break


if __name__ == "__main__":
    main()