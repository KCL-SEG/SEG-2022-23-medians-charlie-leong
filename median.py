"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        numbers.sort()
        length = len(numbers)
        if(length%2 ==0):
            value = (numbers[int((length/2) -0.5)] + numbers[int((length/2)+0.5)] )/2
        else:
            value = numbers[int(length/2)]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(value)
