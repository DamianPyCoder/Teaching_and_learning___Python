def calc_money(hours, minutes):
    mins = hours * 60 + minutes
    return 10 + mins*5

time = input("Temps de la trucada (HH:MM:SS): ")
tokens = time.split(":")

money_cents = calc_money(int(tokens[0]), int(tokens[1]))

euros = int(money_cents / 100)
cents = money_cents % 100
print("Cost de la trucada:",euros,"euros i",cents,"cèntims")
