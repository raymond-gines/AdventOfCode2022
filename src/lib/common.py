import logging

def print_hello():
    print('hello')

    
def read_input(text_file_name):
    logging.info("In: read_input()")
    lines = None

    with open(text_file_name) as f:
        lines = f.read()

    split_lines = lines.splitlines()
    
    logging.info("Out: read_input()")
    return split_lines