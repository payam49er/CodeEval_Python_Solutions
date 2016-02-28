__author__ = 'payam'
#Solution to https://www.codeeval.com/open_challenges/237/
import sys
test_cases = open(sys.argv[1], 'r')

def SumAntiVirusComponents(components = []):
    value = 0
    for component in components:
         integerVal = int(component,2)
         value += integerVal
    return value

def SumVirusComponents(components = []):
    value = 0
    for component in components:
        integerVal = int(component,16)
        value += integerVal
    return value


for test in test_cases:
    if len(test) > 0:
        lineValue = test.split("|")
        antiVirusValue = SumAntiVirusComponents(lineValue[1].strip().split(" "))
        virusSideValue =  SumVirusComponents(lineValue[0].strip().split(" "))
        if(antiVirusValue >= virusSideValue):
            print("True")
        else:
            print("False")


test_cases.close()






