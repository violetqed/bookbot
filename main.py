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

def get_word_dict(text):
    word_dict = {}
    words = text.lower().split()
    for word in words:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
    return word_dict

def get_most_common_word(text):
    most_common_word = ""
    highest_count = 0
    word_dict = get_word_dict(text)

    for word in word_dict:
        if word_dict[word] > highest_count:
            most_common_word = word
            highest_count = word_dict[word]
    return (most_common_word, highest_count)


def report(text, path):
    report_string = f"--- Begin report of {path} ---\n"
    
    num_words = get_num_words(text)
    report_string += f"{num_words} words found in the document\n"

    most_common = get_most_common_word(text)
    most_common_word = most_common[0]
    most_common_word_count = most_common[1]
    most_common_word_percent = ((most_common_word_count / num_words) * 100)
    report_string += f"\"{most_common_word}\" is the most common word in the document ({most_common_word_count} times), representing {most_common_word_percent:.2f}% of words.\n\n"

    character_dict = get_character_dict(text)
    characters = sorted(list(character_dict.keys()))
    for char in characters:
        report_string += f"The '{char}' character was found {character_dict[char]} times\n"
    
    report_string += "--- End report ---"
    return report_string



path = "books/frankenstein.txt"
with open(path) as f:
    text = f.read()
    print(report(text, path))