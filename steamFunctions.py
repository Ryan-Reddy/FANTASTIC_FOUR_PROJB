# Functie voor berekenen gemiddelde prijs van alle games.
def average_game_price():
    # Importeer json om steam.json correct uit te lezen.
    import json

    # Het json bestand uitlezen en opslaan als variable.
    source = open("steam_small.json")
    data = json.load(source)

    # Lees elk spel uit het bestand in en sla het aantal spellen en de totale prijs op.
    count = 0
    total = 0
    for i in data:
        count += 1
        total += int(i["price"])

    # Bepaal de gemiddelde prijs van alle spellen en geeft deze waarde terug als getal met 2 decimalen.
    average = total / count
    # average = "{:.2f}".format(total/count)
    formatting = "{average_price:.2f}"
    return formatting.format(average_price=average) # TODO implement this "quantitative variable" to mainscreen


# Functie voor ophalen van alle game developers.
def list_game_developers():
    # Importeer json om steam.json correct uit te lezen.
    import json

    # Het json bestand uitlezen en opslaan als variable.
    source = open("steam_small.json")
    data = json.load(source)

    # Lees alle developers uit het bestand in en sla de namen op, geeft deze namen terug als resultaat.
    developers = set()
    for i in data:
        x = str(i["developer"])
        developers.add(x)

    return developers


# Functie voor ophalen van alle game developers.
def list_first_game_developers():
    # Importeer json om steam.json correct uit te lezen.
    import json

    # Het json bestand uitlezen en opslaan als variable.
    source = open("steam_small.json")
    data = json.load(source)

    # Lees de developer(s) uit het bestand in van de eerste game en sla deze op, geeft dit terug als resultaat.
    x = data[0]
    developers = x["developer"]
    print(x)
    return developers # TODO implement this "qualitative variable" to mainscreen
