def count_words(text):
    words_list = text.split()
    return len(words_list)

def count_characters(text):
    character_count = {}
    for ch in text:
        ch_lower = ch.lower()
        if ch_lower not in character_count:
            character_count[ch_lower] = 0
        character_count[ch_lower]+=1
    return character_count

def sort_on(item):
    return item["num"]

def sort_dictionary_to_list(dictionary):
    result = []
    for item in dictionary:
        character_count = {
            "char": item,
            "num": dictionary[item]
        }
        result.append(character_count)
    result.sort(key=sort_on,reverse=True)
    return result
