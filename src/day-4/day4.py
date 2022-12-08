import logging

def read_input(text_file_name):
    logging.info("In: read_input()")
    lines = None

    with open(text_file_name) as f:
        lines = f.read()

    split_lines = lines.splitlines()
    
    logging.info("Out: read_input()")
    return split_lines


if __name__ == '__main__':
    result = read_input('input.txt')

    contained_count = 0

    for i in result:
        first, second = i.split(',')
        x1, y1 = map(int, first.split('-'))
        x2, y2 = map(int, second.split('-'))

        if x1 >= x2 and y1 <= y2:
            contained_count += 1
        elif x2 >= x1 and y2 <= y1:
            contained_count += 1

    print(f'Final: {contained_count}')