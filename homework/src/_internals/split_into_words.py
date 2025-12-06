def split_into_words(all_lines):
    # split lines into words
    words = []
    for line in all_lines:
        words.extend(words.strip(",.!?") for words in line.split())
    return words
