pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))
total_in_usd = pesos * 0.05 + soles * 0.27 + reais * 0.17
print(total_in_usd)