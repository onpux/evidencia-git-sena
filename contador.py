def main():
    contador = 0
    print("Contador interactivo")
    print(f"Valor actual: {contador}")

    while True:
        opcion = input("Presiona Enter para incrementar o escribe 's' para salir: ")

        if opcion.lower() == "s":
            print("Fin del programa.")
            break

        contador += 1
        print(f"Valor actual: {contador}")


if __name__ == "__main__":
    main()
