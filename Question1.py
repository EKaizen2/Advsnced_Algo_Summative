#variable to store the sum of the integers
ans = 0

#recieving imput from user
num = int(input("enter a number: "))
#adding the recieved number to the variable
ans += num
#looping through the integer received
for x in range(num):
#add the numbers to the variable ans as they loop through them
  ans += x
#Printitng the sum of all the integers added
print(ans)
