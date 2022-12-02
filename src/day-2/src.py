import logging


def read_input(text_file_name):
    logging.info("In: read_input()")
    lines = None

    with open(text_file_name) as f:
        lines = f.read()

    split_lines = lines.splitlines()
    
    logging.info("Out: read_input()")
    return split_lines


if __name__ == "__main__":
    result = read_input('sample.txt')

    total = 0

    scoring_table = {
        'A X': 4,
        'B X': 1,
        'C X': 7,
        'A Y': 8,
        'B Y': 5,
        'C Y': 2, 
        'A Z': 3,
        'B Z': 9,
        'C Z': 6 
    }

    for i in result:
        total += scoring_table[i]
        
    print(f'Total Score: { total }')