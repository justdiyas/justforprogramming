from random import shuffle


#Problem 1. Find a target card in a given list of sorted cards.
# A function that locates a target card in a given set of cards
def locate_card(cards, target):
    pass


#below might be the list of dictionary tests cases for different scenarios including edge cases.
#test cases may include an empty list of cards, a list that contains repeated cards, a list that contains no target card etc.
tests = [
    {'input': {'cards': [0, 4, 6, 7, 10, 12, 25], 'target': 4}, 'output': 4},
    {'input': {'cards': [0, 0, 3, 5, 7, 7, 9, 9, 10, 17, 32], 'target': 9}, 'output': 9},
    {'input': {'cards': [1, 2, 6, 8, 13, 19, 20], 'target': 11}, 'output': 11},
]

#running a function for a test case
# locate_card(**tests[0]['input']) == tests[0]['output'])

#create a list of numbers that represent cards and shuffle it
cards = [i for i in range(50)]
shuffle(cards)


#Solution 1 to Problem 1. Brute force method that executes linear search algorithm,
#that is to check all answers from 0 until answer is found and return -1 if target is not in the list.
def locate_card(cards, target):
    index = 0
    while index < len(cards):
        if cards[index] == target:
            return index
        index += 1
    return -1

# print(locate_card(cards, 10))

#checking if in a list of cards there are several repeated cards
def check_location (cards, target, half):
    cards = sorted(cards)
    if target == cards[half]:
        if half - 1 >= 0 and cards[half-1] == target:
            return 'left'
        else:
            return 'found'
    elif target > cards[half]:
        return 'right'
    else:
        return 'left'

#Solution 2 to Problem 1. Binary search algorithm
nums = sorted([1, 4, 5, 7, 2, 3, 18, 15, 10, 77, 85])
def locate_card(cards, target):
    cards = sorted(cards)
    low_index = 0
    high_index = len(cards) - 1
    while low_index <= high_index:
        half = (low_index + high_index) // 2
        result = check_location(cards, target, half)
        if result == 'found':
            return half
        elif result == 'right':
            low_index = half + 1
        elif result == 'left':
            high_index = half - 1
    return -1

#Solution 2.1 to Problem 1. Binary search method but with the help of recursion
# def locate_card(cards, low, high, target):
#     half = (low + high) // 2
#     if cards[half] == target:
#         return half
#     elif target > cards[half] and low <= high:
#         return locate_card(cards, half+1, high, target)
#     elif target < cards[half] and low <= high:
#         return locate_card(cards, low, half-1, target)
#     else:
#         return -1

# print(locate_card(cards, 76))


#Problem 2. Given a rotated sorted list, find a number of times the given list was rotated. Rotated sorted list does not have a repeated numbers.

numbers_rotated = [22, 27, 30, 4, 7, 8, 11, 15, 19]
numbers_not_rotated = [i for i in range(10)]

#Solution 1. Brute force method
def rotation_times(nums):
    index = 0
    while index < len(nums):
        if index > 0 and nums[index] < nums[index-1]:
            return index
        index += 1
    return 0

print(rotation_times(numbers_rotated))
print(rotation_times(numbers_not_rotated))
