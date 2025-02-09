# Função que retorna a soma máxima dos elementos (+ e -) de uma array

def largest(arr):

  # Se o array não tiver elementos:
  if len(arr) == 0:
    return print('Array sem elementos!')

  # Criação de variável para guardar a soma máxima
  max_sum = current_sum = arr[0]  # Armazena o primeiro valor do array

  for num in arr[1:]:  # Para cada elemento no array, exceto o primeiro
    current_sum = max(current_sum + num, num)  # A soma atual será o max entre o num e a soma
    max_sum = max(current_sum, max_sum)

  # Retorna o valor máximo da soma
  return max_sum

# Exemplo
print(largest([7,1,2,-1,3,4,10,-12,3,21,-19]))
