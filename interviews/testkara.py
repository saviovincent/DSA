def all_characters_present(word, string_list):
    word_set = set(word)

    # Check each string in the list
    for string in string_list:
        # Check if all characters of the current string are present in the word
        if set(string).issubset(word_set):
            return string

    # All characters of each string are present in the word
    return "-"


if __name__ == '__main__':

    # Example usage
    word = "apple"
    string_list = ["aper", "plum", "leapp"]

    result = all_characters_present(word, string_list)
    print(result)