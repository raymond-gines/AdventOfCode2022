import sys
import logging
from string import ascii_lowercase, ascii_uppercase
# from ..lib import common


def read_input(text_file_name):
    logging.info("In: read_input()")
    lines = None

    with open(text_file_name) as f:
        lines = f.read()

    split_lines = lines.splitlines()
    
    logging.info("Out: read_input()")
    return split_lines

def populate_priority_values():
    priorities = {}
    letter_value = 1

    for letter in ascii_lowercase:
        priorities[letter] = letter_value
        letter_value += 1

    letter_value = 27

    for letter in ascii_uppercase:
        priorities[letter] = letter_value
        letter_value += 1

    return priorities


def find_shared_item(rucksack):
    rucksack_size = len(rucksack)
    compartment_size = int(rucksack_size / 2)
    
    compartment_1 = rucksack[0: compartment_size]
    compartment_2 = rucksack[compartment_size: rucksack_size]

    print(f'Rucksack: {rucksack}')
    print(f'Compartment 1: {compartment_1}')
    print(f'Compartment 2: {compartment_2}')

    common_characters = ''.join(set(compartment_1).intersection(compartment_2))

    print(f'Common Character(s): {common_characters}')

    return common_characters

def find_shared_item_group_of_three(group):
    result = set(group[0]) & set(group[1]) & set(group[2])
    return (list(result)[0])

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
 


if __name__ == '__main__':
    elf_input = read_input('sample.txt')

    priority_values = populate_priority_values()

    groups_of_three = list(divide_chunks(elf_input, 3))

    sum_priorities = 0

    # Part 1
    # for rucksack in elf_input:
    #     shared_item = find_shared_item(rucksack)
    #     sum_priorities += priority_values[shared_item]

    # print(sum_priorities)

    # Part 2
    for rucksack in groups_of_three:
        shared_item = find_shared_item_group_of_three(rucksack)
        sum_priorities += priority_values[shared_item]

    # sample = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg']
    # find_shared_item_group_of_three(sample)

    print(sum_priorities)