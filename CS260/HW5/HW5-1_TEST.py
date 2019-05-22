# Mark Boady
# Drexel University 2018
# Test Bed
import HW5

print("Test Bed for Binary Search Tree Class")
x = int(input("Enter Test Number (1-6):\n"))
if x == 1:
    print("Make an Empty Tree")
    T = HW5.BST()
    print("Your Tree looks like:")
    print(T)
if x == 2:
    print("Make a Balanced Tree.")
    balance = [6, 8, 4, 3, 7, 5, 9]
    print("Inserting:", balance)
    T = HW5.BST()
    for x in balance:
        T.insert(x)
    print("Your Tree looks like:")
    print(T)
if x == 3:
    print("Make a Left Heavy Tree.")
    left = [8, 7, 6, 5, 4, 3, 2]
    print("Inserting:", left)
    T = HW5.BST()
    for x in left:
        T.insert(x)
    print("Your Tree looks like:")
    print(T)
if x == 4:
    print("Make a Right Heavy Tree.")
    right = [1, 2, 3, 4, 6, 5, 7]
    print("Inserting:", right)
    T = HW5.BST()
    for x in right:
        T.insert(x)
    print("Your Tree looks like:")
    print(T)
if x == 5:
    print("Make a Random Tree")
    import random

    random.seed(91)
    rand = [random.randint(0, 100) for x in range(0, 15)]
    print("Inserting:", rand)
    T = HW5.BST()
    for x in rand:
        T.insert(x)
    print("Your Tree looks like:")
    print(T)
if x == 6:
    print("Testing Find")
    import random

    random.seed(26)
    rand = [random.randint(0, 20) for x in range(0, 15)]
    print("Inserting:", rand)
    T = HW5.BST()
    for x in rand:
        T.insert(x)
    print("Your Tree looks like:")
    print(T)
    print("Test all Integers from 0 to 20")
    tests = 0
    passed = 0
    for x in range(0, 21):
        correct = x in rand
        student = T.find(x)
        if correct == student:
            passed += 1
        else:
            print("Searched for", x)
            print("Expected", correct)
            print("Find Returned", student)
        tests += 1
    print("Passed", passed, "out of", tests)
