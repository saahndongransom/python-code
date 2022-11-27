sum = 0
cnt = 0
while True:
    inp = input("Enter the number or done: ")
    if (inp == 'done'):
        break
    try:
        inp = int(inp)
        cnt = cnt + 1
        sum = sum + inp
    except:
        print("Enter the numeric value")
        continue

avg = sum / cnt

print("Total is:", sum)
print("Th eCount is:", cnt)
print("Average is:", avg)