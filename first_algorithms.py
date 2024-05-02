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


#Solution 1 to Problem 1: Brute force method that executes linear search algorithm,
#that is to check all answers from 0 until answer is found and return -1 if target is not in the list.
def locate_card_bf(cards, target):
    index = 0
    while index < len(cards):
        if cards[index] == target:
            return index
        index += 1
    return -1

# print(locate_card_bf(cards, 10))

#checking if in a list of cards there are several repeated cards
def check_location(cards, target, half):
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

#Solution 2 to Problem 1: Binary search algorithm
nums = sorted([1, 4, 5, 7, 2, 3, 18, 15, 10, 77, 85])
def locate_card_bs(cards, target):
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

#Solution 2.1 to Problem 1: Binary search method but with the help of recursion
# def locate_card_bs(cards, low, high, target):
#     half = (low + high) // 2
#     if cards[half] == target:
#         return half
#     elif target > cards[half] and low <= high:
#         return locate_card_bs(cards, half+1, high, target)
#     elif target < cards[half] and low <= high:
#         return locate_card_bs(cards, low, half-1, target)
#     else:
#         return -1

# print(locate_card_bs(cards, 76))


#Problem 2. Given a rotated sorted list, find a number of times the given list was rotated. Rotated sorted list does not have a repeated numbers.
#E.g.: [20, 0, 6, 8, 10, 17, 18, 19] was rotated 1 time from originally being [0, 6, 8, 10, 17, 18, 19, 20]

#Solution 1 to Problem 2: Brute force method
def rotation_times_bf(nums):
    index = 0
    while index < len(nums):
        if index > 0 and nums[index] < nums[index-1]:
            return index
        index += 1
    return 0

# print(rotation_times_bf(numbers_not_rotated))
# print(rotation_times_bf(numbers_rotated))

#Solution 2 to Problem 2: Binary search algorithm
def rotation_times_bs(nums):
    low = 0
    high = len(nums)-1
    while low <= high:
        half = (low + high) // 2
        if nums[half] < nums[half-1]:
            return half
        elif nums[half] < nums[high]:
            high = half - 1
        else:
            low = half + 1
    return 0

numbers_empty = []
numbers_rotated = [22, 27, 30, 4, 7, 8, 11, 15, 19]
numbers_rotated_1 = [3, 1]
numbers_rotated_2 = [i for i in range(20) if i % 2 != 0] + [0]
numbers_not_rotated = [i for i in range(10)]


#Below testing solution for different scenarios
# print(rotation_times_bs(numbers_empty))
# print(rotation_times_bs(numbers_rotated))
# print(rotation_times_bs(numbers_rotated_1))
# print(rotation_times_bs(numbers_rotated_2))
# print(rotation_times_bs(numbers_not_rotated))


#Problem 3. Create a data structure that is able to store 100 million user profiles including unique username, name and email.
#Data structure must be editable.

#Creating User class that instantiates instances
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f'Username: {self.username}, Name: {self.name}, Email: {self.email}'

#User instances
user1 = User('justdiyas', 'Diyas', 'iyemberidyev@gmail.com')
user2 = User('marathoner', 'Eliud', 'eliud.kipchoge@gmail.com')
user3 = User('skyrunner', 'Kylian', 'kylian.jornet@gmail.com')
user4 = User('microsofter', 'Bill', 'bill.gates@gmail.com')
user5 = User('ggg', 'Genadiy', 'genedaiy.golovkin@gmail.com')
user6 = User('amazoner', 'Jeff', 'jeff.bezos@gmail.com')
user7 = User('investor', 'Warren', 'warren.baffet@gmail.com')

users = [user1, user2, user3, user4, user5, user6, user7]

#Solution 1 to Problem 3: UserDatabase class serves as a data structure that collects user instances to store it.
# Class methods in it are implemented by a brute force way.
class UserDatabaseBF:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users



udb = UserDatabaseBF()
for i in users:
    udb.insert(i)

# print(udb.list_all())
# print(udb.find('investor'))
# user8 = User('ggg', 'Gena', 'gena.golovkin@gmail.com')
# udb.update(user8)
# print(udb.list_all())


#Solution 2 to Problem 3: Methods use binary search algorithm.
class UserDatabaseBS(UserDatabaseBF):
    def __init__(self):
        super().__init__()
        self.users = []

    def insert(self, user):
        pass

    def find(self, username):
        pass

    def update(self, user):
        pass

    def list_all(self):
        return self.users

#Creating binary tree using class
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


node0 = BinaryTree(0)
node1 = BinaryTree(7)
node2 = BinaryTree(5)
node3 = BinaryTree(10)
node4 = BinaryTree(15)

node0.left = node2
node0.right = node1
node0.left.left = node3
node0.left.right = node4

tree = node0
print(tree.value, tree.left, tree.right, tree.left.left, tree.left.right, tree.right.left, tree.right.right)