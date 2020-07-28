def findMax(l):
    """
    Description: Finds the maximum number of the given list for numeric values
    """
    try:

        maxValue = max(l)
        return maxValue

    except Exception:
        raise

def fileHandling(fileName):
    """
    Description:
    """
    try:

        with open(fileName, 'w') as f:
            mult, cat = stringOps("Sample")
            f.write(mult + "\n" + cat)

        with open(fileName, 'r') as f:
            for eachline in f:
                print(eachline)

    except Exception:
        raise

def stringOps(ipString):
    """
    Description: Performs basic string operations on the specified string
    """
    try:

        stringMultiplication = ipString * 5
        stringCancat = ipString + " " + "Hello World ..!!"
        return stringMultiplication, stringCancat

    except Exception:
        raise

if __name__ == '__main__':

    try:
        L = [1, 2, 3, 5.0]
        maxValue = findMax(L)
        fileHandling("./testing.txt")
    except TypeError:
        raise Exception("Can't find maximum for non-numeric values")


