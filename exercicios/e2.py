def calculadora():
    primeiro = int(input("qual o primeiro numero"))
    segundo = int(input("qual o seugundo numero"))
    operacao =str(input("qual a operacao"))
    if operacao == '+':
        print(primeiro+segundo)
    elif operacao == '-':
        print(primeiro-segundo)
    elif operacao == '/':
        print(primeiro/segundo)
    elif operacao == '*':
        print(primeiro*segundo)
    else:
        print("undefined")
        
def carterWaiter():
    receitasEscolhidas = receitas()
    aperitivo = aperitivos()
    ingredientes = []
    compradorVegetariano = []
    for receita in receitasEscolhidas:
        if receita['restricao'] == 'vegetariano':
            compradorVegetariano.append(receita['ingredientes'])

    for ingrediente in receitasEscolhidas:
        ingredientes.append(ingrediente['engredientes'])
    
def receitas():
    receitasCompleta = []
    while(True):
        receita1 = []
        nome = str(input("insira o nome da receita: "))
        tipo = int(input("insira um tipo do prato:\n[1/2/3]\n 1:normal\n2:vegano\n:3vegetariano: "))
        retricao = str(input("insira a restricao:\n qual restricao:\n [gloten/lactose/amendoim/frutos do mar]: "))
        while(True):
            ingrediente = str(input("insira um ingrediente: "))
            receita1.append(ingrediente)
            prefere = str(input("deseja continuar?:[s/n]: "))
            if prefere != "s":
                break
        receita =   {'receitaNome':nome,'ingredientes':receita1,'tipos':tipo,'restricao':retricao}
        receitasCompleta.append(receita)
        prefere = str(input("quer addicionar mais receitas?[s/n]: "))
        if prefere != "s":
            break
        else:
            continue
    return receitasCompleta
def aperitivos():
    # while aperitivo
    lista = ["maca","banana","abacate"]
    return lista
def colossal():
    pass

class FilaNormal:
    def __init__(self,capacidade):
        self.fila = []
        self.capacidade = capacidade

    def queue(self,pessoa):
        if self.capacidade == len(self.fila):
            return None
        else:
            self.fila.append(pessoa)
    def enqueue(self):
        self.fila.pop(0)
    def peek(self):
        return print(self.fila[0])
class PrioridadeFila:
    def __init__(self):
        self.filaPrioridade = []
# https://github.com/exercism/python/blob/main/exercises/concept/chaitanas-colossal-coaster/.docs/instructions.md

# class codigo:
#     def __init__(self):
#         self.colecao = []
#         self.tamanho = 1
#     def adcionar(self):
#         self.colecao.append(self.tamanho)
#         self.tamanho = self.tamanho + 1
#     def verificacao(self,nome,sobrenome,id):
#         if len(nome) < 2 and len(sobrenome) < 2 or type(nome) != 'str' or type(sobrenome) != 'str':
#             return False 
#         for i in range(0,len(self.colecao)):
#             if i is id:
#                 return True
#         return False
# pessoas = codigo
# pessoas.adcionar()
# pessoas.adcionar()
# pessoas.adcionar()
# print(pessoas.verificacao('cassiano','sobral',2))            

#making-the-grade
import math
def round_scores(student_scores,studant_names):
    notas = []
    for nota in student_scores:
        notas.append(round(nota))
    fail = count_failed_students(notas)
    above = above_threshold(notas,75)
    hight = above[0]
    for best in above:
        if hight < best:
            hight = best
    studant_ranking(studant_names,above)
    perfect_grades()
def count_failed_students(notas):
    sum = 0
    for nota in notas:
        if nota < 40:
            sum = sum + 1 
    return sum 
def above_threshold(list,threshold):
    above = []
    for student in list:
        if student > threshold:
            above.append(student)
    return above
def perfect_grades():
    pass
def studant_ranking(studantNames,studantScore):
    notas = []
    for i in range(0,len(studantScore)):
        notas.append([studantNames[i],studantScore[i]])
    return notas

 
