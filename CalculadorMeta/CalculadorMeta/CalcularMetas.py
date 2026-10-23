#Solicitamos as informações para o calculo 
ReceitaTotal = float(input("Insira o valor da sua Meta: "))
ReceitaAtual = float(input("Insira o valor da sua Meta atual: "))
DiasRestantes = int(input("Insira quantos dias restam para acabar a Campanha: "))

#Realizamos os calculos 
ReceitaRestante = ReceitaTotal - ReceitaAtual
MetaDia = ReceitaRestante / DiasRestantes

#Definimos que o valor recebido gera 3% de resultado para a meta
PdDia = MetaDia / 0.03

if ReceitaRestante <= 0:
    print(" Meta Batida! Parabéns!!!🎉🎉")
    
else:
    print(f"Receita restante: R${ReceitaRestante:.2f}")
    print(f"Meta por dia: R${MetaDia:.2f}")
    print(f"Precisa fazer por dia: R${PdDia:.2f}")



