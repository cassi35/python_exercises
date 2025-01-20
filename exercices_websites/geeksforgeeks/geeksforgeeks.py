def binarySeach(arr,low,high,x):
    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid +1
        else:
            high = mid -1 
    return -1
arr = [2, 3, 4, 10, 40]
x = 10
result = binarySeach(arr,0,len(arr)-1,x)
print(result)
# def LeftView(self, root):
#         if not root:
#             return []
        
#         left_view = []
#         queue = deque([root])  # Inicializa a fila com o nó raiz
        
#         while queue:
#             # Número de nós no nível atual
#             level_size = len(queue)
            
#             # Para cada nível, o primeiro nó é o nó da vista à esquerda
#             for i in range(level_size):
#                 node = queue.popleft()  # Remove o nó da fila
                
#                 # Se for o primeiro nó do nível, adicione à vista à esquerda
#                 if i == 0:
#                     left_view.append(node.data)
                
#                 # Adiciona os filhos à fila, se existirem
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
        
#         return left_view

# Two Sum - Pair with Given Sum

def sum_two(arr,target):
    if len(arr) < 2:
        return False
    for i in range(0,len(arr)):
        for x in range(i+1,len(arr)):
            if arr[i] + arr[x] == target:
                return True
    return False
def entrada_sum_two():
    arr = [1, 4, 45, 6, 10, 8]
    target = 16
    print(sum_two(arr,target))
entrada_sum_two()