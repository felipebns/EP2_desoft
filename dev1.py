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

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    navio = []
    for k,v in frota.items():
        for posicoes in v:
            navio.append(posicoes)
    def define_posicoes(linha, coluna, orientacao, tamanho):
        i = 0
        retorno = [0,0]*tamanho
        retorno2 = []
        grid = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        ] 
        if orientacao == 'vertical':
            retorno = [0,coluna]*tamanho
            while i < tamanho:
                retorno = [linha+ i, coluna]
                retorno2.append(retorno)
                i += 1
        elif orientacao == 'horizontal':
            retorno = [linha,0]*tamanho
            while i < tamanho:
                retorno = [linha, coluna + i]
                retorno2.append(retorno)
                i += 1
        return retorno2
    x = (define_posicoes(linha, coluna, orientacao, tamanho))
    for y in x:
        if y[0] > 9:
            return False
        elif y[1] > 9:
            return False

    for e in navio:
        for ee in e:
            if ee in x:
                return False
    return True
