#Sara Delgado González
#Calcula el pago total despues de horas extras

def calcularpagoNormal(horasN, pago):
    pagoNormal = horasN * pago
    return pagoNormal

def calcularpagoExtra(HorasE, pago):
    pagoExtra = HorasE * (pago * 1.85)
    return pagoExtra

def calcularpagototal(pagoN, pagoE):
    pagoTotal = pagoN+pagoE
    return pagoTotal

def main():
   horasN = float(input("Número de horas normales trabajadas: "))
   horasEx = float(input("Número de horas extras trabajadas: "))
   pago = float(input("Pago por hora: "))
   pagoNormal = calcularpagoNormal(horasN,pago)
   pagoExtra = calcularpagoExtra(horasEx,pago)
   pagoTotal = calcularpagototal(pagoNormal,pagoExtra)
   print("")
   print("Pago normal: $%.2f" %(pagoNormal))
   print("Pago extra: $%.2f" %(pagoExtra))
   print("-----------------------")
   print("Pago total: $%.2f" %(pagoTotal))
main()