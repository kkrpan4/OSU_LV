with open('SMSSpamCollection.txt', 'r') as file:
    redci = file.readlines()


ham_ukupno_rijeci = 0
ham_broj_poruka = 0
spam_ukupno_rijeci = 0
spam_broj_poruka = 0


spam_sa_usklicnikom= 0

for redak in redci:
    dijelovi = redak.strip().split(maxsplit=1)  
    
    tip = dijelovi[0]     
    poruka = dijelovi[1]  
    
    broj_rijeci = len(poruka.split())  
    
    if tip == "ham":
        ham_ukupno_rijeci += broj_rijeci
        ham_broj_poruka += 1
    elif tip == "spam":
        spam_ukupno_rijeci += broj_rijeci
        spam_broj_poruka += 1
        
        if poruka.endswith("!"):
            spam_sa_uzviком += 1


ham_prosjek = ham_ukupno_rijeci / ham_broj_poruka if ham_broj_poruka > 0 else 0
spam_prosjek = spam_ukupno_rijeci / spam_broj_poruka if spam_broj_poruka > 0 else 0

print("=" * 50)
print("a) PROSJEČAN BROJ RIJEČI")
print("=" * 50)
print(f"Prosječan broj riječi u HAM: {ham_prosjek:.2f}")
print(f"Prosječan broj riječi u SPAM: {spam_prosjek:.2f}")

print("\n" + "=" * 50)
print("b) SPAM PORUKE SA USKLIČNIKOM")
print("=" * 50)
print(f"Broj spam poruka koje završavaju sa !: {spam_sa_usklicnikom}")
