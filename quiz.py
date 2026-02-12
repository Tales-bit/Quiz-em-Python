respostas = []
for i in range (0, 1):
    print("====================================")
    print("    Quiz de Matematica em Python")
    print("====================================\n")
    print("Para comecarmos, digite a quantidade de jogadores:", end=" ")
    nj = int(input())
    print("\n")

    with open("perguntas.txt", "r") as arq1, open("gabarito.txt", "r") as arq2:
        # O "3" é o total de questões 
        for i in range(3):
            for i in range(8):
                linha = arq1.readline().rstrip()
                print(linha)
            for i in range(0, nj):
                n = input()
                respostas.append(n)

            # O "3" é o total de respostas
            for i in range(3):
                for i in range(2):
                    linha = arq2.readline().rstrip()
                    for i in range(0, nj):
                        if respostas[nj] == linha