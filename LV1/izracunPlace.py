
def unesiPodatke():
    brojRadnihSati = int(input('Unesite broj radnih sati: '))
    satnica = float(input('Unesite satnicu: '))
    return brojRadnihSati, satnica

def izracunajZaradu(brojRadnihSati, satnica):
    ukupnoZaradeno = brojRadnihSati * satnica
    return ukupnoZaradeno

def ispisiZaradu(ukupnoZaradeno):
    print(f'Ukupno zarađeno: {ukupnoZaradeno:.2f} eura')

brojRadnihSati, satnica = unesiPodatke()
ukupnoZaradeno = izracunajZaradu(brojRadnihSati, satnica)
ispisiZaradu(ukupnoZaradeno)