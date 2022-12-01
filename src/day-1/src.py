import logging


def read_elf_calories(text_file_name):
    logging.info("In: read_elf_calories()")
    lines = None

    with open(text_file_name) as f:
        lines = f.readlines()

    logging.info("Out: read_elf_calories()")
    return lines


def get_elf_calories(calories):
    logging.info("In: get_max_calories()")
    elf_calories_total = 0
    elf_calories = []

    for i in lines:

        if i == '\n':
            elf_calories.append(elf_calories_total)
            elf_calories_total = 0
        else:
            elf_calories_total += int(i)
    
    elf_calories.append(elf_calories_total)

    logging.info("Out: get_max_calories()")
    return elf_calories


if __name__ == '__main__':
    logging.info("Starting program")

    text_file_name = 'calories.txt'

    lines = read_elf_calories(text_file_name)
    elf_calories = get_elf_calories(lines)
    max_calories = max(elf_calories)

    print(max_calories)

    logging.info("Ending program")