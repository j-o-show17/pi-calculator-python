"""
Finding Pi of the Nth digit
Developer: Joshua Ola Sorungbe
Algorithm: Chudnovsky Algorithm
"""
import math
from decimal import Decimal, getcontext
from math import factorial


def getDenominator(decimal_places):
    """
    using Chudnovsky Algorithm we iterate through n decimal places
    :param decimal_places: user input for n digits of pi
    :return: return the numerator by iterating through n decimal places
    """
    decimal_places += 1
    getcontext().prec = decimal_places
    sum = 0

    for decimal_places in range(decimal_places):
        numerator = factorial(6*decimal_places) * (13591409+545140134*decimal_places)
        denominator = factorial(3*decimal_places) * (factorial(decimal_places))**3*(640320**(3*decimal_places))
        sum += numerator/denominator

    return Decimal(sum)

def getPi(decimal_places):
    """
    Get the value of pi by division as in Chudnovsky Algorithm
    :param decimal_places:
    :return: pi
    """
    denominator = getDenominator(decimal_places)
    numerator = 426880*math.sqrt(10005)
    pi = Decimal(numerator)/denominator
    return pi

def app():
    """
    This is the interactive function for the user
    called when __name__ = __main__
    :return: no return
    """
    print("Welcome to Pi Calculator!")
    print("Enter number of decimal places you want value of Pi or type 'quit' to exit")

    while True:
        user_input = input("Enter number or 'quit' to exit: ")
        if user_input == "quit":
            break
        if not user_input.isdigit():
            print("You did not enter a number, try again")
        else:
            print(getPi(int(user_input)))

if __name__=="__main__":
    app()