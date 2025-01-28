# Queues (double ended queue)

# Importa uma queue -> objeto que pode ser modificado pela esquerda e pela direita
from collections import deque

# Add elementos à direita
queue = deque()
queue.append(1)
queue.append(2)
print(queue)
print('\n')

# Removendo elemento da esquerda
queue.popleft()
print(queue)
print('\n')

# Add elemento à esquerda
queue.appendleft(3)
print(queue)
print('\n')

# Removendo elemento à direita
queue.pop()
print(queue)
print('\n')