def main():
    # Declara una lista de cadenas
    aves = ["Loro gris", "Paloma de diamante", "Cóctel"]
    
    print("Los valores de la lista antes de insertar:")
    # Itera sobre la lista para imprimir los valores
    for ave in aves:
        print(ave, end=" ")
    print()
    
    # Agrega tres valores al final de la lista utilizando append()
    aves.extend(["Mayna", "Periquitos", "Cacatúa"])
    
    print("Los valores de la lista después de insertar:")
    # Itera sobre la lista para imprimir los valores
    for ave in aves:
        print(ave, end=" ")
    print()

# Llama a la función main para ejecutar el código
if __name__ == "__main__":
    main()