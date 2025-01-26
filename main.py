def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(word_count)
main()