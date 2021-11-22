
def EsBisiesto(Año):
    Bisiesto=False
    if(Año%4==0):
        if(Año%100==0):
            if(Año%400==0):
                Bisiesto=True
        else:
            Bisiesto=True
    return Bisiesto

def queDiaEs(Día, Mes, Año):
    numero=Año%100
    numero+=int(numero/4)
    numero+=Día
    if(Mes==1):
        numero+=1
        if(EsBisiesto(Año)==True):
            numero-=1
    elif(Mes==2):
        numero+=4
        if(EsBisiesto(Año)==True):
            numero-=1
    elif(Mes==3):
        numero+=4
    elif(Mes==5):
        numero+=2
    elif(Mes==6):
        numero+=5
    elif(Mes==8):
        numero+=3
    elif(Mes==9):
        numero+=6
    elif(Mes==10):
        numero+=1
    elif(Mes==11):
        numero+=4
    elif(Mes==12):
        numero+=6
    Centenas=int(Año/100)
    if(Centenas==16 or Centenas==20):
        numero+=6
    elif(Centenas==17 or Centenas==21):
        numero+=4
    elif(Centenas==18):
        numero+=2
    modulo=numero%7
    Hoy=""
    if(modulo==1):
        Hoy="Domingo"
    elif(modulo==2):
        Hoy="Lunes"
    elif(modulo==3):
        Hoy="Martes"
    elif(modulo==4):
        Hoy="Miércoles"
    elif(modulo==5):
        Hoy="Jueves"
    elif(modulo==6):
        Hoy="Viernes"
    else:
        Hoy="Sábado"
    return Hoy

