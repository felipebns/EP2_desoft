def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = []
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicao.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicao.append([linha + i, coluna])
    return posicao
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes_navio)
    else:
        frota[nome_navio] = [posicoes_navio]
    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
    
print(faz_jogada([
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
],1,1))

def posiciona_frota(frota):
  tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

  lista = []
  for k in frota:
      tipo = frota[k]
      for n in tipo:
         for x in n:
          lista.append(x)
  for j in lista:
    tabuleiro[j[0]][j[1]] = 1
  return tabuleiro

def afundados(frota, tabuleiro):
    afundados = 0
    for tipo, embarcacoes in frota.items():
        for embarcacao in embarcacoes:
            afundada = True
            for posicao in embarcacao:
                linha, coluna = posicao
                if tabuleiro[linha][coluna] != 'X':
                    afundada = False
                    
            if afundada:
                afundados += 1
    return afundados
