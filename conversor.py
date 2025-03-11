def iniciarPrograma():
    pergunta = int(input("Digite o valor em metros que você deseja converter: "))
    print("Convertendo ", pergunta, " metros...")
    conversor(pergunta)
    
def continuarPrograma():
    continuar = int(input("Deseja converter outro número?\n1. Sim\n2. Não\n"))
    if continuar == 1:
        iniciarPrograma()
    elif continuar == 2:
        print("Finalizando...")
        exit()
    else:
        print("Insira um valor válido!")
        continuarPrograma()
    

def conversor(metros):
    quilometro = metros/1000
    centimetro = metros*100
    milimetro = metros*1000
    milha = metros/1609
    jarda = metros*1.094
    pes = metros*3.281
    polegada = metros*39.37
    milhaNautica = metros/1852
    print(metros, "Metros para:\nQuilômetros:", quilometro, "\nCentimetros:", centimetro, "\nMilimetros:", milimetro, "\nMilhas:", milha,"\nJardas:", jarda, "\nPés:", pes, "\nPolegadas:", polegada, "\nMilhas Náuticas:", milhaNautica)
    continuarPrograma()
    
    
iniciarPrograma()