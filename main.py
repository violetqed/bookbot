def get_num_words(text):
    return len(text.split())

def get_character_dict(text):
    character_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char not in character_dict:
                character_dict[char] = 0
            character_dict[char] += 1
    return character_dict

def report(text, path):
    reportstring = f"--- Begin report of {path} ---\n"
    
    num_words = get_num_words(text)
    reportstring += f"{num_words} words found in the document\n\n"

    character_dict = get_character_dict(text)
    characters = sorted(list(character_dict.keys()))
    for char in characters:
        reportstring += f"The '{char}' character was found {character_dict[char]} times\n"
    
    reportstring += "--- End report---"

    return reportstring

path = "books/frankenstein.txt"

with open(path) as f:
    text = f.read()
    print(report(text, path))