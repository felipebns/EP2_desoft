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
