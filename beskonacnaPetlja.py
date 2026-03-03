import math

brojevi  = []

while(True):
    broj = input('Unesite broj:')

    if(broj.upper() == 'DONE'):
        break

    try:
        broj = int(broj)
        brojevi.append(broj)

    except:
        print('Pogrešan unos, pokušajte ponovo.')

print(f'Brojevi: {len(brojevi)}')
print(f'Srednja vrijednost: {sum(brojevi) / len(brojevi) if brojevi else 0}')
print(f'Minimalni broj: {min(brojevi) if brojevi else 0}')
print(f'Maksimalni broj: {max(brojevi) if brojevi else 0}')
print(f'Sortirana lista: {sorted(brojevi)}')
    