#-*- coding:UTF-8 -*-

def isOdd(num):
    return num % 2 != 0

def isOdd2(num):
    return (num & 1) == 1

print(isOdd(-1))
print(isOdd2(-1))






