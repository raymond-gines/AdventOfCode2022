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

    player1_total = 0
    player2_total = 0

    player1_scores = {
        'A X': 4,
        'B X': 8,
        'C X': 3,
        'A Y': 1,
        'B Y': 5,
        'C Y': 9, 
        'A Z': 7,
        'B Z': 2,
        'C Z': 6 
    }

    player2_scores = {
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
        player1_total += player1_scores[i]
        player2_total += player2_scores[i]
        
    print(f'Player 1 Score: { player1_total }')
    print(f'Player 2 Score: { player1_total }')