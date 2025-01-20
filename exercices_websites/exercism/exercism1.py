# robot simulator
class Robo_simulator:
    def __init__(self):
        self.grid = []
        self.column = None
        self.row = None
        self.onde_esta = [None, None]

    def cordenadas_entrada(self, num1, num2):
        if not self.grid:
            new_grid = []
            self.column = num1
            self.row = num2
            for i in range(num1):
                new_row = []
                for x in range(num2):
                    new_row.append(None)
                new_grid.append(new_row)
            self.grid = new_grid
            self.onde_esta[0] = num1 - 1
            self.onde_esta[1] = 0
            self.grid[self.onde_esta[0]][self.onde_esta[1]] = 'R'
            return True

    def printar_entrada(self):
        if not self.grid:
            return None
        else:
            for row in self.grid:
                print(row)
            return

    def mover(self, direcao):
        if direcao == 'd':
            if self.onde_esta[1] + 1 < self.row:
                self.grid[self.onde_esta[0]][self.onde_esta[1]] = None
                self.onde_esta[1] += 1
                self.grid[self.onde_esta[0]][self.onde_esta[1]] = 'R'
            else:
                new_row = [None] * self.row
                new_row[0] = 'R'
                self.grid.append(new_row)
                self.grid[self.onde_esta[0]][self.onde_esta[1]] = None
                self.onde_esta[0] += 1
                self.onde_esta[1] = 0
                self.row += 1
        elif direcao == 'a':
            if self.onde_esta[0] - 1 >= 0:
                self.grid[self.onde_esta[0]][self.onde_esta[1]] = None
                self.onde_esta[0] -= 1
                self.grid[self.onde_esta[0]][self.onde_esta[1]] = 'R'
            else:
                new_row = [None] * self.row
                new_row[0] = 'R'
                self.grid.insert(0, new_row)
                self.grid[self.onde_esta[0]][self.onde_esta[1]] = None
                self.onde_esta[0] = 0
                self.row += 1
        elif direcao == 'l':
            if self.onde_esta[1] - 1 >= 0:
                self.grid[self.onde_esta[0]][self.onde_esta[1]] = None
                self.onde_esta[1] -= 1
                self.grid[self.onde_esta[0]][self.onde_esta[1]] = 'R'
            else:
                new_row = [None] * self.row
                new_row[0] = 'R'
                self.grid.insert(0, new_row)
                self.grid[self.onde_esta[0]][self.onde_esta[1]] = None
                self.onde_esta[1] = 0
                self.row += 1
        return print(self.onde_esta[0], self.onde_esta[1])

# robo = Robo_simulator()
# robo.cordenadas_entrada(7, 3)
# robo.printar_entrada()
# robo.mover('d')
# robo.mover('a')
# robo.mover('l')


# placar de basquete
# colocar em uma fila de 3 em 3 as pessoas que vao changando vao indo pro final e 
# a partida vai demorar 15 minutos se a partida acaba antes ver qual time perdeu e colocar no final da fila
# e se fechar coloca mais 3 times para jogar se nao tiver eles jogam denovo ate 15 
import datetime
import random

class PartidaBasquete:
    def __init__(self):
        self.fila_espera = []
        self.horario = None
        self.ganhador = None

    def jogo(self):
        return len(self.fila_espera) >= 6

    def inserir_pessoa(self, nome):
        if not self.jogo():
            self.fila_espera.append(nome)
            print(f"{nome} adicionado à fila de espera.")
        else:
            print("Já há jogadores suficientes para iniciar uma partida.")

    def iniciar_partida(self):
        if not self.jogo():
            print("Jogadores insuficientes para começar.")
            return

        self.horario = datetime.datetime.now().minute
        self.termino = self.horario + 15

        time1 = self.fila_espera[:3]
        time2 = self.fila_espera[3:6]
        self.fila_espera = self.fila_espera[6:]

        pontuacao1 = pontuacao2 = 0
        while pontuacao1 < 12 and pontuacao2 < 12:
            if random.choice([True, False]):
                pontuacao1 += random.choice([2, 3])
            else:
                pontuacao2 += random.choice([2, 3])

        if pontuacao1 > pontuacao2:
            self.ganhador = time1
            print(f"Time 1 venceu! {pontuacao1} x {pontuacao2}")
            self.colocar_na_fila(time2)
        else:
            self.ganhador = time2
            print(f"Time 2 venceu! {pontuacao2} x {pontuacao1}")
            self.colocar_na_fila(time1)

    def colocar_na_fila(self, time_perdedor):
        for jogador in time_perdedor:
            resposta = input(f"{jogador} quer continuar jogando? [s/n]: ").strip().lower()
            if resposta == 's':
                self.fila_espera.append(jogador)
                print(f"{jogador} voltou para a fila de espera.")

    def exibir_fila(self):
        print("Fila de Espera Atual:", self.fila_espera)


# A leap year
def leap_year(calendar):
    return (calendar % 4 and calendar % 400) == 0
# print(leap_year(1997))
#  Spiral Matrix 


# Grep
def grep_comando():
    import re
    print('contrua um arquivo')
    nome = str(input(f"insira o nome do arquivo:"))
    conteudo = str(input(f"insira o conteudo do arquivo {nome}\n"))
    comando = str(input(f"comando grep: --> "))
    conjuntos = "-n -l -i -v -x"
    comando = comando.rsplit() 
    if len(comando) != 4:
        print("err:length undefined")
        return grep_comando()
    elif re.search("grep",comando[0]) == None or re.search(f"{conjuntos}",comando[1]) == None or re.search(f"{conteudo}",comando[2])  or re.search(f"{nome}",comando[3]):
        print("err:comand")
        return grep_comando()
    else:
        conjunto = re.findall(f"{conjuntos}",comando[1])[0]
        conteudo_escolhido = re.findall(f"{conteudo}",comando[2])[0]
        if conjunto == '-n':
            return print(len(conteudo_escolhido))
        elif conjunto == '-l':
            return print(nome)
        elif conjunto == '-v':
            lines = []
            refeito = conteudo.rsplit()
            for line in refeito:
                if re.search(f"{comando[2]}",line) == None:
                    lines.append(line)
            return print(lines)
        else:
            lines = []
            refeito = conteudo.rsplit()
            for line in refeito:
                if line == comando[2]:
                    lines.append(line)
            return print(lines)
# grep_comando()


