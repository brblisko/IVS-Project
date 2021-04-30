#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2021

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import re

##
# @package ttt-calc
# MathlibTTT is a mathematical library for our calculator.
#
# Library is made out of basic arithmetic functions such as add,
# subtraction, multiplication, division, factorial, root, power and
# natural logarithm of a number. It also consists of a parser which
# converts string with math expressions into a result
#

##
# @brief Class for MathlibTTT
#


class MathlibTTT:

    ##
    # @brief Sum of two numbers
    #
    # @param a First number
    # @param b Second number
    #
    # @return Sum of a and b

    @staticmethod
    def add(a, b):
        return a + b

    ##
    # @brief Subtraction of two numbers
    #
    # @param a Number from which is subtracted
    # @param b Number which subtracts
    #
    # @return Difference of numbers a and b

    @staticmethod
    def sub(a, b):
        return a - b

    ##
    # @brief Product of two numbers
    #
    # @param a First number
    # @param b Second number
    #
    # @return Product of two numbers a and b

    @staticmethod
    def mul(a, b):
        return a * b

    ##
    # @brief Quotient of two numbers
    #
    # @param a First number, to be divided
    # @param b Second number, divisor
    #
    # @exception Error if b is zero
    # @return Quotient of two numbers a and b

    @staticmethod
    def div(a, b):
        if not b:
            raise ValueError('Dividing by zero')
        if a % b == 0:
            return a / b
        else:
            return float(a)/b

        ##
    # Method computes factorial of a
    #
    # @param a number of which factorial is calculated
    # @exception Error if number a is not a positive integer or the result would be to great
    # @return factorial of number a

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
    # @param a base of the power
    # @param b exponent determines how many times the base will be multiplied
    # @return a raised to the power of b

    @staticmethod
    def pow(a, b):
        if not b:
            return 1
        if b < 0:
            return round(1.0/a**(-b), 13)
        else:
            return round(a**b, 13)

    ##
    # Method calculates b-th root of a
    #
    # @param a the base for which the root will be calculated
    # @param b exponent
    # @exception Error if one or both of the numbers are negative
    # @return b-th root of a

    @staticmethod
    def root(a, b):
        if b <= 0 or a < 0:
            raise ValueError('Both numbers in root need to be positive')
        return round(a ** (1 / float(b)), 13)

    ##
    # Method calculates natural logarithm of a
    #
    # @param a number of which natural logarithm will be calculate
    # @exception Error when value is less or equall of zero
    # @return natural logarithm of a

    @staticmethod
    def ln(a):
        if a <= 0:
            raise ValueError('Value of ln function needs to be greater than 0')
        n = 100000000.0
        return round(n * ((a ** (1/n)) - 1), 13)

    # (\-?|\+?)(\d+\.?\d+|\d*\.?\d+)

    ##
    # Method parses math expresions from string
    #
    # @param x string from which method parses math expresions
    # @exception Error when there is incorrect math syntax
    # @return result of math expresion

    @staticmethod
    def parse(x):
        while x.find("!") > -1:
            splitx = x.split("!", 1)
            a = [float(a)
                 for a in re.findall(r'-?\d+\.?\d*', splitx[0])]
            if bool(a):
                a = a[len(a)-1]
                if round(a) == a:
                    x = x.replace(str(a), str(int(a)), 1)
                    a = int(a)
                x = x.replace(str(a)+"!",
                              str(MathlibTTT.fac(a)), 1)
            else:
                raise ValueError('Incorect use of fac()')

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
                y = x.replace(str(a)+"^"+str(b),
                              str(MathlibTTT.pow(a, b)), 1)
                if not y == x:
                    x = y
                else:
                    raise ValueError('Error with the expression')
            else:
                raise ValueError('Incorect use of pow()')

        while x.find("(") > -1:
            startpar = x.find("(")
            endpar = x.find(")")
            if endpar < 0:
                raise ValueError('Incorect use of parentheses')
            x = x.replace(x[startpar:endpar+1],
                          str(MathlibTTT.parse(x[startpar+1:endpar])), 1)

        if not x.find(")") == -1:
            raise ValueError('Incorect use of parentheses')

        while x.find("*") > -1:
            splitx = x.split("*", 1)
            a = [float(a)
                 for a in re.findall(r'-?\d+\.?\d*', splitx[0])]
            b = [float(b)
                 for b in re.findall(r'-?\d+\.?\d*', splitx[1])]

            if bool(a) and bool(b):
                a = abs(a[len(a)-1])
                b = b[0]
                if round(a) == a:
                    x = x.replace(str(a), str(int(a)))
                    a = int(a)
                if round(b) == b:
                    x = x.replace(str(b), str(int(b)))
                    b = int(b)
                y = x.replace(str(a)+"*"+str(b),
                              str(MathlibTTT.mul(a, b)), 1)
                if not y == x:
                    x = y
                else:
                    raise ValueError('Error with the expression')
            else:
                raise ValueError('Incorect use of multiplication')

        while x.find("/") > -1:
            splitx = x.split("/", 1)
            a = [float(a)
                 for a in re.findall(r'-?\d+\.?\d*', splitx[0])]
            b = [float(b)
                 for b in re.findall(r'-?\d+\.?\d*', splitx[1])]
            if bool(a) and bool(b):
                a = abs(a[len(a)-1])
                b = b[0]
                if round(a) == a:
                    x = x.replace(str(a), str(int(a)))
                    a = int(a)
                if round(b) == b:
                    x = x.replace(str(b), str(int(b)))
                    b = int(b)
                y = x.replace(str(a)+"/"+str(b),
                              str(MathlibTTT.div(a, b)), 1)
                if not y == x:
                    x = y
                else:
                    raise ValueError('Error with the expression')
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
                    y = x.replace(str(a)+"+"+str(b),
                                  str(MathlibTTT.add(a, b)), 1)
                    if not y == x:
                        x = y
                    else:
                        raise ValueError('Error with the expression')
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
                    y = x.replace(str(a)+"-"+str(b),
                                  str(MathlibTTT.sub(a, b)), 1)
                    if not y == x:
                        x = y
                    else:
                        raise ValueError('Error with the expression')
                else:
                    raise ValueError('Incorect use of subtraction')

        if float(x) or float(x) == 0:
            return round(float(x), 3)
        else:
            raise ValueError('Wrong syntax of math function:' + x)
