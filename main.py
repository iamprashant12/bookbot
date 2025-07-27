from stats import count_words
from stats import count_characters
from stats import sort_dictionary_to_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def main():
    cli_args = sys.argv
    if len(cli_args)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = cli_args[1]
    text = get_book_text(file_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    count_list = sort_dictionary_to_list(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {cli_args[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in count_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

main()