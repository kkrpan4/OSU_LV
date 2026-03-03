while(True):
    try:
        ocjena = float(input('Unesite broj (0.0 - 1.0) : '))
        if ocjena < 0 or ocjena > 1:
            print('Broj mora biti između 0 i 1!')
            continue
        break
    except:
        print('Pogrešan unos, pokušajte ponovo.')


match ocjena:
    case ocjena if ocjena < 0.6:
        print('Ocjena: F')
    case ocjena if ocjena >= 0.6 and ocjena <0.7:
        print('Ocjena: D')
    case ocjena if ocjena >= 0.7 and ocjena <0.8:
        print('Ocjena: C')
    case ocjena if ocjena >= 0.8 and ocjena <0.9:
        print('Ocjena: B')
    case ocjena if ocjena >= 0.9 and ocjena <=1.0:
        print('Ocjena: A')  

