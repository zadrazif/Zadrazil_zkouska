# Nalezení nejkratšího a nejdelšího slova v textu
# Filip Zadražil, 3. ročník, BGEKA
# zimní semestr 2020/21
# Úvod do programování MZ370P19

import os 

# Funkce otevírající příslušný soubor a ošetřující proti nežádoucím vstupům
def load_file(file_name):
    try:
        with open(file_name, encoding = 'utf-8') as f: # Otevření a dekódování jazyka zkoumaného souboru
            data = f.read()
            if os.path.getsize(file_name) == 0:
                print(f"Soubor {file_name} je prázdný.")
    except ValueError:
        print(f"Soubor {file_name} je chybný.")
        exit()
    except FileNotFoundError:
        print(f"Soubor {file_name} nebyl nalezen.")
        exit()
    except PermissionError:
        print(f"Soubor {file_name} je nepřístupný.")
        exit()  
    return data

# Funkce hledající v textu nejkratší a nejdelší slova
def search_file(file_text):
    nejdelsi = ""
    nejkratsi = ""
    nejdelsi_delka = -1
    nejkratsi_delka = -1

    slova = file_text.split() # Rozdělení textu na jednotlivá slova
    for i in slova: # Cyklus procházející slovo po slově 
        delka = len(i)
        if(i[delka-1] == ',' or i[delka-1] == "." or i[delka-1] == ":"): # Odstranění čárek, teček a dvojteček pro počítání délky slov
            i = i[:-1]
            delka = len(i)
        if(nejdelsi_delka == -1):
            nejdelsi_delka = delka
            nejdelsi = i
        if(nejkratsi_delka == -1):
            nejkratsi_delka = delka
            nejkratsi = i
        if(nejdelsi_delka == delka): 
            if i in nejdelsi: # Podmínka ošetřující stejně dlouhá slova a případnou duplikaci
                pass
            else:
                nejdelsi = nejdelsi + ", " + i 
        if(nejkratsi_delka == delka): 
            if i in nejkratsi: # Podmínka ošetřující stejně dlouhá slova a případnou duplikaci
                pass
            else:
                nejkratsi = nejkratsi + ", " + i
        if(nejdelsi_delka < delka):
            nejdelsi_delka = delka
            nejdelsi = i
        if(nejkratsi_delka > delka):
            nejkratsi_delka = delka
            nejkratsi = i
    longest_word = "Nejdelší slovo/slova v textu je/jsou: " + nejdelsi + " (s délkou " + str(nejdelsi_delka) + ")."
    shortest_word = "Nejkratší slovo/slova v textu je/jsou: " + nejkratsi + " (s délkou " + str(nejkratsi_delka) + ")."
    outfile = open('result.txt', 'w', encoding = 'utf-8') # Vytvoření nového txt souboru a uložení výsledků do něj
    outfile.write(longest_word + '\n')
    outfile.write(shortest_word)
    outfile.close()
    return longest_word, shortest_word

file_text = load_file("input_file.txt") # Spuštění funkce otevírající soubor, v němž hledáme nejkratší a nejdelší slovo
longest_word = search_file(file_text) # Spuštění funkce hledající nejkratší a nejdelší slovo
shortest_word = search_file(file_text) # Spuštění funkce hledající nejkratší a nejdelší slovo

