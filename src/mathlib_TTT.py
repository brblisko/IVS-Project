#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

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
            raise ValueError('Value of ln function needs to be greater than 0')
        n = 100000000.0
        return round(n * ((a ** (1/n)) - 1), 13)

    ##
    # Method parses math expresions from string
    #
    # @param x string from which method parses math expresions
    # @exception Ma ERROR if the x parameter  is less or equal to zero
    # @return result of math expresion

    @staticmethod
    def parse(x):
        while x.find("!") > -1:
            start = x.find("!")
            a = [float(a)
                 for a in re.findall(r'-?\d+\.?\d*', x[start:])]
            if bool(a):
                a = a[0]
                if round(a) == a:
                    x = x.replace(str(a), str(int(a)), 1)
                    a = int(a)
                    x = x.replace("!"+str(a),
                                  str(MathlibTTT.fac(a)), 1)
                else:
                    raise ValueError(
                        'Factorials must be positive integers or the result is too great')
            else:
                raise ValueError('Incorect use of pow()')

        while x.find("root(") > -1:
            startpar = x.find("root(")
            endpar = x[startpar:].find(")")
            s = [float(s)
                 for s in re.findall(r'-?\d+\.?\d*', x[startpar:startpar+endpar])]
            if 2 == len(s):
                x = x.replace(x[startpar:startpar+endpar+1],
                              str(MathlibTTT.root(s[0], s[1])), 1)
            else:
                raise ValueError('Incorect use of root()')

        while x.find("ln(") > -1:
            startpar = x.find("ln(")
            endpar = x[startpar:].find(")")
            s = [float(s)
                 for s in re.findall(r'-?\d+\.?\d*', x[startpar:startpar+endpar])]
            if 1 == len(s):
                x = x.replace(x[startpar:startpar+endpar+1],
                              str(MathlibTTT.ln(s[0])), 1)
            else:
                raise ValueError('Incorect use of ln()')

        while x.find("^") > -1:
            splitx = x.split("^", 1)
            a = [float(a)
                 for a in re.findall(r'-?\d+\.?\d*', splitx[0])]
            b = [float(b)
                 for b in re.findall(r'-?\d+\.?\d*', splitx[1])]

            if bool(a) and bool(b):
                a = a[len(a)-1]
                b = b[0]
                if round(a) == a:
                    x = x.replace(str(a), str(int(a)))
                    a = int(a)
                if round(b) == b:
                    x = x.replace(str(b), str(int(b)))
                    b = int(b)
                x = x.replace(str(a)+"^"+str(b),
                              str(MathlibTTT.pow(a, b)), 1)
            else:
                raise ValueError('Incorect use of pow()')

        while x.find("(") > -1:
            startpar = x.find("(")
            endpar = x.find(")")
            if endpar < 0:
                raise ValueError('Incorect use of parentheses')
            x = x.replace(x[startpar:endpar],
                          MathlibTTT.parse(x[startpar:endpar]), 1)

        if not x.find(")") == -1:
            raise ValueError('Incorect use of parentheses')

        while x.find("*") > -1:
            splitx = x.split("*", 1)
            a = [float(a)
                 for a in re.findall(r'-?\d+\.?\d*', splitx[0])]
            b = [float(b)
                 for b in re.findall(r'-?\d+\.?\d*', splitx[1])]

            if bool(a) and bool(b):
                a = a[len(a)-1]
                b = b[0]
                if round(a) == a:
                    x = x.replace(str(a), str(int(a)))
                    a = int(a)
                if round(b) == b:
                    x = x.replace(str(b), str(int(b)))
                    b = int(b)
                x = x.replace(str(a)+"*"+str(b),
                              str(MathlibTTT.mul(a, b)), 1)
            else:
                raise ValueError('Incorect use of multiplication')

        while x.find("/") > -1:
            splitx = x.split("/", 1)
            a = [float(a)
                 for a in re.findall(r'-?\d+\.?\d*', splitx[0])]
            b = [float(b)
                 for b in re.findall(r'-?\d+\.?\d*', splitx[1])]
            if bool(a) and bool(b):
                a = a[len(a)-1]
                b = b[0]
                if round(a) == a:
                    x = x.replace(str(a), str(int(a)))
                    a = int(a)
                if round(b) == b:
                    x = x.replace(str(b), str(int(b)))
                    b = int(b)
                x = x.replace(str(a)+"/"+str(b),
                              str(MathlibTTT.div(a, b)), 1)
            else:
                raise ValueError('Incorect use of division')

        while x.find("+") > -1 or x.find("-") > -1:
            if x.find("-") == 0 and (x.find("+") > -1 or x[1:].find("-") > -1):
                min_index = x[1:].find("-")
            else:
                min_index = x.find("-")
            if (x.find("+") < min_index and x.find("+") > -1) or (x.find("+") > -1 and min_index == -1):
                splitx = x.split("+", 1)
                a = [float(a)
                     for a in re.findall(r'-?\d+\.?\d*', splitx[0])]
                b = [float(b)
                     for b in re.findall(r'-?\d+\.?\d*', splitx[1])]
                if bool(a) and bool(b):
                    a = a[len(a)-1]
                    b = b[0]
                    if round(a) == a:
                        x = x.replace(str(a), str(int(a)))
                        a = int(a)
                    if round(b) == b:
                        x = x.replace(str(b), str(int(b)))
                        b = int(b)
                    x = x.replace(str(a)+"+"+str(b),
                                  str(MathlibTTT.add(a, b)), 1)
                else:
                    raise ValueError('Incorect use of adding')
            elif min_index < x.find("+") or (min_index > -1 and x.find("+") == -1):
                splitx = x.split("-", 1)
                a = [float(a)
                     for a in re.findall(r'-?\d+\.?\d*', splitx[0])]
                b = [float(b)
                     for b in re.findall(r'-?\d+\.?\d*', splitx[1])]
                if not bool(a) and len(b) == 1:
                    return round(float(x), 2)
                if bool(b):
                    a = a[len(a)-1]
                    b = b[0]
                    if round(a) == a:
                        x = x.replace(str(a), str(int(a)))
                        a = int(a)
                    if round(b) == b:
                        x = x.replace(str(b), str(int(b)))
                        b = int(b)
                    x = x.replace(str(a)+"-"+str(b),
                                  str(MathlibTTT.sub(a, b)), 1)
                else:
                    raise ValueError('Incorect use of subtraction')

        return round(float(x), 3)
