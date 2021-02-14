# Finding shortest and longest word in a text
# Filip Zadražil, 3. BGEKA
# winter semester 2020/21
# Úvod do programování MZ370P19

import os 

# Function loading the picked file and checking invalid inputs
def load_file(file_name):
    try:
        with open(file_name, encoding = 'utf-8') as f: # Opening and encoding picked file
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

# Function searching for the shortest and longest word in a text
def search_file(file_text):
    words = file_text.split() # Splitting text to single words

    longest = words[0]
    shortest = words[0]
    longest_length = len(words[0])
    shortest_length = len(words[0])

    for word in words: # Loop checking word by word 
        i = len(word)

        if(word[i-1] == ',' or word[i-1] == "." or word[i-1] == ":"): # Removing commas, dots and colons at the end of the words
            word = word[:-1]
            i = i-1
        
        if(longest_length < i): # Overwriting the longest word, if it is longer than the current one
            longest_length = i
            longest = word

        if(shortest_length > i):  # Overwriting the shortest word, if it is shorter than the current one
            shortest_length = i
            shortest = word

        if(i == longest_length): # Same length requirement
            if word == longest: # Requirement excluding duplicates
                pass
            else:
                longest = longest + ", " + word # Including the non-duplicate same length word
        if(i == shortest_length): # Same length requirement
            if word == shortest: # Requirement excluding duplicates
                pass
            else:
                shortest = shortest + ", " + word # Including the non-duplicate same length word

    # Result excluding 'word/words' and 'is/are' in the output 
    if "," in longest:
        longest_word = "Longest words in the text are: " + longest + " (" + str(longest_length) + " letter/s long)."
    else:
        longest_word = "Longest word in the text is: " + longest + "(" + str(longest_length) + "letter/s long)."

    if "," in shortest:
        shortest_word = "Shortest words in the text are: " + shortest + " (" + str(shortest_length) + " letter/s long)."
    else:
        shortest_word = "Shortest word in the text is: " + shortest + " (" + str(shortest_length) + " letter/s long)."

    outfile = open('result.txt', 'w', encoding = 'utf-8') # Creating a new txt file and saving the results into it
    outfile.write(longest_word + '\n')
    outfile.write(shortest_word)
    outfile.close()
    return longest_word, shortest_word

file_text = load_file("input_file.txt") # Running the function opening the file, in which we want to find the shortest and longest word
longest_word = search_file(file_text) # Running the function searching for the longest word
shortest_word = search_file(file_text) # Running the function searching for the shortest word

