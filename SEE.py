import math as mt
import sys
from decimal import Decimal

#####################################################
## SET THE BASIC FUNCTIONS FOR THE OPERATORS       ##
#####################################################

def Power(num1, num2):
    answer = num1 ** num2
    return answer

def Multiply(num1, num2):
    answer = num1 * num2
    return answer

def Divide(num1, num2):
    answer = num1 / num2
    return answer

def Add(num1, num2):
    answer = num1 + num2
    return answer

def Subtract(num1, num2):
    answer = num1 - num2
    return answer

####################################################
## DECLARE THE APPROPRIATE LIST TO RECOGNIZE      ##
## FUNCTIONS AND NUMBERS                          ##
##                                                ##
## FUNCTION DICTIONARIES TO CALL FUNCTIONS        ##
## THROUGH THEIR STRING NAME                      ##
####################################################

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
ASCII = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',\
        'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O', \
        'P','Q','R','S','T','U','V','W','X','Y','Z']
FUNCTIONS_1ARG = {'sin': mt.sin, 'cos': mt.cos, 'tan': mt.tan, 'exp': mt.exp}
FUNCTIONS_2ARG = { 'log': mt.log, '^': Power, '*': Multiply, '/': Divide, '+': Add, '-': Subtract}
OPERATORS = ['^', '*', '/', '+', '-']

####################################################
## FUNCTIONS TO PHARSE NUMBERS AND FUNCTION NAMES ##
## AND GET THE ACTUAL FUNCTIONS                   ##
####################################################

def get_number(string, i, length):
    number = []

    while((string[i] in NUMBERS)):
        number.append(string[i])
        i = i + 1

        if(i >= length):
            break

    number = "".join(number)
    number = Decimal(number)
    return number, i - 1

def get_function(string, i, length):
    function = []

    while((string[i] in ASCII) and (i < length)):
        function.append(string[i])
        i = i + 1

        if(i >= length):
            break

    function = "".join(function)
    return function, i - 1

def return_function(function):
    if function in FUNCTIONS_1ARG:
        return FUNCTIONS_FUNCTIONS_1ARG[function]

    else:
         return FUNCTIONS_FUNCTIONS_1ARG[function]

###################################################
## FUNCTIONS TO SET THE PRECEDENCE               ##
###################################################

def precedence(operator):
    if(operator == '^'):
        return 0
    if(operator == '/' or operator ==  '*'):
        return 1
    if(operator == '+' or operator ==  '-'):
        return 2
    else: 
        return 3


#________________________START PROGRAM________________________#

##################################################
## GET THE EXPRESSION PURGE THE WHITESPACES AND ##
## SET THE TWO STACK OF THE ALGORITHM           ##
##################################################

user_string = input("GIVE VALID EXPRESSION:\n")
user_string = user_string.replace(' ','')

NUMBER_STACK = []
OPERATOR_STACK = []

##################################################
## READ AND RECOGNIZE EACH TERM OF THE EXPRESSI ##
## ON AND THEN ACT APPROPRIATELY                ##
## GET CHARACTERS UNTIL THE EXPRESSION STRING H ##
## AS COMPLETELY PHARSED                        ##
##################################################

i = 0

