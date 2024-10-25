# n = 5
# arr = [1,2,3,4,5]
# def convert(self,n:int,a:list[int]) -> None:
#     for i in range(1,n,2):
#         a[i],a[i - 1] = a[i - 1],a[i]
    
#     return len(a)
# c = convert(n,arr)
# print(c)
terror = ["freddye criquer","madrugada da morte"," assano a sangeue frio"]
terror[0] = "mudei"
print(terror)
terrorTuple = (terror[0],terror[1])
y = 6 < 2
x = bool(y)
print(x)
t = frozenset(("cassiano","maria","eduardo"))
palavra = bytes(2)
palavra2 = bytearray(2)
nome = "cassiano"
mensagem = f"bom dia {nome}"

print(mensagem)
i = [[1,2,3],[1,2,3]]
for x in i:
    for y in x:
        print(y * len(x))

######################
#lambda sao funcoes inteligentes 
x = lambda a : a + 10
print(x(5))
########################
#classes sao objetos
# class Person:#pass é caso a minha classe seja vazia entao colocasse o pass
#     def __init__(self,nome,idade) -> None:
#         pass
#         self.nome = nome
#         self.idade = idade
#     def soma(self,idade):
#         self.idade = idade
#         return self.idade
# p1 = Person('cassiano',19)
# x = p1.soma(19)
# print(x)
# del p1.nome #deletar objeto
# print(p1.idade)

#######################

listas = [1,2,3,4,5,6]
# for x in listas:
#     if x == 3:
#         continue
#     print(x)
# for t in range(1,10,2):
#     print(t * 2)
for filho in range(5):
    print('bem vindo a familia {f}'.format(f = filho))