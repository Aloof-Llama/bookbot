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



def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"total words: {word_count}")
    character_count = count_characters(text)
    print(f"character count: {character_count}")
    print(character_count.keys())

main()