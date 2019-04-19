from math import*
from time import sleep
a = input("Choisissez un nombre pour ce programe vous dise\
          si il est pair ou impair")
a = int(a)

def PairImpair(a):
    sleep(0.5)
    print("Le nombre choisi est", a)
    
    if a%2 == 0:
        sleep(0.5)
        print("Le nombre", a, "est pair")
    else:
        sleep(0.5)
        print("Le nombre", a, "est impair")

PairImpair(a)
 
