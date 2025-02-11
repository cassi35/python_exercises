# --- Day 1: Report Repair ---
def report_repair(despesas):
    for i, atual_despesa in enumerate(despesas):
        resto = despesas[i + 1:]
        for outra_despesa in resto:
            if atual_despesa + outra_despesa == 2020:
                return atual_despesa * outra_despesa

numeros = [
    1411, 1802, 1773, 1775, 1442, 1471, 1048, 1403, 1881, 1930, 1710, 1717, 685, 1255, 1451, 1870,
    208, 1725, 1879, 143, 1372, 1726, 1357, 1624, 1378, 1993, 1721, 1712, 1867, 1355, 1743, 1942,
    114, 407, 1892, 1937, 2001, 1466, 1461, 1770, 1441, 1410, 1915, 1482, 1512, 1631, 1954, 1632,
    1788, 1971, 1989, 1427, 1684, 1749, 1795, 1839, 1358, 1354, 1591, 1924, 1456, 2002, 1746, 1323,
    1946, 1889, 296, 1908, 1959, 1944, 1655, 1602, 1768, 1666, 1465, 1782, 1739, 1472, 1576, 645,
    1496, 1538, 1761, 1353, 1639, 1904, 1765, 1519, 1948, 1900, 1376, 1918, 1950, 667, 1976, 1925,
    1939, 1319, 1895, 1510, 1480, 735, 1674, 1997, 1868, 1728, 1893, 1500, 1363, 1840, 1905, 1361,
    1894, 1558, 1369, 1922, 1367, 1463, 1365, 1504, 1898, 1343, 1436, 1700, 1911, 1811, 1829, 1984,
    1444, 1806, 1455, 1778, 1835, 1817, 1668, 1907, 1748, 2007, 1534, 1269, 1473, 1572, 2006, 1651,
    1853, 1943, 1968, 1969, 1437, 1692, 1955, 1964, 1821, 1805, 1999, 1614, 1754, 1888, 1832, 1623,
    1723, 1678, 2008, 1819, 1595, 1972, 1229, 1703, 1762, 1818, 1062, 1599, 1996, 2000, 1960, 1927,
    1407, 1414, 1923, 1685, 1998, 1497, 1687, 1416, 1757, 1470, 1810, 2010, 1553, 1379, 1495, 1565,
    1796, 2004, 1899, 2009, 1395, 1388, 1902, 1741
]

relatorio_elfo = report_repair(numeros)
# print(relatorio_elfo)


# --- Day 2: Password Philosophy --- 2020
def password_philosophy():
    contador = 0
    def password(lista,decisao):
        if decisao == False or contador == 3:
            return lista 
        else:
            def existente(senha_nova):
                if len(lista) == 0:
                    return True
                else:
                    for senha in lista:
                        if senha == senha_nova:
                            return False
                        else:
                            return True
            global new_password 
            while True:
                import re 
                new_password = str(input("insira a senha do banco de dados: "))
                if len(re.findall("",new_password)) != 0 and len(new_password) >= 12 and existente(new_password): 
                    break
                else:
                    print("invalid password")
                    continue
            while True:
                alterar = str(input("deseja alterar a senha {senha} [s/n]".format(senha=new_password))) 
                if alterar != 's' and alterar != 'n':
                    print("invalid")
                    continue
                elif alterar == 's':
                    nova_senha = str(input("qual a senha?: "))
                    new_password = nova_senha
                    print('aqui esta a nova senha : {senha}'.format(senha=nova_senha))
                    break
                else:
                    break 
            lista.append(new_password)
            while True:
                continuar = int(input("deseja continuar?[1:'sim', 2:'nao']"))
                if continuar != 1 and continuar != 2:
                    print("invalid")
                    continue
                elif continuar == 1:
                    contador = contador +1
                    return password(lista,decisao=True)
                else:
                    contador = contador +1
                    return password(lista,decisao=False)
    print("digite no maximo 3 senhas:")
    lista_password = password([],True)
    print(lista_password)



# password_philosophy()

