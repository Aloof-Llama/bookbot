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


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"total words: {word_count}")
        character_count = count_characters(file_contents)
        print(f"character count: {character_count}")
main()