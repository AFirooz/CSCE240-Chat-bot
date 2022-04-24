import os


def counter(file_name):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0

    with open(file_name, 'r') as file:
        for line in file:
            # separating a line from "\n" character and storing again in line variable for further operations
            line = line.strip(os.linesep)

            # splitting the line to make a list of all the words present in that line and storing that list in wordlist variable
            wordslist = line.split()

            num_lines = num_lines + 1
            num_words = num_words + len(wordslist)

            # incrementing value of num_charc by 1 whenever value of variable c is other than white space in the separated line
            num_charc = num_charc + sum(1 for c in line if c not in (os.linesep, ' '))

            # incrementing value of num_spaces by 1 whenever value of variable s is white space in the separated line
            num_spaces = num_spaces + sum(1 for s in line if s in (os.linesep, ' '))
    count = (num_spaces, num_charc, num_lines, num_words)
    return count
