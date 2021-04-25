#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @package TTTcalc
# MathlibTTT is a mathematical library for our calculator.
#
# This mathematical library consists of basic mathematical operations
# such as sum, difference, multiplication or division, advanced mathematical
# operations such as power, root, natural logarithm. This library also
# includes some conversion functions such as convert_weight, convert_time
# convert_degrees, convert_lenght
#

##
# @brief Class for MathlibTTT
#
class MathlibTTT:

    ##
    # @brief Sum of two numbers
    #
    # @param a First number to be added
    # @param b Second number to be added
    #
    # @return Sum of two numbers a and b

    @staticmethod
    def add(a, b):
        return a + b

    ##
    # @brief Difference of two numbers
    #
    # @param a First number, minor
    # @param b Second number, minority
    #
    # @return Difference of two numbers a and b

    @staticmethod
    def sub(a, b):
        return a - b

    ##
    # @brief Product of two numbers
    #
    # @param a First number to be multiplied
    # @param b Second number to be multiplied
    #
    # @return Product of two numbers a and b

    @staticmethod
    def mul(a, b):
        return a * b

    ##
    # @brief Quotient of two numbers
    #
    # @param a First number, dividend
    # @param b Second number, divisor
    #
    # @return Quotient of two numbers a and b
    # @exception Ma ERROR In case the second number is zero, function will throw error Ma ERROR

    @staticmethod
    def div(a, b):
        if not b:
            raise ValueError('Dividing by zero')
        if a % b == 0:
            return a / b
        else:
            return float(a)/b

        ##
    # Method computes factorial of n
    #
    # @param n number of which factorial is calculated
    # @exception Ma ERROR if the n parameter isn't an inteeger or is less then zero
    # @return factorial of number n

    @staticmethod
    def fac(a):
        if a < 0 or type(a) != int or a > 990:
            raise ValueError(
                'Factorials must be positive integers or the result is too great')
        else:
            if a == 0:
                return 1
            else:
                return a * MathlibTTT.fac(a-1)

    ##
    # Method calculates a base raised to a power
    #
    # @param base base of the power
    # @param exponent exponent determines how many times the base will be multiplied
    # @exception Ma ERROR if the exponent parameter isn't an inteeger or is less or equal to zero
    # @return base raised to the power

    @staticmethod
    def pow(a, b):
        if type(b) != int:
            raise ValueError('Exponent needs to be an integer')
        if not b:
            return 1
        if b < 0:
            return round(1.0/a**(-b), 13)
        else:
            return round(a**b, 13)

    ##
    # Method calculates square root of n
    #
    # @param n the base for which the root will be calculated
    # @param rvalue the exponent
    # @exception Ma ERROR if the rvalue parameter is less or equal to zero or the n parameter
    # is less then zero
    # @return square root of n

    @staticmethod
    def root(a, b):
        if b <= 0 or a < 0:
            raise ValueError('Both numbers in root need to be positive')
        return round(a ** (1 / float(b)), 13)

    ##
    # Method calculates natural logarithm of x
    #
    # @param x number of which natural logarithm will be calculate
    # @exception Ma ERROR if the x parameter  is less or equal to zero
    # @return natural logarithm of x

    @staticmethod
    def ln(a):
        if a <= 0:
            # print("Error - ln value has to be more than 0!")
            raise ValueError('Value of ln function needs to be greater than 0')
        n = 100000000.0
        return round(n * ((a ** (1/n)) - 1), 13)
