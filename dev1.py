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