studantsNames =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
studentScores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
round_scores(studentScores,studantsNames)
# //Mecha Munch
class Node:
    def __init__(self,data = None,next = None):
        self.data = data 
        self.next = next
class mechaMunch:
    def __init__(self):
        self.products = None
        self.stock = []
    def add(self,item):
        new_product = Node(item)
        new_product.next = self.products
        self.products = new_product
        self.send_to_stock(item)
    def length(self):
        temp = self.products
        if temp.data == None:
            return False
        else:
            count = 0
            temp = self.products
            while temp:
                count+=1
                temp.next
            return count
    def remove(self,index):
        temp = self.products
        if (temp is not None):
            if (temp.data == index):
                self.products = temp.next
                temp = None
                return
        while (temp is not None):
            if (temp.data == index):
                break
            prev = temp
            temp = temp.next
        if temp == None:
            print(False)
            return 
        prev.next = temp.next
        temp = None
    def print_products(self):
        temp = self.products
        while(temp):
            print(temp.data)
            temp = temp.next
    def send_to_stock(self,item):
        self.stock.append(item)
product = mechaMunch()
product.add('banana')
product.add('maca')
product.add('alface')
product.add('uva')
product.remove(1)


# //ellens-alien-game

            
class Alien:
    def __init__(self):
        self.x_cordinate = None
        self.y_cordinate = None
        self.total_aliens_create = []
        self.health = 3
        self.total = 0
        
    def hit(self):
        self.health-=1
        return
    def is_alive(self):
        if self.health == 0:
            return True
        else:
            return False
    def teleport(self,x,y):
        self.x_cordinate = x
        self.y_cordinate = y 
    def create_alien(self,x,y):
        alien_pass = Alien()
        alien_pass.x_cordinate = x
        alien_pass.y_cordinate = y
        self.total_aliens_create.append(alien_pass)
        self.total = self.total+1
    def list_alients(self):
        for alien in self.total_aliens_create:
            print(alien.y_cordinate)
            print(alien.x_cordinate)
            print()

    def collison_detection(self,other_object):
        for alien_colid in self.total_aliens_create:
            if alien_colid.x_cordinate == other_object.x_cordinate or alien_colid.y_cordinate == other_object.y_cordinate:
                return True
        return False
# alien1 = Alien()
# alien1.create_alien(1,2)
# alien1.create_alien(2,3)
# alien2 = Alien()
# alien2.x_cordinate = 2
# alien2.y_cordinate = 2
# print(alien1.collison_detection(alien2))
# alien1.list_alients()

# ghost-gobble-arcade-game
import math,random
class Pacman:
    def __init__(self):
        self.jogo = []
        self.column = 0
        self.pos = 0
        self.eat = 0

    def create_game(self):
        for i in range(0,5):
            self.jogo.append([])
            for y in range(0,5):
                self.jogo[i].append('.')

        for i in range(0,len(self.jogo)):
            import random 
            p = random.randint(0,4)
            self.jogo[i][p] = '**'
        self.jogo[0][0] = 'pac'
    def entrada(self):
        for road in self.jogo:
            print(road)
        column = int(input("left || right: [0 : 5]->"))
        pos = int(input(" top || down [0 : 5]->"))
        if (column < 0 or column > 5) or (pos < 0 or pos > 5):
            return self.entrada()
        else:

            self.jogo[self.column][self.pos] = '.'
            if column != 0 and pos != 0:
                self.column = column -1 
                self.pos = pos -1
            elif column == 0 and pos != 0:
                self.pos = pos -1
            elif column != 0 and pos == 0:
                self.column = column -1
            else:
                self.column = column
                self.pos = pos
            if self.jogo[self.column][self.pos] == '**':
                self.jogo[self.column][self.pos] = '[pac--> died]'
                for p in self.jogo:
                    print(p)
                print('game over...')
                return 
            self.jogo[self.column][self.pos] = 'pac'
            if self.column != column and self.pos != pos:
                self.eat = self.eat + self.pos + self.column
            for c in self.jogo:
                print(c)
            print(self.eat)
            continues = str(input("continue?... "))
            if continues == 'y':
                return self.entrada()
            else:
                    print("exit")
                    return            
