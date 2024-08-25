def slicer(
    conjunto1,
    conjunto2):  #Função que recebe o conjunto em string e corta e separa-o
  sliced_conjunto1 = conjunto1.split(',')
  sliced_conjunto2 = conjunto2.split(',')
  sliced_conjunto1 = [elemento.strip(' ') for elemento in sliced_conjunto1]
  sliced_conjunto2 = [elemento.strip(' ') for elemento in sliced_conjunto2]
  return sliced_conjunto1, sliced_conjunto2


def uniao(
    conjunto1,
    conjunto2):  #Função que recebe os 2 conjuntos e retorna a união deles
  conjunto_uniao = []

  (sliced_conjunto1, sliced_conjunto2) = slicer(conjunto1, conjunto2)

  for elemento in sliced_conjunto1:
    if elemento not in conjunto_uniao:
      conjunto_uniao.append(elemento)
  for elemento in sliced_conjunto2:
    if elemento not in conjunto_uniao:
      conjunto_uniao.append(elemento)

  print(
      f"Uniao conjunto 1:  [{conjunto1}] conjunto 2: [{conjunto2}]. Resultado:{conjunto_uniao}"
  )
  return conjunto_uniao


def intersecao(
    conjunto1,
    conjunto2):  #Função que recebe os 2 conjuntos e retorna a interseção deles
  conjunto_intersecao = []
  (sliced_conjunto1, sliced_conjunto2) = slicer(conjunto1, conjunto2)

  for elemento in sliced_conjunto1:
    if elemento in sliced_conjunto2:
      conjunto_intersecao.append(elemento)
  print(
      f"Interseção -> conjunto 1:  [{conjunto1}] conjunto 2: [{conjunto2}]. Resultado:{conjunto_intersecao} "
  )
  return conjunto_intersecao


def diferenca(
    conjunto1,
    conjunto2):  #função que recebe os 2 conjuntos e retorna a diferença deles
  conjunto_diferenca = []
  (sliced_conjunto1, sliced_conjunto2) = slicer(conjunto1, conjunto2)
  for elemento in sliced_conjunto1:
    if elemento not in sliced_conjunto2:
      conjunto_diferenca.append(elemento)
  print(
      f"Diferença -> conjunto 1:  [{conjunto1}] conjunto 2: [{conjunto2}]. Resultado:{conjunto_diferenca} "
  )
  return conjunto_diferenca


def produto_cartesiano(
    conjunto1, conjunto2
):  #função que recebe os 2 conjuntos e retorna o produto cartesiano entre eles
  conjunto_produto_cartesiano = []
  (sliced_conjunto1, sliced_conjunto2) = slicer(conjunto1, conjunto2)
  for elemento in sliced_conjunto1:
    par_ordenado = []
    for elemento1 in sliced_conjunto2:
      par_ordenado.append((elemento, elemento1))
    conjunto_produto_cartesiano.append(par_ordenado)
  print(
      f"Produto Cartesiano -> conjunto 1:  [{conjunto1}] conjunto 2: [{conjunto2}]. Resultado:{conjunto_produto_cartesiano} "
  )
  return produto_cartesiano


def operations(linhas, n_operacoes):  #Função que chama as operações
  operation_counter = 0
  for n in range(n_operacoes):
    nop = n + operation_counter
    m = linhas[nop]
    match m:
      case "U":
        uniao(linhas[nop + 1], linhas[nop + 2])
        print('\n')
      case "I":
        intersecao(linhas[nop + 1], linhas[nop + 2])
        print('\n')
      case "D":
        diferenca(linhas[nop + 1], linhas[nop + 2])
        print('\n')
      case "C":
        produto_cartesiano(linhas[nop + 1], linhas[nop + 2])
        print('\n')
      case _:
        print("Operação inválida")
        print('\n')
    operation_counter += 2


file = open("teste1.txt", "r")  #abre o arquivo para leitura
linhas = []

for line in file:  #Separa as linhas
  linhas.append(line.strip('\n'))

n_operacoes = int(linhas[0])  #Recebe a primeira linha do arquivo
linhas.pop(0)  #Remove a primeira linha da lista para facilitar a manipulação
print(f"No arquivo {file.name} temos: {n_operacoes} operações\n")

operations(linhas, n_operacoes)
