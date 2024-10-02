def runAtomato( estado_atual, alfa, palavra, final, delta):
    
    for letra in palavra:
        #verifica se a letra esta no alfabeto
        if letra not in alfa: 
            print("Palavra nao aceita")
            return
        
        print("Estado atual: ", estado_atual)
        print("Letra: ", letra)

        est_temp = []
        for estado in estado_atual:
            if estado not in estados:
                continue
            est_temp.extend(delta[estado][letra])
        estado_atual = est_temp

    print("Estado atual: ", estado_atual)    
            
    #verifica se o estado atual é final portanto aceita 
    for estado in estado_atual:
        if estado in final:
            print("aceita")
            break
    else:
        print("rejeita")

def funçao_transiçao(estados, alfa):
    delta = {}
    alfa.append("vazio")

    for estado in estados:
        values = input().split(" ")

        state_dict = {}
        for i in range(len(alfa)):
            state_dict[alfa[i]] = values[i+1].split(",")
        delta[estado] = state_dict

    return delta
   

if __name__ == "__main__":
    estados = input().split(" ")
    alfabeto = input().split(" ")
    estado_atual = input().split(" ")
    estados_finais = input().split(" ")
    func_trans = funçao_transiçao(estados, alfabeto)
    palavras = input().split(" ")

    print(estados)
    print(alfabeto)
    print(estado_atual)
    print(estados_finais)
    print(func_trans)
    print(palavras)

    for palavra in palavras:
        runAtomato(estado_atual, alfabeto, palavra, estados_finais, func_trans)
