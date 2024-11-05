# Cube Conundrum
def cube_conundrown(num):
    if num == 2:
        print('exit')
        return
    red = int(input('red numbers: '))
    green = int(input('green numbers: '))
    blue = int(input('green numbers: '))
    if(red > 12 or blue > 14 or green > 13):
        print('game over')
        num+=1
        return cube_conundrown(num)
    else:
        print('game win')
        num+=1
        return cube_conundrown(num)

def parse_diagram(diagram):
    # Convert the string diagram into a list of lists (2D array)
    return [list(row) for row in diagram.strip().split('\n')]

def is_symbol(char):
    # Define what characters are considered symbols
    return char not in '0123456789.'

def get_adjacent_numbers(diagram, row, col):
    # Define directions for all 8 adjacent positions (including diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    numbers = []
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(diagram) and 0 <= c < len(diagram[0]):
            if diagram[r][c].isdigit():
                numbers.append(int(diagram[r][c]))
    return numbers

def sum_part_numbers(diagram):
    part_numbers_sum = 0
    for row in range(len(diagram)):
        for col in range(len(diagram[0])):
            if is_symbol(diagram[row][col]):
                part_numbers_sum += sum(get_adjacent_numbers(diagram, row, col))
    return part_numbers_sum

# Example engine schematic
schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# Process the schematic and compute the sum of part numbers
parsed_diagram = parse_diagram(schematic)
total_sum = sum_part_numbers(parsed_diagram)
# print(f"Total sum of part numbers: {total_sum}")
# Scratchcards
def scratchcards(card):
    global win 
    win = []
    global right 
    right = []
    c = 0
    global pipe 
    pipe = False
    while c < len(card):
        if card[c-1] == '|':
            pipe = True
        if pipe:
            right.append(card[c])
        else:
            win.append(card[c])
        c+=1
    soma = 0
    for i in range(0, len(right)):
        for x in range(0,len(win)):
            if right[i] == win[x]:
                soma+=right[i]
    return soma 
# print(scratchcards([1,2,3,'|',1,2,3,4]))
# corrida de barco
def corrida(lista_corrida):
    total_maneiras = 1  # Total de maneiras para todas as corridas
    for corrida in lista_corrida:
        tempo_total = corrida[0]  # Tempo total da corrida
        recorde = corrida[1]  # Distância recorde
        maneiras = 0  # Contador de maneiras para esta corrida

        # Verificar diferentes tempos de pressão do botão
        for tempo_pressionado in range(tempo_total + 1):
            # Velocidade alcançada
            velocidade = tempo_pressionado
            # Tempo restante após soltar o botão
            tempo_restante = tempo_total - tempo_pressionado
            
            # Cálculo da distância total percorrida
            if tempo_restante >= 0:  # Garantindo que o tempo restante não seja negativo
                distancia = velocidade * tempo_restante + (velocidade * (velocidade + 1)) // 2
                # Verifica se a distância é maior que o recorde
                if distancia > recorde:
                    maneiras += 1
        
        total_maneiras *= maneiras  # Multiplica as maneiras da corrida atual ao total

    return total_maneiras

# Testando com os dados fornecidos
# print(corrida([[7, 9], [15, 40], [30, 200]]))

import string

def emOrdem(alfabeto, i):


    if i >= len(alfabeto):
        return

    # Visit left subtree
    emOrdem(alfabeto, 2 * i + 1)

    # Visit root
    print(alfabeto[i])

    # Visit right subtree
    emOrdem(alfabeto, 2 * i + 2)

# Example usage:
alfabeto = list(string.ascii_lowercase)
# emOrdem(alfabeto, 0)


#  Mirage Maintenance
def sequencia():
    conjunto = []
    for i in range(0, 5):
        # temp = int(input('escolha um num: '))
        temp = i
        conjunto.append(temp)
    return diferenca1(conjunto, len(conjunto)-1, [])

def diferenca1(arr, index, diferenca):
    if index <= 0:  # Parar quando index for menor ou igual a 0
        return diferenca[::-1]  # Reverter a lista de diferenças para manter a ordem correta
    subtracao = arr[index] - arr[index - 1]
    diferenca.append(subtracao)
    return diferenca1(arr, index - 1, diferenca)

