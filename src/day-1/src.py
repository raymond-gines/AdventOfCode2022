import logging

def read_elf_calories():
    lines = None

    with open('calories.txt') as f:
        lines = f.readlines()

    return lines

def get_max_calories(calories):
    elf_calories_total = 0
    elf_calories = []

    for i in lines:

        if i == '\n':
            elf_calories.append(elf_calories_total)
            elf_calories_total = 0
        else:
            elf_calories_total += int(i)
    
    return elf_calories


if __name__ == '__main__':
    print("Beginning")
    logging.info("Starting program")

    lines = read_elf_calories()
    max_calories = get_max_calories(lines)
    
    logging.info("Ending program")