
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

a = [[0] * columns for _ in range(rows)]
b = [[0] * columns for _ in range(rows)]
c = [[0] * columns for _ in range(rows)]

while True:
    section = input("Enter which section you want (a/b/c or 'exit' to stop): ").lower()
    if section == "exit":
        break

    row = int(input("Enter row number (0-based index): "))
    column = int(input("Enter column number (0-based index): "))

    if 0 <= row < rows and 0 <= column < columns:
        if section == 'a':
            a[row][column] = 1
        elif section == 'b':
            b[row][column] = 1
        elif section == 'c':
            c[row][column] = 1
        else:
            print("Choose the correct seat section.")
    else:
        print("Invalid row or column number. Please enter within the range.")

    
    print("Section A:")
    for r in a:
        print(" ".join(map(str, r)))

    print("Section B:")
    for r in b:
        print(" ".join(map(str, r)))

    print("Section C:")
    for r in c:
        print(" ".join(map(str, r)))
