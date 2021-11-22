def categoria(edad):
    if(edad<6):
        print("No tiene edad para entrar en ninguna categoría")
    elif(edad>=6 and edad<=7):
        print("Benjamín")
    elif (edad>=8 and edad<=9):
        print("Alevín")
    elif (edad>=10 and edad<=11):
        print("Infantil")
    else:
        print("Cadete")