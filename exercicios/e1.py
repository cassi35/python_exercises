def countNodes(head):
    print(head)



array_2d = [[1,4,3],[3,1,9],[0,5,2]]
total = 0
for d in array_2d:
    for i in d:
        total += (i * (total + total))
print(total)
# def search(arr,target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) / 2
#         if arr[mid] == target:
#             return mid 
#         elif target < arr[mid]:
#             right = mid - 1
#         else:
#             left = mid +1
# arrs = [-2,3,4,7,8,9,11,13]
# searchs = search(arrs,11)
# print(searchs)
def partition(arr,l,r):
    pivot = arr[r]
    i = l - 1
    for j in r - 1:
        if arr[j] < pivot:
            i+=1
            arr[i]
def qs(arr,l,r):
    if l >= r:
        return 
    p = partition(arr,l,r)
    qs(arr,l,p-1)
    qs(arr,l,p-1)
qs_arr = [3,-2,0,2,4,1]


def intersting():
    principal = int(input("\nenter principal: "))
    porcentagem = float(input("\n rate your intersting: "))
    year = int(input("\nhow many years?: "))
    formula = (((principal/100)*porcentagem)*year)+principal
    return formula
# print(intersting())

def taxCalculator():
    amount = int(input("\nwhat is order amount: "))
    state = str(input("\nwhat is your state?: "))
    tax = 0
    if state == "pa" or state == "sc" or state == "rs":
        tax = (amount /100) * 5.5 
    elif state is "rj" or state is "sp":
        tax = (amount / 100) * 6.0
    else:
        tax (amount / 100) * 3.0 
    print(tax)
    print(tax+amount)
    return 
# taxCalculator()
def temperate_convert(times):

    choice = str(input("please enter to c to convert from firanheit or \n  pess f to convert celcius to firenheit: "))
    if choice == "c":
        temperature = int(input("please enter the temperature in faranheit: "))
        celcuis = (temperature-32)*5/9
        return celcuis
    elif choice == "f":
        temperature = int(input("please enter the temperature in celcius: "))
        farenheit = (temperature * 9/5)+32
        return farenheit
    else:
        if times > 3:
            return "times above!!"
        times = times+1
        print("choice is undefined please do again")
        return temperate_convert(times)
# temperate_convert(1)
def bmi_calculator():
    print("\-- nbmi calculator ---")
    height = float(input("insert your height"))
    weight = int(input("insert your weight"))
    if weight > 400 and height > 2.30:
        print("weight is undefined and height is undefined")
        return bmi_calculator()
    elif weight > 400:
        print("weight is undefined ")
        return bmi_calculator()
    elif height > 2.30:
        print("height is undefined ")
        return bmi_calculator()
    else:
        imc = (weight/ (height * 2))
        if imc < 18:
            imc = str(imc)
            imc = imc[0:3]
            print("your goal is above "+imc) 
            family = input("do you want try your family?:")
            if family == "y":
                 family_imc()
        else:
            imc = str(imc)
            imc = imc[0:3]
            print("congrats you got the goal"+imc)
            family = input("do you want try your family?:")
            if family == "y":
                 family_imc()
def family_imc():
    members = int(input("how many membres?"))
    i = members
    peaple = []
    while i > 0:
        height = float(input("insert your height"))
        weight = int(input("insert your weight"))
        imc = (weight/ (height * 2))
        peaple.append(imc)
        i = i - 1
    for p in peaple:
        print(p)


