def get_world_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def dict_into_list(char_count):
    char_count_list = []
    isalpha_dump = []
    for char, count in char_count.items():
        if char.isalpha():
         char_count_list.append({'char': char, 'num': count})
        else:
            isalpha_dump.append({'char': char, 'num': count})
            
    return char_count_list


def sort_on(char_count):
    return char_count['num']
