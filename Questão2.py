#assumindo que ja conhecemos o processo de fibonacci
#Daremos neste codigo o quantidade de elementos da sequencia em que queremos verificar se o nosso numero está

def fibonacci(Qtda, elem):
    
    achado= False
    fibo_sequencia = [0,1]
    
    if Qtda == 0:
        return achado
    elif Qtda == 1:
        if elem==0:
            achado= True
        return achado
    else:
        for i in range(2,Qtda):
            
            fibo_sequencia.append(fibo_sequencia[i-1]+fibo_sequencia[i-2])
            
            if(elem==fibo_sequencia[i]):
                achado= True
                return achado


elemento = int(input("Digite o elemento que quer saber se esta na sequência:"))
qtda_dada = int(input("Digite a quantidade de numeros da sequência para verificar se o elemento está:"))
sequencia_fibonacci = fibonacci(qtda_dada, elemento)

if(sequencia_fibonacci):
    print("Pertence a sequência de Fibonacci")
else:
    print("Não pertence a sequência de Fibonacci")
