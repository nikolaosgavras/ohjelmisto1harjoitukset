def poistaParittomat(luvut):
    for i in luvut:
        if i % 2 == 1:
            luvut.remove(i)
    return luvut
    

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Alkuperäinen lista: {numberList}")
parittomatLuvut = poistaParittomat(numberList)
print(f"Lista ilman parittomia lukuja: {parittomatLuvut}")
