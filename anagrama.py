# Anagrama

# Criação de função que verifica de se duas frases/palavras são anagramas:

def anagrama(s1,s2):

  # Retirada de espaços e convertendo para lower case
  s1 = s1.replace(' ','').lower()
  s2 = s2.replace(' ','').lower()

  # Agora, iremos verificar se s1 e s2 possuem a mesma quantidade de caracteres
  if len(s1) != len(s2):
    return False

  # Ao invés de usar a função sort(), iremos verificar se ambas possuem os
  # mesmos caracteres e na mesma frequência.
  # Definindo um dicionário vazio:
  contagem = {}

  # Fazendo para a s1
  for c in s1:  # Para cada caracter em s1
    if c in contagem:  # Se o caracter já estiver no dict
      contagem[c] += 1  # Acrescenta uma unidade ao caracter
    else:
      contagem[c] = 1  # Cria o novo caracter

  # Fazendo o inverso para s2
  for c in s2:  # Para cada caracter em s2
    if c in contagem:  # Se o caracter já estiver no dict
      contagem[c] -=1  # Reduz em uma unidade
    else:
      contagem[c] = 1  # Cria o novo caracter

  # Agora, é feita a contagem dos caracteres no dicionário contagem.
  # Caso todos os caracteres não tenham nenhum elemento, então as duas frases
  # são anagramas.
  for e in contagem:  # para cada elemento no dicionário
    if contagem[e] != 0:  # se o caracter possui algum elemento
      return False

  # Caso não haja nenhum elemento no dicionário
  return True

# Exemplo 1
a = 'Iracema'
b = 'America'
anagrama(a,b)

# Exemplo 2
c = 'Clint Eastwood'
d = 'Old West Action'
anagrama(c,d)

# Exemplo 3
e = 'aAvf'
f = 'VVaA'
anagrama(e,f)
