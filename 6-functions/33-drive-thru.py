def get_item(position):
    if position == 1:
        return '🍔 Cheeseburger'
    elif position == 2:
        return '🍟 Fries'
    elif position == 3:
        return '🥤 Soda'
    elif position == 4:
        return '🍦 Ice Cream'
    elif position == 5:
        return '🍪 Cookie'

def welcome():
    print('Welcome to the Drive-Thru! Here\'s the menu:')
    print(f'1: {get_item(1)}')
    print(f'2: {get_item(2)}')
    print(f'3: {get_item(3)}')
    print(f'4: {get_item(4)}')
    print(f'5: {get_item(5)}')

welcome()
order = int(input('Please choose the position you would like to order: '))
print(f'Here is your order: {get_item(order)}')