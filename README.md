class in Python that contains the following two public methods:

    aboveBelow

    accepts two arguments
        An unsorted collection of integers (the list)
        an integer (the comparison value)
    returns a dictionary with the keys "above" and "below" with the corresponding count of integers from the list that are above or below the comparison value

Example usage:

exercise=RTSlab_exercise()
inputList= [1, 5, 2, 1, 10]
outputDic=exercise.aboveBelow(inputList,6)

# output: { "above": 1, "below": 4 }

    stringRotation

    accepts two arguments
        a string (the original string)
        a positive integer (the rotation amount)
    returns a new string, rotating the characters in the original string to the right by the rotation amount and have the overflow appear at the beginning

Example usage:

exercise=RTSlab_exercise()
inputStr="MyString"
outputStr=exercise.stringRotation("MyString", 2)

# output: "ngMyStri"

A test unit was implemented to test the class methods

Usage:

$ python test_exercise.py