# --- Day 3: Toboggan Trajectory ---
def contar_arvores(mapa, movimento_direita, movimento_baixo):
    arvores_encontradas = 0
    posicao_horizontal = 0
    largura_mapa = len(mapa[0])  
    
    for linha in range(0, len(mapa), movimento_baixo):
        if mapa[linha][posicao_horizontal % largura_mapa] == '#':
            arvores_encontradas += 1

        # Move para a direita no mapa
        posicao_horizontal += movimento_direita

    return arvores_encontradas

mapa_exemplo = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]

resultado = contar_arvores(mapa_exemplo, movimento_direita=3, movimento_baixo=1)

print(f"Número de árvores encontradas: {resultado}")



#year 2020 exerc--- Day 4: Passport Processing ---
from colour import Color
import uuid
def passportProcessing(listaPassport):
    valid = []
    nonValid = []
    def validation(passport):
            if passport['key'] != None and passport['value'] != None and passport['hcl'] != None and passport['ecl'] and passport['eyr'] and passport['byr'] != None and passport['hgt'] != None:
                return True 
            else:
                return False
    for i in range(0,len(listaPassport)):
        if validation(listaPassport[i]):
             valid.append(listaPassport[i])
        else:
             nonValid.append(listaPassport[i])
    return len(valid)
listaPassport = []
colors = ['red','green','blue','grey','yellow']
for i in range(0,5):
    import random
    colorChoose = Color(colors[random.randint(0,len(colors)-1)] ).rgb
    pid = uuid.uuid4()
    birthYear = random.randint(1930,2003)
    height = random.uniform(1.50,2.10)
    eyes = ['green','blue','black']
    eyesColor = eyes[random.randint(0,len(eyes)-1)]
    yearExpiration = random.randint(2024-30,2024)+10
    listaPassport.append({'key':i,'value':random.randint(0,10),
                          'hcl':colorChoose,'pid':pid,'byr':birthYear,
                          'hgt':height,'ecl':eyesColor,'eyr':yearExpiration})
    
# print(passportProcessing(listaPassport))

# --- Day 5: Binary Boarding ---
# Função para calcular o número da linha ou coluna baseado na string e no intervalo inicial
def decode_position(instructions, lower_char, upper_char, total_range):
    low, high = 0, total_range - 1
    for char in instructions:
        mid = (low + high) // 2
        if char == lower_char:
            high = mid  
        elif char == upper_char:
            low = mid + 1 
    return low  

def find_highest_seat_id(boarding_passes):
    highest_id = 0
    
    for bp in boarding_passes:
        row = decode_position(bp[:7], 'F', 'B', 128)
        column = decode_position(bp[7:], 'L', 'R', 8)
        seat_id = row * 8 + column
        highest_id = max(highest_id, seat_id)
    
    return highest_id

boarding_passes = [
    "FBFBBFFRLR",
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL",
  
]

# # Resultado
# highest_seat_id = find_highest_seat_id(boarding_passes)
# print(f"O maior ID de assento é: {highest_seat_id}")
# --- Day 6: Custom Customs ---
def questionario(pessoas):
    grupos = pessoas.strip().split('\n\n')

    somatoria_total = 0

    for grupo in grupos:
        respostas = ''.join(grupo.split('\n'))
        respostas_unicas = set(respostas)
        somatoria_total += len(respostas_unicas)

    return somatoria_total


respostas_pessoas = 'abc\n\na\nb\nc\n\nab\nac\n\na\na\na\n\nb\n'
resultado = questionario(respostas_pessoas)
# print("Resultado:", resultado)
# --- Day 7: Handy Haversacks ---
from collections import defaultdict, deque

def parse_rules(rules):
    graph = defaultdict(list)
    for rule in rules:
        bag, contains = rule.split(" bags contain ")
        if "no other bags" in contains:
            continue
        for contained in contains.split(", "):
            count, adj, color, _ = contained.split()
            graph[f"{adj} {color}"].append(bag)
    return graph

def count_outer_bags(graph, target):
    queue = deque([target])
    visited = set()
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return len(visited)

# Exemplo de entrada
rules = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags."
]

# Construindo o grafo
# graph = parse_rules(rules)

# Calculando o número de bolsas que podem conter "shiny gold"
# result = count_outer_bags(graph, "shiny gold")
# print(f"Número de cores de bolsas que podem conter 'shiny gold': {result}")

