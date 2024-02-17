class Queue():
    def __init__(self):
        self.cards = []

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def push(self, card):
        self.cards.append(card)

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def pop(self):
        self.cards.pop(0)

if __name__ == '__main__':
    queue1 = Queue.cards
    print(queue1)
    #push tests LR