def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def count_characters(text):
    char_counts = {}
    for char in text:
        if char.isalpha():
            letter = char.lower()
            char_counts[letter] = char_counts.get(letter, 0) + 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def get_character_list(character_count):
    character_list = []
    for character, count in character_count.items():
        character_dictionary = {"char": character, "num": count}
        character_list.append(character_dictionary)
    character_list.sort(reverse = True, key = sort_on)
    return character_list

def make_report(path, character_list, word_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for character in character_list:
        char = character["char"]
        num = character["num"]
        print(f"The '{char}' character was found {num} times")
    print("--- End report ---")



def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    character_list = get_character_list(character_count)
    make_report(book_path, character_list, word_count)

main()