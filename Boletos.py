#Sara Delgado González
#Calcula es precio total de boletos dependiendo el numero y el lugar


def calcularPago(asientosA, asientosB, asientosC):
    precioA=asientosA*3250
    precioB=asientosB*1730
    precioC=asientosC*850
    totalPago= precioA +precioB +precioC
    return totalPago



def main() :
     numeroBoletosA = int(input("Leer el número de asientos de clase A: "))
     numeroBoletosB = int(input("Leer el número de asientos de clase B: "))
     numeroBoletosC = int(input("Leer el número de asientos de clase C: "))
     total = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
     print("El costo total es : $ %d.00" % total)

main()