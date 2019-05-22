# Mark Boady
# Drexel University 2018
# Stack Test for CS260

from stack import *
import random

if __name__ == "__main__":
    print("Welcome to Stack Test")
    test_level = int(input("Enter Test Level (1-5):\n"))
    if test_level >= 1:
        print("Step 1: Check that constructor works.")
        S = Stack()
        if (S == None):
            print("Variable not set.")
        else:
            print("Variable Created.")
        print("Step 2: Test Print Empty Stack.")
        if str(S) == "Stack Empty":
            print("Success")
        else:
            print("Returned", str(S), "expected", "Stack Empty")
    # Test Level 2
    if test_level >= 2:
        print("Step 3: Check that Stack is Empty")
        if S.empty() == True:
            print("Success")
        else:
            print("Returned", S.empty(), "expected", True)
        print("Step 4: Add a single Value to Stack")
        S.push(5)
        if str(S) == "[ 5 ]":
            print("Success")
        else:
            print("Returned", str(S), "expected", "[ 5 ]")
    # Test Level 3
    if test_level >= 3:
        print("Step 5: Check top of Stack")
        if S.top() == 5:
            print("Success")
        else:
            print("Returned", S.top(), "expected", 5)
        print("Step 6: Check Stack is not empty")
        if S.empty() == False:
            print("Success")
        else:
            print("Returned", S.empty(), "expected", False)
    # Test Level 4:
    if test_level >= 4:
        print("Step 7: Test Pop")
        S.pop()
        if S.empty() == True:
            print("Success")
        else:
            print("Failure: Stack is not empty! Looks like", str(S))
    # Test Level 5
    if test_level >= 5:
        print("Step 8: Test Adding and removing 100 Random Elements")
        expected = []
        passed = 0
        failed = 0
        for x in range(0, 100):
            test = random.randint(0, 10000)
            expected.append(test)
            S.push(test)
        while not (S.empty()) and failed <= 100:
            if S.top() == expected[len(expected) - 1]:
                passed += 1
            else:
                failed += 1
            S.pop()
            expected.pop(len(expected) - 1)
        if (failed == 0):
            print("Passed", passed, "out of", (passed + failed), "tests.")
        else:
            print("Failed", failed, "out of", (passed + failed), "tests.")

