import math


def closeEnough(a, b):
    accuracy = 1e-7
    if abs(a - b) < accuracy:
        return True
    else:
        return False


def enterValues():
    print("Enter the length of the three sides of a triangle.")
    s1 = int(input())
    s2 = int(input())
    s3 = int(input())
    # Check for largest value
    large = s1
    if s2 > s1:
        large = s2
        if s3 > s2:
            large = s3
    # Check which is largest and use pythagorean thereom
    if(large == s1):
        if((math.pow(s1, 2)) == (math.pow(s2, 2) + math.pow(s3, 2))):
            print('True')
        else:
            print('False')
    elif(large == s2):
        if((math.pow(s2, 2)) == (math.pow(s1, 2) + math.pow(s3, 2))):
            print('True')
        else:
            print('False')
    elif(large == s3):
        if((math.pow(s3, 2)) == (math.pow(s2, 2) + math.pow(s1, 2))):
            print('True')
        else:
            print('False')


repeat = 'yes'
while repeat == 'yes' or repeat == 'y':
    enterValues()
    print('Enter new values? (y/n)')
    repeat = input()
