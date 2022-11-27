#compared number
n1 = int (input ("Enter the 1st number: "))
n2 = int (input ("Enter the 2nd number: "))
n3 = int (input ("Enter the 3rd number: "))

if (n1 < n2):
    if (n1 < n3):
        print ("1st number is the smallest number")
    else:
        print ("3rd number is the smallest number")
elif (n2 < n3):
    print ("2nd number is the smallest nuumber")
else:
    print ("3rd number is the smallest number")