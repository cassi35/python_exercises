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
            high = mid  # Metade inferior
        elif char == upper_char:
            low = mid + 1  # Metade superior
    return low  # No final, low e high serão iguais

# Função principal para calcular o maior ID de assento
def find_highest_seat_id(boarding_passes):
    highest_id = 0
    
    for bp in boarding_passes:
        # Primeiros 7 caracteres determinam a linha
        row = decode_position(bp[:7], 'F', 'B', 128)
        # Últimos 3 caracteres determinam a coluna
        column = decode_position(bp[7:], 'L', 'R', 8)
        # Calcula o ID do assento
        seat_id = row * 8 + column
        # Atualiza o maior ID encontrado
        highest_id = max(highest_id, seat_id)
    
    return highest_id

# Entrada (substitua por sua lista de passes de embarque)
boarding_passes = [
    "FBFBBFFRLR",
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL",
    # Adicione mais passes de embarque aqui
]

# # Resultado
# highest_seat_id = find_highest_seat_id(boarding_passes)
# print(f"O maior ID de assento é: {highest_seat_id}")


