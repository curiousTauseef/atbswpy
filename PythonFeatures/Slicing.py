a = []

for i in range(1, 11):
    a.append(i)

print("Reverse " + str(a[::-1]))  # reverse order of priting
# print by leaving two elements starting from beginning
print("Leave Two " + str(a[::2]))
# print complete list except the last two elements
print("Except Last two " + str(a[:-2]))
