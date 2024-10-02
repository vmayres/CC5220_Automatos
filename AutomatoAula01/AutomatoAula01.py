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
final = input()
estado_atual = input() #inicio
alfa = input().split(" ")
palavras = input()

delta = {'q1':{"0":'q1', "1":'q2'}, 
         'q2':{"0":'q3', "1":'q2'}, 
         'q3':{"0":'q2', "1":'q2'}}

runAtomato( estado_atual, alfa, palavras)