while(i < len(user_string)):
    if(user_string[i] in NUMBERS):
        num, i = get_number(user_string, i, len(user_string))
        NUMBER_STACK.append(num)
        i = i + 1

    elif(user_string[i] in ASCII):
        fun, i = get_function(user_string, i, len(user_string))
        OPERATOR_STACK.append(fun)
        i = i + 1

    elif(user_string[i] == '('):
        OPERATOR_STACK.append('(')
        i = i + 1

    elif(user_string[i] in OPERATORS):
        if OPERATOR_STACK:
            while(precedence(user_string[i]) >= precedence(OPERATOR_STACK[-1])):
                if(OPERATOR_STACK[-1] not in OPERATORS):
                    if(OPERATOR_STACK[-1] in FUNCTIONS_1ARG):
                        a = NUMBER_STACK.pop()
                        f = FUNCTIONS_1ARG[OPERATOR_STACK.pop()]
                        c = Decimal(f(a))
                        NUMBER_STACK.append(c)

                    else:
                        b = NUMBER_STACK.pop()
                        a = NUMBER_STACK.pop()
                        f = FUNCTIONS_2ARG[OPERATOR_STACK.pop()]
                        c = Decimal(f(a, b))
                        NUMBER_STACK.append(c)

                else:
                    b = NUMBER_STACK.pop()
                    a = NUMBER_STACK.pop()
                    f = FUNCTIONS_2ARG[OPERATOR_STACK.pop()]
                    c = Decimal(f(a, b))
                    NUMBER_STACK.append(c)

                if not OPERATOR_STACK:
                    break
                
            OPERATOR_STACK.append(user_string[i])
            i = i + 1

        else:
            OPERATOR_STACK.append(user_string[i])
            i = i + 1

    elif(user_string[i] == ')'):
        while(OPERATOR_STACK[-1] != '('):
            if(OPERATOR_STACK[-1] in FUNCTIONS_2ARG):
                b = NUMBER_STACK.pop()
                a = NUMBER_STACK.pop()
                f = FUNCTIONS_2ARG[OPERATOR_STACK.pop()]
                c = Decimal(f(a, b))
                NUMBER_STACK.append(c)

            else:
                a = NUMBER_STACK.pop()
                f = FUNCTIONS_1ARG[OPERATOR_STACK.pop()]
                c = Decimal(f(a))
                NUMBER_STACK.append(c)

        OPERATOR_STACK.pop()

        if OPERATOR_STACK:
            if((OPERATOR_STACK[-1] not in OPERATORS) and (OPERATOR_STACK[-1] in FUNCTIONS_1ARG)):
                a = NUMBER_STACK.pop()
                f = FUNCTIONS_1ARG[OPERATOR_STACK.pop()]
                c = Decimal(f(a))
                NUMBER_STACK.append(c)

            elif((OPERATOR_STACK[-1] not in OPERATORS) and (OPERATOR_STACK[-1] in FUNCTIONS_2ARG)):
                b = NUMBER_STACK.pop()
                a = NUMBER_STACK.pop()
                f = FUNCTIONS_2ARG[OPERATOR_STACK.pop()]
                c = Decimal(f(a, b))
                NUMBER_STACK.append(c)

            else:
                pass

        i = i + 1
    
    elif(user_string[i] == ','):
        i = i + 1

    else:
        pass

    if(i >= len(user_string)):
        break

###################################################
## IF AN ERROR ON THE FOLLOWING PART OF THE CODE ##
## IT MEANS THAT USER HAS GIVEN MISSALIGNED PARE ##
## NTHESIS, SO TERMINATE WITH ERROR?             ##
###################################################

try:
    while(OPERATOR_STACK):
        if(OPERATOR_STACK[-1] in FUNCTIONS_2ARG):
            b = NUMBER_STACK.pop()
            a = NUMBER_STACK.pop()
            f = FUNCTIONS_2ARG[OPERATOR_STACK.pop()]
            c = Decimal(f(a, b))
            NUMBER_STACK.append(c)

        else:
            a = NUMBER_STACK.pop()
            f = FUNCTIONS_1ARG[OPERATOR_STACK.pop()]
            c = Decimal(f(a))
            NUMBER_STACK.append(c)

except:
    print("MISALLIGNED PARENTHESES. EXITING...\n")
    input()
    sys.exit(-1)

###################################################
## PRINT THE FINAL RESULT AFTER THE OPERATOR STA ##
## CK EMPTYIED ITS CONTENTS AND WAIT FOR EXIT    ##
###################################################

print(NUMBER_STACK.pop())
input()
