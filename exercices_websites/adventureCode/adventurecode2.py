# 2021 
# --- Day 1: Sonar Sweep ---
def sonar(lista):
    quantidade = 0
    for i in range(1,len(lista)):
        compra = lista[i]
        anterior = lista[i-1]
        if compra > anterior:
            quantidade+=1
    return quantidade
depth_measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
# print(sonar(depth_measurements))
# --- Day 2: Dive! ---
def dive(dive_input):
    horizontal = 0
    vertical = 0
    for posicao in dive_input:
        comando,valor = posicao.rsplit()
        if comando == 'forward':
            horizontal+=int(valor)
        if comando == 'down':
            vertical+=int(valor)
        if comando == 'up':
            vertical-= int(valor)
    return horizontal * vertical
dive_entrada =  [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]
# print(dive(dive_entrada))

# --- Day 3: Binary Diagnostic ---

def binary_dognostic(binaries):
    gamma = ""
    epsilon = ""
    tamanho = len(binaries[0])
    for i in range(0,tamanho):
        zeros = 0
        one = 0
        for j in range(0,len(binaries)):
            if binaries[j][i] == "0":
                zeros+=1
            else:
                one+=1
        if zeros > one:
            gamma = gamma+"1"
            epsilon = epsilon+"0"
        else:
            gamma = gamma+"0"
            epsilon = epsilon+"1"
    return int(gamma,2) * int(epsilon,2)
entrada_diagnostic_report = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]
# print(binary_dognostic(entrada_diagnostic_report))

# --- Day 4: Giant Squid ---
def calcular_pontuacao(cartelas, numeros_sorteados):
    cartelas = [[[int(num) for num in linha.split()] for linha in cartela.splitlines()] for cartela in cartelas]
    cartelas_marcadas = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(cartelas))]
    
    def venceu(cartela_marcada):
        for i in range(5):
            if all(cartela_marcada[i]) or all(cartela_marcada[j][i] for j in range(5)):
                return True
        return False
    for numero in numeros_sorteados:
    
        for i, cartela in enumerate(cartelas):
            for linha in range(5):
                for coluna in range(5):
                    if cartela[linha][coluna] == numero:
                        cartelas_marcadas[i][linha][coluna] = True
            if venceu(cartelas_marcadas[i]):
                soma_nao_marcados = 0
                for linha in range(5):
                    for coluna in range(5):
                        if not cartelas_marcadas[i][linha][coluna]:
                            soma_nao_marcados += cartela[linha][coluna]
                return soma_nao_marcados * numero
    return 0  
numeros_sorteados = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
cartelas = [
    """22 13 17 11 0
       8 2 23 4 24
       21 9 14 16 7
       6 10 3 18 5
       1 12 20 15 19""",
    """3 15 0 2 22
       9 18 13 17 5
       19 8 7 25 23
       20 11 10 24 4
       14 21 16 12 6""",
    """14 21 17 24 4
       10 16 15 9 19
       18 8 23 26 20
       22 11 13 6 5
       2 0 12 3 7"""
]
# pontuacao = calcular_pontuacao(cartelas, numeros_sorteados)
# print(f'Pontuação final: {pontuacao}')
