# Definindo a linguagem: L = { a^n b^n | n >= 0 }
def linguagem_L(caractere):
    
    n = len(caractere)  # contabiliza quantos caracteres a cadeia tem
    meio = 0  #conta quantos "a"s tem no começo

    # Percorre a cadeia enquanto os caracteres forem 'a'
    while meio < n and caractere[meio] == 'a':
        meio += 1  # Enquanto encontrar "a", vai incrementar o meio

    # Verificar se todos os próximos caracteres serão "b"
    for i in range(meio, n):
        if caractere[i] != 'b':  # Caso encontre algum caractere que não seja 'b', a palavra não pertence à linguagem
            return False

    # Verifica se o número de 'a's é igual ao número de 'b's
    return meio == (n - meio)
    # meio é o número de 'a', n-meio é o número de 'b'
    # Se forem iguais, será retornado True - cadeia pertence, caso contrário, False

# Lema de bombeamento
def aplicar_lema_do_bombeamento(linguagem, p, w):
    
    tamanho = len(w)  # Armazena o tamanho da cadeia w
    quebra_lema = False  # variavel para identificar as quebras do lema de bombeamento

    # Apresenta no terminal as informações iniciais - cadeia, tamanho e o p
    print(f"\nTestando cadeia: {w} (tamanho {tamanho}) com p = {p}")
    print("="*50)

    # Divisões
    for i in range(1, p+1):  
        for j in range(i, p+1):  
            x = w[:i]   # Pega do início até a posição i-1 -> x
            y = w[i:j]  # Pega de i até j-1 -> y
            z = w[j:]   # Pega do j até o fim -> z

            if len(y) == 0:
                continue  # Se y ficar vazio, ignora a divisão

            # Mostra no terminal a divisão que tá sendo testada
            print(f"\nDivisão: x='{x}', y='{y}', z='{z}'")

            # Repetições de y
            for repeticoes in [0, 2, 3, 4, 5, 6]:  
                nova_cadeia = x + (y * repeticoes) + z  # Gera uma nova cadeia bombeada
                pertence = linguagem(nova_cadeia)  # Verifica se nova cadeia pertence à linguagem
                status = "PERTENCE" if pertence else "NÃO PERTENCE"
                print(f" - {repeticoes} repetições de y: '{nova_cadeia}' -> {status}")

                # Se alguma das novas cadeias formadas não pertencer a linguagem, o lema é quebrado
                if not pertence:
                    quebra_lema = True

    # Apresenta o resultado final, pós testes, no terminal
    if quebra_lema:
        print("\nConclusão: Houve quebra do lema. A linguagem NÃO é regular!")
    else:
        print("\nConclusão: Nenhuma quebra encontrada. Não podemos afirmar que a linguagem é não regular.")

# Informações para a execução do programa - bombeamento e cadeia
p = 3 
w = "aaabbb"  

aplicar_lema_do_bombeamento(linguagem_L, p, w)