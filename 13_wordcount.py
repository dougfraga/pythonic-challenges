"""
13. wordcount

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.
Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.
Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
"""

import sys


# +++ SOLUTION +++
# Define the functions print_words(filename) and print_top(filename).


def open_file(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', ' ')
        words = sorted(data.lower().split())
    return words


def print_words_aux(filename):
    words = open_file(filename)
    counts = dict()

    for word in words:

        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace(";", "")
        word = word.replace(":", "")
        word = word.replace("?", "")
        word = word.replace("!", "")
        word = word.replace("(", "")
        word = word.replace(")", "")
        word = word.replace("(", "")
        word = word.replace("`", "")
        word = word.replace("'", "")
        word = word.replace("\"", "")
        word = word.replace("*", "")
        word = word.replace("--", "")

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def print_words(filename):
    words = print_words_aux(filename)
    result = []
    for k, v in words.items():
        result.append(f'{k} {v}')
    return '\n'.join(result)


def print_top(filename):
    words = print_words_aux(filename)
    sorted_dct = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}
    result = []
    for k, v in sorted_dct.items():
        result.append(f'{k} {v}')
    return '\n'.join(result[:20])


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print(print_words(filename))
    elif option == '--topcount':
        print(print_top(filename))
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
