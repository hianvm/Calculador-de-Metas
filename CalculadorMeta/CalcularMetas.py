ReceitaTotal = float(input("Insira o valor da sua Meta: "))
ReceitaAtual = float(input("Insira o valor da sua Meta atual: "))
DiasRestantes = int(input("Insira quantos dias restam para acabar a Campanha: "))

ReceitaRestante = ReceitaTotal - ReceitaAtual
MetaDia = ReceitaRestante / DiasRestantes

PdDia = MetaDia / 0.03

if ReceitaRestante <= 0:
    print(" Meta Batida! Parabéns!!!🎉🎉")
    
else:
    print(f"Receita restante: R${ReceitaRestante:.2f}")
    print(f"Meta por dia: R${MetaDia:.2f}")
    print(f"Precisa fazer por dia: R${PdDia:.2f}")



