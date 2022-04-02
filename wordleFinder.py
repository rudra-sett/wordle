import random, sys, time, os
solved_words = [[]]
yellow_words = [[]]
dissalowed_words = [[]]

def get_wordle_words():
    """
    Returns a list of words from a file.
    """
    with open('wordle-words.txt', 'r') as f:
        words = f.read().splitlines()
    return words

def take_input():
    """
    Takes input from the user.
    """
    update_wordle_words()
    
    lens_solved_words = int(input("How many characters do you have solved?: "))
    if lens_solved_words != 0:
        add_words(lens_solved_words, solved_words)

    len_yellow = int(input("How many characters are yellow?: "))
    if len_yellow != 0:
        add_words(len_yellow, solved_words)

    len_dissallowed = int(input("How many characters are dissallowed?: "))
    if len_dissallowed != 0:
        add_words(len_dissallowed, solved_words)

    print(findPossibleWords())

def add_words(words, r):
    """
    Adds words to the list of words.
    """
    if (words == 0):
        return
    r.append([input("Enter char: "), input("Enter the index (starting from 0): ")])
    add_words(words-1, r)

def update_wordle_words():
    return

def findPossibleWords():
    """
    Finds possible words.
    """
    new_words = []
    # loop through the wordle_words and if theres a letter in dissallowed_words, then remove it using a hashmap
    
    for word in wordle_words:
        for i in range(len(word)):
            if word[i] in dissalowed_words:
                word = word.replace(word[i], "")
        new_words.append(word)

    # loop through the new_words and if theres a letter in yellow_words in the same index, then remove it
    for word in new_words:
        for i in range(len(word)):
            if word[i] in yellow_words:
                word = word.replace(word[i], "")
        new_words.append(word)
    
    # loop through the new_words and if theres isnt a letter in solved_words in the same index, then remove it
    for word in new_words:
        for i in range(len(word)):
            if word[i] in solved_words:
                word = word.replace(word[i], "")
        new_words.append(word)

    return new_words

def main():
    """
    Main function.
    """
    global wordle_words
    wordle_words = get_wordle_words()
    take_input()

if __name__ == '__main__':
    main()