# --- Day 8: Handheld Halting ---

def interpretador_de_codigo():
    instructions = [
    ("nop", 0),
    ("acc", 1),
    ("jmp", 4),
    ("acc", 3),
    ("jmp", -3),
    ("acc", -99),
    ("acc", 1),
    ("jmp", -4),
    ("acc", 6)
    ]
    index = 0
    visited = []
    acumulador = 0
    while instructions[index] != None:
        current_index = index 
        if current_index in visited:
            return print("laco infinito detectado")
        else:
            if instructions[index][0] == "acc":
                acumulador = acumulador + 1
                visited.append(current_index)
            elif instructions[index][0] == "jmp":
                index = index + instructions[index][1]
                visited.append(current_index)
            else:
                index = index +1 
    return print("não tem loop infinito")
# interpretador_de_codigo()


# --- Day 9: Encoding Error ---
def find_invalid_number(data, preamble_size):
    for i in range(preamble_size, len(data)):
        preamble = data[i - preamble_size:i]
        current_number = data[i]
        if not any(current_number - x in preamble and current_number - x != x for x in preamble):
            return current_number 

    return None 

data = [
    35, 20, 15, 25, 47,
    40, 62, 55, 65, 95,
    102, 117, 150, 182, 127,
    219, 299, 277, 309, 576
]
preamble_size = 5 

# invalid_number = find_invalid_number(data, preamble_size)
# print(f"O primeiro número inválido é: {invalid_number}")


# --- Day 10: Adapter Array ---

def adapter(adaptadores):
    for i in range(0,len(adaptadores)):
      swapped = False
      for j in range(0,len(adaptadores)-i-1):
          if adaptadores[j] > adaptadores[j+1]:
              adaptadores[j],adaptadores[j+1] = adaptadores[j+1],adaptadores[j]
              swapped = True
      if swapped == False:
          break  
    diferenca_1 =1
    diferenca_3 = 1
    print(len(adaptadores))
    i = 1
    while i < len(adaptadores):
        if adaptadores[i-1] +1 == adaptadores[i]:
            diferenca_1 = diferenca_1 +1 
            i = i +1
        else:
            diferenca_3 = diferenca_3 +1 
            i = i +1 

    return print(diferenca_1 * diferenca_3)

numeros = [
    28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 
    24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 
    25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
]
# adapter(numeros)

# --- Day 11: Seating System ---

def count_occupied_neighbors(matrix, row, col):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    occupied = 0
    rows, cols = len(matrix), len(matrix[0])

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and matrix[r][c] == '#':
            occupied += 1
    return occupied

def simulate_seating(matrix):
    rows, cols = len(matrix), len(matrix[0])
    while True:
        new_matrix = [row[:] for row in matrix]
        changed = False

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 'L' and count_occupied_neighbors(matrix, row, col) == 0:
                    new_matrix[row][col] = '#'
                    changed = True
                elif matrix[row][col] == '#' and count_occupied_neighbors(matrix, row, col) >= 4:
                    new_matrix[row][col] = 'L'
                    changed = True

        if not changed:
            break
        matrix = new_matrix

    return sum(row.count('#') for row in matrix)

# Matriz inicial fornecida
matriz = [
    list("L.LL.LL.LL"),
    list("LLLLLLL.LL"),
    list("L.L.L..L.."),
    list("LLLL.LL.LL"),
    list("L.LL.LL.LL"),
    list("L.LLLLL.LL"),
    list("..L.L....."),
    list("LLLLLLLLLL"),
    list("L.LLLLLL.L"),
    list("L.LLLLL.LL")
]

# Executando a simulação
total_occupied = simulate_seating(matriz)
# print("Número total de assentos ocupados:", total_occupied)

# --- Day 13: Shuttle Search ---
def earliest_bus(timestamp, buses):
    buses = [int(bus) for bus in buses.split(",") if bus != "x"] 
    waiting_times = {bus: bus - (timestamp % bus) for bus in buses} 
    best_bus = min(waiting_times, key=waiting_times.get) 
    return best_bus * waiting_times[best_bus] 
timestamp = 939
buses = "7,13,x,x,59,x,31,19"
print(earliest_bus(timestamp, buses))

















