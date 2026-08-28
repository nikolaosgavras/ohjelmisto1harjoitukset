numbers = []

while True:
    userInput = input("Syötä luku: ")
    
    if not userInput.isnumeric():
        break
    
    numbers.append(int(userInput))

smallestNumber = min(numbers)
largestNumber = max(numbers)
print("Pienin arvo:", smallestNumber, "Suurin arvo:", largestNumber)