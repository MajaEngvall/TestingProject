import math

def std_dev(listing):

    
    array=listing
    mean=sum(array)/20

    elements=[]

    for i in range(len(array)):
        diff=array[i]-mean
        square=diff**2
        elements.append(square)

    sum1=sum(elements)
    s=math.sqrt(sum1/19)

    print mean
    print s
