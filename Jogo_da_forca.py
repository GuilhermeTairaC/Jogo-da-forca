Palavra = str(input('Digite a palavra que quiser:'))
Letras = []
Resposta = []
Erros = 0
x = 0
for i in Palavra: # Separa a palavra em letras conrrespondentes a palavra
    Letras.append(i)
for i in range(len(Letras)): # Cria uma lista onde ira ficar a resposta
    A = '_'
    print("                             ")
    print("                             ")
    print("                             ")
    print("                             ")
    print("                             ")
    print("                             ")
    print("                             ")
    Resposta.append(A)
print(f'Contagem de Erros: {Erros}/5') 
while x < (len(Letras)) and Erros < 5: # Funcionamento do jogo
    
    
        
    print(Resposta[::])
    S = (str(input('Digite a Letra que quiser:')))
        
                
    if S in Letras:
        for i in range(len(Letras)):

        
            if S == Letras[i]:
                Resposta [i] = S
                x += 1
   
   
    else:
        Erros += 1
        print('Incorreta!')
        print(f'Contagem de Erros: {Erros}/5') 
if Resposta == Letras:
    for i in range(20):
        print("                             ")
    print(f'Você ganhou a palavra era: {Palavra}')
else:
    for i in range(20):
        print("                             ")
   
    print(f'VocÊ perdeu a palavra era: {Palavra}')

            






