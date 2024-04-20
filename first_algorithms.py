from random import shuffle


#a function that locates a target card in a given set of cards
def locate_card(cards, target):
    pass


#test cases for different scenarios including edge cases
tests = []

#running a function for a test case
# locate_card(**tests[0]['input']) == tests[0]['output'])

#create a list of numbers that represent cards and shuffle it
cards = [i for i in range(50)]
shuffle(cards)


#solving a problem using brute force solution that executes linear search algorithm,
#that is to check all answers from 0 until answer is found and return -1 if target is not in the list.
def locate_card(cards, target):
    index = 0
    while index < len(cards):
        if cards[index] == target:
            return index
        index += 1
    return -1

print(locate_card(cards, 10))
