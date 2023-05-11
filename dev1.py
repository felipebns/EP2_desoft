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
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = []
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicao.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicao.append([linha + i, coluna])
    return posicao

def preenche_frota(frota, e, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    if e in frota:
        frota[e].append(posicoes_navio)
    else:
        frota[e] = [posicoes_navio]
    return frota
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    navio = []
    for k,v in frota.items():
        for posicoes in v:
            navio.append(posicoes)
    def define_posicoes(linha, coluna, orientacao, tamanho):
        i = 0
        retorno = [0,0]*tamanho
        retorno2 = []
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
def monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
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
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

for e in frota:
    if e == 'porta-aviões':
        tamanho = 4
    elif e == 'navio-tanque':
        i = 1
        tamanho = 3
    elif e == 'contratorpedeiro':
        i = 1
        tamanho = 2
    elif e == 'submarino':
        i = 1
        tamanho = 1

    while True:
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(e,tamanho))
        linha = int(input('linha>'))
        coluna = int(input('coluna>'))
        valido = True
        if e != 'submarino':
            orientacao = int(input('orientacao>'))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
            else:
                valido = False

        valido2 = posicao_valida(frota, linha, coluna, orientacao, tamanho)
        if valido == True and valido2 == True:
            if e == 'porta-aviões':
                frota = (preenche_frota(frota, e, linha, coluna, orientacao, tamanho))
                break
            elif e == 'navio-tanque':
                if i < 2: #ultimo não atualiza
                    frota = (preenche_frota(frota, e, linha, coluna, orientacao, tamanho))
                    i += 1
                elif i == 2:
                    frota = (preenche_frota(frota, e, linha, coluna, orientacao, tamanho))
                    break
                else:
                    break
            elif e == 'contratorpedeiro':
                if i < 3:
                    frota = (preenche_frota(frota, e, linha, coluna, orientacao, tamanho))
                    i += 1
                elif i == 3:
                    frota = (preenche_frota(frota, e, linha, coluna, orientacao, tamanho))
                    break
                else:
                    break
            elif e == 'submarino':
                if i < 4:
                    frota = (preenche_frota(frota, e, linha, coluna, orientacao, tamanho))
                    i += 1
                elif i == 4:
                    frota = (preenche_frota(frota, e, linha, coluna, orientacao, tamanho))
                    break
                else:
                    break
        else:
            print('Esta posição não está válida!')


tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)


jogando = True
lista = []
verifica = True
while jogando:
    while verifica:
        while True:
            linhaAtaque = int(input('Jogador, qual linha deseja atacar?'))
            if linhaAtaque < 0 or linhaAtaque > 9:
                print('Linha inválida!')
                linhaAtaque = int(input('Jogador, qual linha deseja atacar?'))
            break
        while True:
            colunaAtaque = int(input('Jogador, qual coluna deseja atacar?'))
            if colunaAtaque < 0 or colunaAtaque > 9:
                print('Coluna inválida!')
                colunaAtaque = int(input('Jogador, qual coluna deseja atacar?'))
            break
        if [linhaAtaque, colunaAtaque] in lista: #verifica nessa ordem!!!
            print(('A posição linha {0} e coluna {1} já foi informada anteriormente!').format(linhaAtaque,colunaAtaque))
            break
        else:
            lista.append([linhaAtaque, colunaAtaque]) #guarda na ordem e em lista!!!!
            print(tabuleiro_oponente)
            verifica = False
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente,linhaAtaque,colunaAtaque)
    abatidos = afundados(frota_oponente, tabuleiro_oponente)
    if abatidos == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
jogando = True
lista = []
verifica = True
while jogando:
    while verifica:
        while True:
            linhaAtaque = int(input('Jogador, qual linha deseja atacar? '))
            if linhaAtaque < 0 or linhaAtaque > 9:
                print('Linha inválida!')
                continue
            break
        while True:
            colunaAtaque = int(input('Jogador, qual coluna deseja atacar? '))
            if colunaAtaque < 0 or colunaAtaque > 9:
                print('Coluna inválida!')
                continue
            break
        if [linhaAtaque, colunaAtaque] in lista:
            print(('A posição linha {0} e coluna {1} já foi informada anteriormente!').format(linhaAtaque, colunaAtaque))
            continue
        else:
            lista.append([linhaAtaque, colunaAtaque])
            print(tabuleiro_oponente)
            verifica = False
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linhaAtaque, colunaAtaque)
    abatidos = afundados(frota_oponente, tabuleiro_oponente)
    if abatidos == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:
        print('Seu oponente está atacando na linha {0} e coluna {1}.'.format(linhaOponente, colunaOponente))
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linhaOponente, colunaOponente)
        abatidos_jogador = afundados(frota, tabuleiro_jogador)
        if abatidos_jogador == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
        else:
            verifica = True


