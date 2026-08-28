luvut = []

print("Anna luku: ", end="")
for userInput in iter(input, ""):
    luvut.append(userInput)
    print("Anna lukuja: ", end="")
luvut.sort(reverse=True)
for luku in luvut[:5]:
    print(luku)