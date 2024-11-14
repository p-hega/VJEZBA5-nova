def erastotenovo_sito(limit):
    brojevi= [True] * (limit + 1)
    brojevi[0] = brojevi[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if brojevi[i]:
            for j in range(i * i, limit + 1, i):
                brojevi[j]= False
    
    prosti_brojevi = [i for i, is_prime in enumerate(brojevi) if is_prime]
    return prosti_brojevi

limit = 542
prvih_100_prostih = erastotenovo_sito(limit)[:100]

print(prvih_100_prostih)