# pac = Pacman()
# pac.create_game()
# pac.entrada()

# little sister -eassy
def caotalize_title():
    tittle = str(input("insira o titulo: "))
    tittle = tittle.capitalize()
    sentense = str(input("insira frase: "))
    res = ckeck_sentence(sentense)
    if res:
        all = "\n {t} \n {s}".format(t = tittle , s = sentense)
        print(all)
        return
    else:
        print('oal')
        return 
def ckeck_sentence(sentense):
    import re 
    init = re.findall("^i|^he|^she|^it|^they|^we",sentense)
    i = lambda phase : len(phase) != 0
    initPhase = i(init)
    pontuation = len(re.findall("[s][h][e][,]|[i][,]|[h][e][,]|[t][h][e][y][,]|[w][e][,]|[i][t][,]",sentense)) == 0
    end = len(re.findall(".$|!$",sentense)) != 0
    if initPhase and end and pontuation:
        return True
    else:
        return False
# caotalize_title()

# plane tickets 
# class FilaA:
#     def __init__(self,row):
#         self.next = None
#         self.sit = row

# class Plane:
#     def __init__(self):
#         self.row = []
#         self.fila = ['a','b','c','d']
#         self.ponteiro = 0 
#         self.max = None
#     def seat(self,r,fileira):
#         for i in range(0,r):
#             self.row.append([])
#             for f in self.fila:
#                 obj = {f:None}
#                 complete = FilaA(0)
#                 for c in range(1,fileira):
#                     new = FilaA(c)
#                     complete.next = new 
#                 obj[f] = complete
#                 self.row[i].append(obj)
#         print(self.row[0][0]['a'])
# air = Plane()
# air.seat(4,4)


#election day     

def election():
    import math,random
    polly = 0
    ernest = 0
    states = 0
    while states < 26:
        population1 = random.randint(0,100)
        population2 = random.randint(0,100)
        ernest = ernest + population1
        polly = polly + population2
        states+=1
    if(ernest > polly):
        return 'new president ernest with {ernests}'.format(ernests = ernest)
    elif ernest == polly:
        new_election = election()
        return new_election
    else:
        return 'new president polly with {p}'.format(p = polly)
# print(election())

# max and min val

def tempeture():
    temp = []
    import random
    for i in range(0,24):
        new_tempeture = random.randint(-2,30)
        temp.append(new_tempeture)
    max_temp = temp[0] 
    min_temp = temp[0]
    for actual in temp:
        if actual > max_temp:
            max_temp = actual
        if min_temp > actual:
            min_temp = actual
    print(max_temp)
    print(min_temp)
    return
# tempeture()
# Counting Characters
def blanc_character():
    phase = str(input("digite uma frase"))
    count_blank = phase.count(" ")
    return count_blank
class coin:
    def __init__(self):
        self.cara = 0
        self.coroa = 0
    def lancamento(self):
        par = 1
        impar = 0
        rodada = 0
        while rodada < 100:
            import random
            temp = random.randint(0,1)
            if par == temp:
                self.cara+=1
            else:
                self.coroa+=1
    def get_face(self):
        print(self.coroa)
        print(self.cara)
def color():
    cores = ['azul','vermelho','roxo','rosa']
    desenhos = int(input('quantos desenhos'))
    c = 0
    palheta = []
    while c < desenhos:
        temp_palheta = []
        import random
        p = 0
        seta = 0 
        while p < len(cores):
            seta_escolhida = random.randint(-1,1)
            seta+=seta_escolhida
            temp_palheta.append(cores[seta])  
            p+=1
        palheta.append(temp_palheta) 

        c+=1 
    for palhetas in palheta:
        print(palhetas)
# color()

