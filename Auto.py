#Sara Delgado González
#Calcula el rendimiento de un auto a partir de cierta cantidad de gasolina


def calcularRendimiento(km, litros):
    r = km / litros
    return r


def calcularConversion(km, litros):
    millas = km / 1.6093
    galones = litros * 0.264
    rendimiento = millas / galones
    return rendimiento

def calcularLitros(km, r):
    litros = km / r
    return litros
def main():
    kmRecorridos = float(input("Número de km recorridos: "))
    gasolinaUsada = float(input("Número de litros de gasolina usados: "))
    print("")
    r = round(calcularRendimiento(kmRecorridos, gasolinaUsada), 2)
    r2 = round(calcularConversion(kmRecorridos, gasolinaUsada), 2)
    print("Si recorres 350 kms con 23 litros de gasolina, el rendimiento es:")
    print(r, "km/l")
    print(r2, "mi/gal")
    print("")
    km = float(input("¿Cuántos kilómetros vas a recorrer? "))
    litros = calcularLitros(km, r)
    print("")
    print("Para recorrer", km ,"km. necesitas", round(litros, 2), "litros de gasolina")


main()