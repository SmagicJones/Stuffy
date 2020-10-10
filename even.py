import time

iseven = []

nums = [0, 25, 34, 67, 88, 22, 56, 809, 1004, 2, 6, 8, 90, 99,]


print("this program goes through the items in the nums and checks whether they are even")
time.sleep(1)
print('here is nums')
time.sleep(1)
print(nums)
time.sleep(1)
print('you can add more numbers to nums is you want')
time.sleep(1)
print("if a number is nums is even it is added to the empty list iseven[]")
time.sleep(1)
print("if a number is not even we print 'not even' ")
time.sleep(1)
print("finally we print the iseven[] list with the even numbers from nums added")
time.sleep(1)




for i in range(len(nums)):
    if i % 2 == 0:
        iseven.append(i)
    else:
        print('not even')

print(iseven)
        
