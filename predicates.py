# Words 'n' Predicates

# program parameters
word_file = 'word-list.txt'


# === Utility Functions (do NOT modify) ===

def get_word_list():
    words = []
    with open(word_file) as f:
        for line in f:
            line = line.strip().lower()
            words.append(line)

    # ensure our list of words are sorted
    words.sort()

    print('Read in {} words'.format(len(words)))
    return words


def comma_separated(words):
    return ', '.join(words)


# === Implement your predicates here ===

def is_ascending(word):
    # TODO (1): implement is_ascending() predicate
    
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True


def is_descending(word):
    # TODO (2): implement is_descending() predicate

    for i in range(len(word) - 1):
        if word[i] < word[i + 1]:
            return False
    return True


def is_palindrome(word):
    # TODO (3): implement is_palindrome() predicate
    
    return word == word[::-1]


def has_vowels(word):
    # TODO (4): implement has_vowels() predicate
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(vowels)):
        if vowels[i] in word:
            return True
    return False


# === Write your supporting functions here ===

def report_results(what, words):
    print('\nThere are {} {}'.format(len(words), what))
    print('  First 5:', comma_separated(words[:5]))
    print('   Last 5:', comma_separated(words[-5:]))
    print('  Longest:', comma_separated(longest_words(words)))


def ascending_words(words):
    # TODO (5): return a list of all ascending words
    ascending_words_list = []
    for word in words:
        if is_ascending(word):
            ascending_words_list.append(word)
    return ascending_words_list


def descending_words(words):
    # TODO (6): return a list of all descending words
    descending_words_list = []
    for word in words:
        if is_descending(word):
            descending_words_list.append(word)
    return descending_words_list


def palindromes(words):
    # TODO (7): return a list of all palindromic words
    palindromes_words_list = []
    for word in words:
        if is_palindrome(word):
            palindromes_words_list.append(word)
    return palindromes_words_list


def no_vowels(words):
    # TODO (8): return a list of all words containing no vowels
    no_vowels_word_list = []
    for word in words:
        if not has_vowels(word):
            no_vowels_word_list.append(word)
    return no_vowels_word_list


def longest_words(words):
    # TODO (9): return a list of just the longest words
    len_words = []
    for word in words:
        len_words.append(len(word))
    
    max_word_length = max(len_words)

    longest_words = []
    for word in words:
        if len(word) == max_word_length:
            longest_words.append(word)
    return longest_words


def vowel_count(word):
    # TODO (10): return the number of vowels ('aeiou') found in the word
    vowels = ['a', 'e', 'i', 'o', 'u']
    curr_count = 0
    for i in range(len(word)):
        if word[i] in vowels:
            curr_count += 1
    return curr_count


def find_most_vowels(words):
    # TODO (11): return a list of the word(s) that contain the MOST vowels
    oneWord = []
    for word in words:
        oneWord.append(vowel_count(word))

    most_vowels = max(oneWord)

    most_vowels_words = []
    for word in words:
        if vowel_count(word) == most_vowels:
            most_vowels_words.append(word)
    return most_vowels_words



# === Top level functions  (do NOT modify) ===

def do_ascending(words):
    asc_words = ascending_words(words)
    report_results('ascending words', asc_words)

def do_descending(words):
    desc_words = descending_words(words)
    report_results('descending words', desc_words)

def do_palindromes(words):
    palins = palindromes(words)
    report_results('palindromes', palins)

def do_no_vowels(words):
    nvowels = no_vowels(words)
    report_results('words with no vowels', nvowels)

def do_most_vowels(words):
    most = find_most_vowels(words)
    report_results('words with most vowels', most)


# === Main program ===

def main():
    words = get_word_list()

    # TODO (0): uncomment these lines as you test each section of your code...
    do_ascending(words)
    do_descending(words)
    do_palindromes(words)
    do_no_vowels(words)
    do_most_vowels(words)
    


# run the main function, if script invoked from python interpretter
if __name__ == '__main__':
    main()
