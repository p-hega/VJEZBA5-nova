def provjera_broja(broj):
    if 10 <= broj <= 100:
        return f"Broj {broj} je unutar raspona."
    else:
        return f"Broj {broj} je izvan raspona."

if __name__== "__main__":
    try:
        uneseni_broj = int(input("unesite broj: "))
        print(provjera_broja(uneseni_broj))
    except ValueError:
        print("Unesena vrijednost nije broj.")
