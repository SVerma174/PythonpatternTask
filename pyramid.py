n = int(input("Enter the row you want: "))

for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        row += "1" if j % 2 != 0 else "0"
    print(" " * (n - i) + row)