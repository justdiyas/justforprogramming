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

# print(locate_card(cards, 10))

#solving above problem using binary search algorithm
nums = sorted([1, 4, 5, 7, 2, 3, 18, 15, 10, 77, 85])
def locate_card(cards, target):
    low_index = 0
    high_index = len(cards) - 1
    while low_index <= high_index:
        half = (low_index + high_index) // 2
        if cards[half] == target:
            return half
        elif target > cards[half]:
            low_index = half + 1
        else:
            high_index = half - 1
    return -1


def locate_card(cards, low, high, target):
    half = (low + high) // 2
    if cards[half] == target:
        return half
    elif target > cards[half] and low <= high:
        return locate_card(cards, half+1, high, target)
    elif target < cards[half] and low <= high:
        return locate_card(cards, low, half-1, target)
    else:
        return -1

print(locate_card(nums, 0, len(nums)-1, -10))
print(nums)