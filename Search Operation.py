# Search Operation
index = -1
for i in range(len(arr)):
    if arr[i] == key:
        index = i
        break

if index != -1:
    print(f"Positon in Array: {index +1}")
else:
    print("Not Found in Array 😒")
