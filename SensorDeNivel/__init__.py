sn = int(input('Digite a quantidade: '))
placa = 1
conector = 1
placa = placa * sn
conector = conector * sn
Terminal_Tubular = 5
Terminal_Tubular = Terminal_Tubular * sn
# Determine se "Placa" e "Conector" devem estar no singular ou plural
placa1 = "Placa" if sn == 1 else "Placas"
conector1 = "Conector" if sn == 1 else "Conectores"
Terminal_Tubular1 = "Terminal_tubular" if sn == 1 else "Terminal tubulares"

print('Total: \n{} {} \n{} {} \n{} {}'.format(placa1, placa, conector1, conector, Terminal_Tubular1, Terminal_Tubular, ))
