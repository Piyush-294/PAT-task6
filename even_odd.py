original_list = [10, 501, 22, 37, 100, 999, 87, 351]
l1 = []
l2 = []
# if the number in list is divided by 2 and remainder is 0 then it is even else odd
for i in original_list:
    if i % 2 == 0:
        l1.append(i)
# here l1 is even list, and we are appending the numbers whose remainder is 0
    elif i % 2 != 0:
        l2.append(i)
# here l2 is odd list, and we are appending the numbers whose remainder is not 0
    else:
        pass

print("even list:", l1)
print("odd list:", l2)
