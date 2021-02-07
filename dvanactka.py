# Převod čísla c, c ∈ Z+ z dvojkové soustavy do šestnáctkové a naopak
# Filip Zadražil, 3. ročník, BGEKA
# zimní semestr 2020/21
# Úvod do programování MZ370P19  

# Funkce převodu čísla v dvojkové soustavě do šestnáctkové soustavy
def BinToHex():
    while True: # Cyklus provádějící převod za předpokladu splnění daných podmínek
        try:
            bin1 = input("Napište libovolné celé kladné číslo v binární soustavě: ") # Uložení vstupu do proměnné
            hex1 = hex(int(bin1, 2)) # Samotný převod do hexadecimální soustavy + ošetření proti neceločíselnému vstupu
        except ValueError: # Ošetření proti provedení převodu čísel mimo hexadecimální soustavu a necelých čísel
            print("Vámi zadané číslo není v binární soustavě nebo není celočíselné. Zkuste to, prosím, znovu!")
            continue # Výzva pro vložení nového, validního vstupu
        
        if '-' in bin1 or bin1 == '0': # Ošetření proti provedení převodu nekladných čísel
            print("Vámi zadané číslo není kladné. Zkuste to, prosím, znovu!")
            continue # Výzva pro vložení nového, validního vstupu

        print("Ekvivalentní hodnota v hexadecimální soustavě je", hex1[2:] + ".")
        break # Ukončení funkce a pokračování v programu další funkcí
BinToHex() # Spuštění funkce

# Funkce převodu čísla v šestnáctkové soustavě do dvojkové soustavy
def HexToBin():
    while True: # Cyklus provádějící převod za předpokladu splnění daných podmínek
        try:
            hex2 = input("Napište libovolné celé kladné číslo v hexadecimální soustavě: ") # Uložení vstupu do proměnné
            bin2 = bin(int(hex2, 16)) # Samotný převod do binární soustavy + ošetření proti neceločíselnému vstupu
        except ValueError: # Ošetření proti provedení převodu čísel mimo hexadecimální soustavu a necelých čísel
            print("Vámi zadané číslo není v hexadecimální soustavě nebo není celočíselné. Zkuste to, prosím, znovu!")
            continue # Výzva pro vložení nového, validního vstupu
        
        if '-' in hex2 or hex2 == '0': # Ošetření proti provedení převodu nekladných čísel
            print("Vámi zadané číslo není kladné. Zkuste to, prosím, znovu!")
            continue # Výzva pro vložení nového, validního vstupu

        print("Ekvivalentní hodnota v binární soustavě je", bin2[2:] + ".")
        exit() # Ukončení funkce a programu
HexToBin() # Spuštění funkce