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
    
print(passportProcessing(listaPassport))

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

# Resultado
highest_seat_id = find_highest_seat_id(boarding_passes)
print(f"O maior ID de assento é: {highest_seat_id}")
