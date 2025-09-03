from collections import Counter

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items[1]

def get_chars_dict(text):
    lower_chars = text.lower()
    chars_dict = Counter(lower_chars)
    return chars_dict

def get_sorted_dict(chars_dict):
    sorted_dict = sorted(chars_dict.items(), key=sort_on, reverse=True)
    return sorted_dict