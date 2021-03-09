import re
import numpy

def calculateRange(addresses):
    # enter string in format x.x.x.x x.x.x.x

    # regex for finding all numbers
    numbers = re.findall('\d*[^.]', addresses)
    output = []

    # for each octet in address
    for i in range(0, 4):
        # ip address octets and equivalent wildcard octet
        # are stored separated by 4
        ipValue = numbers[i]
        wildcardValue = numbers[i + 4]

        # if its 0, it has to be same as ip value
        if wildcardValue == '0':
            output.append(int(ipValue))
        # if its 255, it can be anything
        elif wildcardValue == '255':
            output.append('x')
        # otherwise find the range
        else:
            output.append(findRange(int(ipValue), int(wildcardValue)))

    return output

def findRange(ipValue, wildcardValue):
    outputRange = []
    # for each possible value of the ip address
    for i in range(0, 256):
        if (i | wildcardValue) == (wildcardValue | ipValue):
            outputRange.append(i)

    return outputRange

def calculateWildcard(addresses):
    addresses = re.findall('\d*\.\d*\.\d*\.\d*', addresses)
    outputIP = []
    outputWC = []
    ipTable = []

    # for each octet
    for i in range(0, 4):
        # initiate an empty table for that octet
        ipTable.append([])
        # for each address
        for j in range(0, len(addresses)):
            # find the numbers in an ip address and return as a list
            target = re.findall('\d*[^.]', addresses[j])
            # insert the number into the octet's list
            ipTable[i].append(int(target[i]))
        # do the bitwise operation on the octet list
        outputWC.append(bitwiseOperate(ipTable[i])[0])
        outputIP.append(bitwiseOperate(ipTable[i])[1])

    return [outputIP, outputWC]

def bitwiseOperate(ipList):
    binaryTable = []
    outputXOR = []
    outputAND = []

    # calculate the binary value of each number and put in list
    for num in ipList:
        binaryTable.append(calculateBinary(num))

    # rotate table 90 degrees
    # puts each binary digit index in the same list, allowing direct
    # comparisons without iterating through loop
    binaryTable = numpy.array(binaryTable, int)
    binaryTable = numpy.rot90(binaryTable)

    # for each binary digit, perform bitwise operation
    for i in range(0, 8):
        # if there is at least one 0 and one 1 in the list
        # this XOR inserts a 1
        if 0 in binaryTable[i] and 1 in binaryTable[i]:
            outputXOR.insert(0, 1)
        # otherwise if all 0s or all 1s insert 0
        else:
            outputXOR.insert(0, 0)
        # if theres a 0 in the list AND inserts a 1
        if 0 in binaryTable[i]:
            outputAND.insert(0, 0)
        # otherwise if all 1s insert 1
        else:
            outputAND.insert(0, 1)

    # convert both lists to decimal and then return
    return [binaryListToDecimal(outputXOR), binaryListToDecimal(outputAND)]

def binaryListToDecimal(binaryList):
    output = 0
    # for each digit in the list
    for i in range(0, len(binaryList)):
        # add the value of the power
        output = output + binaryList[i] * pow(2, 7 - i)

    return output

# performs AND operation on each value in the octet list
def calculateAND(ipList):
    output = ipList[0]
    for i in range(1, len(ipList)):
        output = output & ipList[i]
    return output

def calculateBinary(number):
    output = number
    binaryList = []

    while output > 0:
        # if number is odd, insert a 1 at the highest index
        if output % 2 == 1:
            binaryList.insert(0, 1)
            output = output - 1
        # otherwise insert 0 at highest index
        else:
            binaryList.insert(0, 0)
        # change output
        output = output / 2

    # fill front with 0s up to 8 digits for compatibility
    if len(binaryList) < 8:
        numFill = 8 - len(binaryList)
        for i in range(0, numFill):
            binaryList.insert(0, 0)
    return binaryList