# locomotive -engenieer
def locomotive():
    listId = []
    for i in range(0,3):
        listId.append(listsIds())
    listId[0] = listId[0].reverse()
    move_final = [listId.pop(),listId.pop()]
    new_list = []
    for i in range(0,len(listId)):
        while True:
            import random
            new_list.append(listId[i].pop())
            if len(listId[i]) != 0:
                continue
            else:
                break
    new_list.append(move_final)
    return new_list


def listsIds():
    listId = []
    while True:
        tempId = int(input("id vagao: "))
        listId.append(tempId)
        add = int(input("continue==[1/2]:"))
        if add == 1:
            break
    return listId
# locomotive()

# Imaginary Coding Interview
import datetime
print(datetime.datetime.now().minute)
# meldown miltigation 
class reator:
    def __init__(self):
        self.isCritical = None
        self.eficient = None
        
    def is_criticality_balanced(self,temperature,neutrons_emitted,netronus_next_generation):
        kff_formula = neutrons_emitted / netronus_next_generation
        if kff_formula is 1:
            self.isCritical = 1
            return 'critically situation'
        elif kff_formula > 1:
            self.isCritical = 2
            return 'super critically situation'
        else:
            self.isCritical = 0
            return 'subcritical situation'
    def reactor_eficiency(self,theorical_max_power,voltage,current):
        generate_power = voltage * current
        percent = (generate_power/theorical_max_power)/100 
        if percent > 80:
            self.eficient = 'green'
            return 'green'
        elif percent < 80 and percent > 60:
            self.eficient = 'orange'
            return 'orange'
        elif percent < 60 and percent >= 30:
            self.eficient = 'red'
            return 'red'

        elif percent < 30:
            self.eficient = '30'
            return 'black'
    def fail_safe(self,temperature,netrons_produced_per_second,thereshold):
        if((temperature * netrons_produced_per_second) < ((thereshold/100)*90)):
            return 'low'
        elif((temperature*netrons_produced_per_second)< ((thereshold /100)*10)):
            return 'normal'
        else:
            return 'danger'
    def control_temerature(self):
        pass 
    def monitoration_contro(self):
        pass 
    def controle_potation_termic(self):
        pass 
    def integraty_pressure(self):
        pass 
    def verification_tax(self):
        pass 
    def protection_fail(self):
        pass 
    def alrm_action(self):
        pass 
    def radiation(self):
        pass 
    def analystic_data(self):
        pass
    def manutensao_programada(self):
        pass 
# restaurant-rozalynn
class restaurant:
    def __init__(self,reservation):
        self.reservation = reservation 
        self.peaple = set()
    def new_seating_chart(self,guests):
        if(self.reservation < len(self.peaple)):
            return None
        else:
            for i in guests:
                self.peaple.add(i)
            return self.peaple
    def clears(self):
        return self.peaple.clear()
    def update(self,new_peaple):
        if len(self.peaple) == 0:
            return None
        else:
            update = set()
            for peaple in new_peaple:
                update.add(peaple)
            return self.peaple.update(update)
    
    
    

import sys,re,operator,string,inspect
# print(string.whitespace)

# print(string.octdigits)
# //Model the game
def jogobaralho():
    import math,random 
    global sam 
    global dealer  
    for i in range(0,2):
        
        nome = str(input("qual seu nome: "))
        embaralhamento1 = random.randint(1,11)
        embaralhamento2 = random.randint(1,11)
        if nome == 'sam':
            res = embaralhamento1+embaralhamento2
            sam = res 
        elif nome == 'dealer':
            res = embaralhamento1+embaralhamento2
            dealer = res 
        else:
            print("Err:undefined try again")
            return jogobaralho()
    if sam < 21 and dealer < 21:
        compra_sam = sam 
        compra_dealer = dealer
        while compra_sam <= 21 or compra_dealer <= 21:
            compra_sam = compra_sam + random.randint(1,11)
            compra_dealer = compra_dealer+random.randint(1,11)
        if compra_sam > compra_dealer:
            print('sam win with {carta}'.format(carta = sam))
            return
        elif compra_sam == 21 and compra_dealer == 21:
            print('empate')
            return
        elif compra_sam == 21:
            print('sam win'.format(carta = sam))
            return
        elif compra_dealer > compra_sam:
            print('dealer win with {carta}'.format(carta = dealer))
            return
        elif compra_dealer == 21:
            print('dealer win with {carta}'.format(carta = dealer))
            return
    elif sam == 21 and dealer == 21:
        print('empate')
        return
    elif sam > 21 and dealer < 21:
        print('dealer win with {carta}'.format(carta = dealer))
        return
    elif dealer > 21 and sam < 21:
        print('sam win with {carta}'.format(carta = sam))
        return
    
