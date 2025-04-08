import datetime
bday_messages = __import__('41-countdown-a')

today = datetime.date.today()
next_birthday = datetime.date(today.year, 5, 5)
days_away = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away.days} days away!')