# print(bmi_calculator())
# Guess the Number Game
import math,random
def amigos(times):
    if times == 5:
        print("\n jogo abacou")
        return 
    else:
        global jogadores 
        jogadores = int(input("quantos jogadores: "))
        if jogadores > 3:
            print("joagdores acima do limite")
            times = times +1 
            continuar = str(input("deseja continuar?: "))
            if continuar == "s":
                amigos(times)
            else:
                return 
        else:
            escolha = int("qual a escolha?: [1/2/3]")
            if escolha != 1 and escolha != 2 and escolha != 3:
                print("\n numeros invalidos")
                continuar = str(input("deseja continuar"))
                if continuar == "s":
                    times = times+1
                    return amigos(times)
                else:
                    return
                
            elif escolha == 1:
                pessoas = []
                computador = random.randint(0,10)
                i = 0
                while i < jogadores:
                    pessoa1 = int(input("insira um numero jogador entre [0/10]"))
                    if pessoa1 < computador:
                        p = str(i)
                        pessoas.append("jogador "+p+" perdeu")
                    else:
                        p = str(i)
                        pessoas.append("jogador "+p+" ganhou")
                    i = i +1
                for i in range(0,pessoas):
                    print(pessoas[i])
                continuar = str(input("deseja continuar?: "))
                if continuar == "s":
                    times = times +1 
                    return amigos(times)
                else:
                    return                
                
            elif escolha == 2:
                pessoas = []
                computador = random.randint(0,100)
                i = 0
                while i < jogadores:
                    pessoa1 = int(input("insira um numero jogador entre [0/100]"))
                    if pessoa1 < computador:
                        p = str(i)
                        pessoas.append("jogador "+p+" perdeu")
                    else:
                        p = str(i)
                        pessoas.append("jogador "+p+" ganhou")
                    i = i +1
                for i in range(0,pessoas):
                    print(pessoas[i])
                continuar = str(input("deseja continuar?: "))
                if continuar == "s":
                    times = times +1 
                    return amigos(times)
                else:
                    return 
            else:
                pessoas = []
                computador = random.randint(0,1000)
                i = 0
                while i < jogadores:
                    pessoa1 = int(input("insira um numero jogador entre [0/1000]"))
                    if pessoa1 < computador:
                        p = str(i)
                        pessoas.append("jogador "+p+" perdeu")
                    else:
                        p = str(i)
                        pessoas.append("jogador "+p+" ganhou")
                    i = i +1
                for i in range(0,pessoas):
                    print(pessoas[i])
                continuar = str(input("deseja continuar?: "))
                if continuar == "s":
                    times = times +1 
                    return amigos(times)
                else:
                    return      
def guess(times):
    if times == 1:
        print("jogo acabou")
        continuar = str(input("quer jogar com os amigos? "))
        if continuar == "s":
            return amigos(0)
        else:
            return 
    else:
        jogadas = int(input("jogue um numero: "))
        if jogadas != 1 and jogadas != 2 and jogadas != 3:
            print("numeros errados jogue novamente")
            times = times + 1
            return   guess(times)
        elif jogadas == 1:
            times = times+1
            computador = random.randint(0,10)
            first = int(input("\njogue uma vez entre 0 e 10: "))
            if computador > first:
                print("\n jogada errada perdeu!!")
                continuar = str(input("\ndeseja continuar? "))
                if continuar == "s":
                    amigos1 = str("quer jogar com os amigos?: ")
                    if amigos1 == "s":
                        times = times+1
                        return amigos(times)
                    return guess(times)
                else:
                    
                    return "acabou"
            else:
                print("parabens ganhou!!")
                continuar = str(input("\ndeseja continuar? "))
                if continuar == "s":
                    amigos1 = str("quer jogar com os amigos?: ")
                    if amigos1 == "s":
                        times = times+1
                        return amigos(times)
                    return guess(times)
                else:
                    return "acabou"
        elif jogadas == 2:
            times = times+1
            computador = random.randint(0,100)
            first = int(input("\njogue uma vez entre 0 e 100: "))
            if computador > first:
                print("\n jogada errada perdeu!!")
                continuar = str(input("\ndeseja continuar? "))
                if continuar == "s":
                    amigos1 = str("quer jogar com os amigos?: ")
                    if amigos1 == "s":
                        times = times+1
                        return amigos(times)
                    return guess(times)
                else:
                    return "acabou"
            else:
                print("parabens ganhou!!")
                continuar = str(input("\ndeseja continuar? "))
                if continuar == "s":
                    amigos1 = str("quer jogar com os amigos?: ")
                    if amigos1 == "s":
                        times = times+1
                        return amigos(times)
                    return guess(times)
                else:
                    return "acabou"
        else:
            times = times+1
            computador = random.randint(0,1000)
            first = int(input("\njogue uma vez entre 0 e 1000: "))
            if computador > first:
                print("\n jogada errada perdeu!!")
                continuar = str(input("\ndeseja continuar? "))
                if continuar == "s":
                    amigos1 = str("quer jogar com os amigos?: ")
                    if amigos1 == "s":
                        times = times+1
                        return amigos(times)
                    return guess(times)
                else:
                    return "acabou"
            else:
                print("parabens ganhou!!")
                continuar = str(input("\ndeseja continuar? "))
                if continuar == "s":
                    amigos1 = str("quer jogar com os amigos?: ")
                    if amigos1 == "s":
                        times = times+1
                        return amigos(times)
                    return guess(times)
                else:
                    return "acabou"

# guess(0)
# ok tenho exefcios gracas a deus