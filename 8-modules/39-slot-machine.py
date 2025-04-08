import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']
chosen = random.choices(symbols, k=3)

print(f'{chosen[0]} | {chosen[1]} | {chosen[2]}')

if chosen == ['7️⃣', '7️⃣', '7️⃣']:
    print('Jackpot! 💰')
else:
    print('Thanks for playing!')