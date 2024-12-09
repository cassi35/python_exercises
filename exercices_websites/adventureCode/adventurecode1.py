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
