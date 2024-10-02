def runAtomato( estado_atual, alfa, palavra, final):
    for letra in palavra:
        if letra not in alfa: #verifica se a letra esta no alfabeto
            print("Palavra nao aceita")
            return
        else:
            estado_atual = delta[estado_atual][letra]
    if estado_atual in final: #verifica se o estado atual é final portanto aceita
        print("aceita")
        return True
    else: #caso contrario rejeita
        print("rejeita")
        return False
            
estados = input().split(" ")
estado_atual = input() #inicio
final = input().split(" ")
alfa = input().split(" ")

#funcao de transicao (delta)
for estado in estados:
    delta = {}
    var = input().split(" ")
    delta.update({var[0]:{"0":var[1], "1":var[2]}})

palavras = input().split(" ")

for palavra in palavras:
    print("Palavra: ", palavra)
    runAtomato(estado_atual, alfa, palavra, final)
