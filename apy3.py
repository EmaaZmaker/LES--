start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
squares = []
odd_squares = []
even_squares = []
for num in range(start, end + 1):
    square = num * num
    squares.append(square)
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)
print("All square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)
