luoti = 13.3
naula = luoti * 32
leiviska = naula * 20

leiviskaInput = float(input("Anna leiviskät: "))
naulaInput = float(input("Anna naulat: "))
luotiInput = float(input("Anna luodit: "))

output = leiviskaInput * leiviska + naulaInput * naula + luotiInput * luoti

kilograms = int(output // 1000)
grams = output % 1000

print(f"\nMassa nykymittojen mukaan:\n{kilograms} kilogrammaa ja {grams:.2f} grammaa")