# jogobaralho()
# Connect4
def jogodavelha():
    display = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ]
    grid = 0
    while True:
        if grid == 0:
            exibir = ''
            for i in range(0,len(display)):
                for x in range(0,len(display[i])):
                    temp = f'{display[i][x]}'
                    exibir+=temp 
                exibir+=f'{i}'
                exibir+='\n'
            print(f'012')
            print(exibir)
            grid = 1
        teste = True
        global col1,col2,linha1,linha2
        while teste:
            teste = False
            col1 = int((input('jogue [x] col:num ')))
            linha1 = int((input('jogue [x] linha:num: ')))
            print('\n')
            exibir = ''
            col2 = int(input('jogue [o] col:num: '))
            linha2 = int(input('jogue [o] linha:num: '))
            if col1 == col2 and linha2 == linha1:
                teste = True
            elif col1 > 2 and col2 > 2:
                teste = True
            elif linha1 > 2 and linha2 > 2:
                teste = True
            else:
                break
        for i in range(0,len(display)):
            for x in range(0,len(display[i])):
                if (linha1 == x and col1 == i):
                    if display[i][x] == '.':
                        display[i][x] = 'x'
                if (linha2 == x and col2 == i):
                    if display[i][x] == '.':
                        display[i][x] = 'o'
        exibir = ''
        for i in range(0,len(display)):
            for x in range(0,len(display[i])):
                temp = f'{display[i][x]}'
                exibir+=temp 
            exibir+=f'{i}'
            exibir+='\n'
        print(f'012')
        print(exibir)
        verificar = 0
        for i in range(0,len(display)):
            for x in range(0,len(display[i])):
                if display[i][x] != '.':
                    verificar+=1
        if verificar == 9:
            break
        
        for i in range(0,len(display)):
            if display[i][0] == 'x' and display[i][1] == 'x' and display[i][2] == 'x':
                print('jogador 1 ganhou')
                return
            elif display[i][0] == 'o' and display[i][1] == 'o' and display[i][2] == 'o':
                print('jogador 2 ganhou')
                return
            if display[0][i] == 'x' and display[1][i] == 'x' and display[2][i] == 'x':
                print('jogador 1 ganhou')
                return
            elif display[0][i] == 'o' and display[1][i] == 'o' and display[2][i] == 'o':
                print('jogador 2 ganhou')
                return 
            if display[0][0] == 'x' and display[1][1] == 'x' and display[2][2] == 'x':
                print('jogador 1 ganhou')
                return
            elif display[0][0] == 'o' and display[1][1] == 'o' and display[2][2] == 'o':
                print('jogador 2 ganhou')
                return
    print('ninguem ganho')
        
