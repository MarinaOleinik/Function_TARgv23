def summa3(arv1:float,arv2:float,arv3:float)->float:
    """Tagastab kolme arvu summa
        
    :param float arv1: Esimene arv
    :param float arv2: Teine arv
    :param float arv3: Kolmas arv
    :rtype: float

    """
    summa=arv1+arv2+arv3
    return summa
def arithmetic(a:float,b:float,t:str)->any:
    """Lihtne kalkulaator. 
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: arv
    :param float b: arv
    :param str t: atitmeetiline tehing
    :rtype: var Määramata tüüp(float or str)
    """
    if t in ["+","-","*","/"]:
        if b==0 and t=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a)+t+str(b))
    else:
        vastus="Tundmatu tehe"

    return vastus
def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine 
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus

    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v
def square(a:float)->any:
    """

    """
    S=a**2
    P=4*a
    d=(2)**(1/2)*a
    return S,P,d
def square_text(a:float)->str:
    """

    """
    S=a**2
    P=4*a
    d=(2)**(1/2)*a
    
    return "Pindala"+str(S)+",Ümbermõõt"+str(P)+",Läbimõõt"+str(d)
def season(param:int)->str:
    """

    """
    if 1<=param<=12:
        if param in [1,2,12]:
            v="talv"
        elif param>2 and param<6:
            v="kevad"
        elif 6<=param<=8:
            v="suvi"
        else:
            v="sügis"
    else:
        v="!!!!"
    return v
#5
def bank(a:float,years:int)->float:
    """

    """
    for i in range(years):
        a*=1.1
    return a
#6
from random import *
def is_prime(a=randint(0,1000))->bool:
    """
    """
    print(a)
    v=False
    for i in range(2,a):
        if a%i==0:
            v=True
    
    return v
#7
def date(päev:int,kuu:int,aasta:int)->bool:
    """
    """

    if päev in range(1,31) and kuu in [1,3,5,7,8,10,12]:
        v=True
    elif päev in range(1,29) and kuu==2 and is_year_leap(aasta):
        v=True
    elif päev in range(1,30) and kuu in [2,4,6,9,11]:
        v=True
    else:
        v=False
    return v
