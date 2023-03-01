import sys, random

SEPARATOR = '---'

class Card:
    def __init__(self, lines):
        title = lines[0]
        words = title.split()
        
        self.tags = set()
        question = ''
        for w in words:
            if w[0] == '#':
                self.tags.add(w)
            else:
                question += ' ' + w

        self.question = question.strip()
        self.answer = ''
        for line in lines[1:]:
            self.answer += line

    
    def __str__(self):
        tags = 'Tags: ' + ', '.join(self.tags) + '\n'
        qs = 'Question: ' + self.question + '\n'
        ans = 'Answer: ' + self.answer
        return tags + qs + ans


    def get_q(self):
        return self.question
    
    def get_a(self):
        return self.answer

    def print_q(self):
        print(self.get_q())
    
    def print_a(self):
        print(self.get_a())

    def has_tag(self, tag):
        return tag in self.tags


def build_cards(full_path):
    cards = []
    with open(full_path, 'r') as f:
        card_lines = []
        for line in f:
            cur_l = line.strip()
            if not cur_l or cur_l.isspace():
                continue
            
            if cur_l == SEPARATOR:
                cards.append(Card(card_lines))
                card_lines = []
                continue
            card_lines.append(line)
    return cards


# return to start new game.
def play(all_cards):
    command = input("Start the game with `go [tag]`:\n")
    res = command.split()

    filter_tag = '#flashcard'
    if not res or res[0] != 'go':
        print('Invalid command:', command)
        return
    if len(res) > 1:  # got a tag
        if res[1][0] != '#':
            print('Invalid tag:', res[1])
            return
        filter_tag = res[1]

    cards = [card for card in all_cards if card.has_tag(filter_tag)]
    random.shuffle(cards)

    i = 0
    while i < len(cards):
        c_card = cards[i]
        c_card.print_q()

        com = input()
        if com == 'r':  # redo prev.
            continue
        c_card.print_a()

        com = input()
        if com == 'r':  # redo prev.
            continue
        i += 1

    print('Deck completed.')

def main(full_path):
    cards = build_cards(full_path)
    # for c in cards:
    #     print(c)

    while True:
        play(cards)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Expected 1 arg, path to file.')

