num=int(input("enter a value: "))
for i in range(2,num):
    if num % i==0:
        print("not a prime number")
        break
    else:
        print("number is prime ")
        break
