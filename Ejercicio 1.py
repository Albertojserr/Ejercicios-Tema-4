def estado(temperatura):
    if(temperatura<0):
        print("A esta temperatura es hielo")
    elif(temperatura>=0 and temperatura<100):
        print("A esta temperatura es agua")
    else:
        print("A esta temperatura es vapor")