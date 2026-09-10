import random

def nopanheitto():
    noppaValue = random.randint(1,6)
    return noppaValue

while True:
    noppa = nopanheitto()
    if noppa == 6:
        print(noppa)
        break
    else:
        print(noppa)
    