# jogodavelha()
# virtual machine fruit
def virtual_machine_fruit(credit):
    def credits(c):
        if c >= 100:
            return 0
        else:
            return c
    import random
    money_machine = 100
    slots = ['black','white','green','yellow']
    money = int(input(f'put a money[10,100]: credit=={credit}: '))
    money  = money + credit
    if money < 10 or money > 200:
        print('wrong\n')
        return virtual_machine_fruit(credits(credit))
    machine_choose = []
    for i in range(0,len(slots)):
        temp_choose = slots[random.randint(0,len(slots)-1)]
        machine_choose.append(temp_choose)
    correct = [0,0,0,0]
    for i in range(0, len(slots)-1):
        for x in range(0,len(machine_choose)-1):
            if slots[i] == machine_choose[x]:
                correct[i] = correct[i]+1
    for i in range(0,len(correct)):
        for x in range(0,len(correct)):
            if correct[x] >= 2:
                to_pay = money * 2 
                print(f' here {to_pay}\n')
                stay = int(input('[1]again [2] out:-->'))
                if to_pay > money_machine:
                    print(f'credit {to_pay}')
                if stay == 1:
                    c = to_pay -money_machine
                    return virtual_machine_fruit(credits(c))
                else:
                    print('out...')
                    return
        diferente = True
        for a in range(0,len(correct)):
            if correct[a] != 1:
                diferente = False
        if diferente == False:
            to_pay = money*5
            print(f'you win ${to_pay} {correct} {machine_choose} \n')
            if money_machine < to_pay:
                print(f'credit ${to_pay}\n')
            stay = int(input('[1]again [2] out:-->'))
            if stay == 1:
                c = to_pay -money_machine
                return virtual_machine_fruit(credits(c))
            else:
                print('out...')
                return
            
            
# virtual_machine_fruit(0)
# //Word Game (Scrabble)
def word_game():
    word = str(input('enter word: '))
    points = {
        1:['e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u'],
        2:['d','g'],
        3:['b','c','m','p'],
        4:['f','h','v','w','y'],
        5:['k'],
        8:['j','x'],
        10:['q','z']
    }
    sum = 0
    for point in points:
        for i in points[point]:
            for a in word:
                if i == a:
                    sum+=point
    return print(sum)

# word_game()
# Snack shack
class Node:
    def __init__(self,value,time):
        self.next = None
        self.value = value
        self.time = time
class LinkedList:
    def __init__(self):
        self.head = None
        self.actual_time = 0
        self.temp_tempo = None
        self.potato = None
    def insertStart(self,value):
        if self.head == None:
            self.head = Node(value,self.actual_time)
            minuto = int(1.30)
            segundo = ((1.30 - minuto)*100)
            tempo_em_minuto = minuto+(segundo/60)
            self.actual_time = tempo_em_minuto
            return
        else:
            temp = self.head 
            while(temp.next):
                temp = temp.next
            new_node = Node(value,self.actual_time) 

            minuto = int(1.30)
            segundo = ((1.30 - minuto)*100)
            self.temp_tempo =minuto+(segundo/60)
            self.actual_time+=self.temp_tempo
            temp.next = new_node
            return
    def insertPotato(self):
            if self.head != None:
                temp = self.head
                while(temp.next):
                    temp = temp.next
                value = temp.value+1
                new_potato = Node(value,self.actual_time)
                minuto = int(1.30)
                segundo = ((1.30 - minuto)*100)
                self.potato = minuto+(segundo/60)
                self.actual_time = self.potato+self.potato
                temp.next = new_potato
                return
            else:
                return None 

    def remove(self):
        if self.head == None:
            return None 
        else:
            new_head = self.head.next
            self.head = new_head
            self.actual_time-=self.temp_tempo
            return
class Queue:
    def __init__(self):
        self.queue = LinkedList()
    def enqueue(self,value):
        return self.queue.insertStart(value)
    def dequeue(self):
        return self.queue.remove()
    def insert_potato(self):
        return self.queue.insertPotato()
    def print(self):
        if self.queue.head != None:
            temp = self.queue.head
            while(temp):
                print(temp.value,temp.time)
                temp = temp.next
        else:
            return None

class Snack:
    def __init__(self):
        self.list = Queue()
    def add(self,value):
        value+=1
        for i in range(1,value):
            self.list.enqueue(i)
    def remove_peaple(self):
        self.list.dequeue()
        self.print_peaple()
        return self.print_peaple()
    def print_peaple(self):
        return self.list.print()
# mac = Snack()
# mac.add(6)
# mac.print_peaple()