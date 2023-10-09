km = float(input('Qual a quantidade de Km percorridos? '))
Dia = int(input("Qual a Quantidade de dias alugados? "))
total= (Dia * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(total))