# print(sequencia())
#  Calorie Counting 
def calories(lista_caloria):
    soma_total = []

    for caloria in lista_caloria:
        soma_individial = 0
        for mais_caloria in caloria:
            soma_individial+=mais_caloria
        soma_total.append(soma_individial)

    maior_caloria_elfo = 0
    for caloria_elfo in soma_total:
        if caloria_elfo > maior_caloria_elfo:
            maior_caloria_elfo = caloria_elfo

    return maior_caloria_elfo
calories([[4,3,2,5],[6,3,1,3],[4,2,21]])

# Rock Paper Scissors
def rockPaperScissors():
    mensagem = 'jogue [a=> rock] ou [b=> paper] ou [c=> scissors]]'
    jogador1 = str(input(mensagem))
    jogador2 = str(input(mensagem))
    if condicao(jogador1,jogador2):
        return rodadas(jogador1,jogador2)
    else:
        return rockPaperScissors()
    

def condicao(jogador1,jogador2):
    jogadores = [jogador1,jogador2]
    for player in jogadores:
        if player != 'a' and player != 'b' and player != 'c':
            return False
        return True
def rodadas(jogador1,jogador2):
    if jogador1 == 'a' and jogador2 == 'c':
        return 'game win jogador1'
    elif jogador1 == 'a' and jogador2 == 'b':
        return 'game win jogador2'
    elif jogador1 == 'b' and jogador2 == 'c':
        return 'jogador 2 win'
    elif jogador1 == 'b' and jogador2 == 'a':
        return 'game win jogador1 win '
    elif jogador1 == 'c' and jogador2 == 'a':
        return 'jogador jogador2 win'
    elif jogador1 == 'c' and jogador2 == 'b':
        return 'jogador1 win'
    return None
# print(rockPaperScissors())

# Rucksack Reorganization
def reorganization(backpacks):
    alfabeto = list(string.ascii_lowercase)
    return set_backpack(backpacks,alfabeto)
def set_backpack(backpacks,alfabeto):
    backpack = [set(),set()]
    x = 0
    for i in backpacks:
        for letra in i:
            backpack[x].add(letra)
        x = x+1
    mochila1 = backpack[0]
    mochila2 = backpack[1]
    intersection = mochila1.intersection(mochila2)
    dict_alfabeto =  {valor: indice for indice, valor in enumerate(alfabeto)}
    output = []
    for i in intersection:
        output.append(dict_alfabeto[i])
    soma_prioridade = 0
    for add in output:
        soma_prioridade+=add 
    return soma_prioridade

# print(reorganization([list('vJrwpWtwJgWr'),list('hcsFMMfFFhFp')]))

#  Supply Stacks 
def supply_stack():
    class No:
        def __init__(self,value):
            self.no = value 
            self.next = None
    class LinkedList:
        def __init__(self):
            self.head = None
            self.removido = None
            self.tail = None
        def insertEnd(self,value):
            if self.head == None:
                novo_no = No(value)
                self.head = novo_no
            else:
                temp = self.head
                while(temp.next):
                    temp = temp.next
                novo_no = No(value)
                temp.next = novo_no
                self.tail = novo_no
        def remover_end(self):
            if self.head is None:
                return None
            else:
                temp = self.head
                while(temp.no != self.tail.no):
                    temp = temp.next
                if self.removido is None:
                    removido = temp.next
                    self.removido = removido
                    temp.next = None
                else:
                    temp_removido = self.removido
                    while(temp_removido.next):
                        temp_removido = temp_removido.next 
                    removido = temp.next
                    temp_removido.next = removido
                    temp.next = None
    class Stack:
        def __init__(self):
            self.stack = LinkedList()
        def append(self,value):
            return self.stack.insertEnd(value)
        def remove(self):
            return self.stack.remover_end()
        def mudar(self):
            if self.stack.head is None:
                return None
            else:
                return self.stack.removido
    stack1 = Stack()
    stack2 = Stack()
    alfabeto = ['a','b','c','d']
    for letra in alfabeto:
        stack1.append(letra)
        stack2.append(letra)
    stack1.remove()
    stack2.append(stack1.mudar())

# supply_stack()
        

