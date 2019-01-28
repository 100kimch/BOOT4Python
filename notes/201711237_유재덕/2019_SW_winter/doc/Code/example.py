#example01
def example01:
    inputArray=[3,6,-2,-5,7,3]
    beforeIndex=inputArray[0]
    max1=0
    for index in inputArray[1:len(inputArray):1]:
        if max1 < index*beforeIndex:
            max1=index*beforeIndex
        beforeIndex=index
    print (max1)

#example02
def exapmle02:
    num=0
    for i in range(1001):
        if(i%3==0):
            num+=num
        elif(i%5==0):
            num+=num
    print num