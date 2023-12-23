v= int(input("Enter no 1: "))
s = int(input("Enter no 2: "))

print(f"Additon: {v+s}")
print(f"Subtraction: {v-s}")
print(f"Multipication: {v+s}")
print(f"Division: {v/s}")
print(f"Power: {v**s}")
print(f"Remainder: {v%s}")
print(f"Int div: {v//s}")

t = True
f = False

print("\nAND OPERARIONS:")
print(f"{f}" + f" and {f}" + f" = {f and f}")
print(f"{f}" + f" and {t}" + f" = {f and t}")
print(f"{t}" + f" and {f}" + f" = {t and f}")
print(f"{t}" + f" and {t}" + f" = {t and t}")

print("\nOR OPERARIONS:")
print(f"{f}" + f" or {f}" + f" = {f or f}")
print(f"{f}" + f" or {t}" + f" = {f or t}")
print(f"{t}" + f" or {f}" + f" = {t or f}")
print(f"{t}" + f" or {t}" + f" = {t or t}")

print("\nNOR OPERARIONS:")
print(f"{f}" + f" nor {f}" + f" = {not (f or f)}")
print(f"{f}" + f" nor {t}" + f" = {not (f or t)}")
print(f"{t}" + f" nor {f}" + f" = {not (t or f)}")
print(f"{t}" + f" nor {t}" + f" = {not (t or t)}")

print("\nXOR OPERARIONS:")
print(f"{f}" + f" xor {f}" + f" = {f ^ f}")
print(f"{f}" + f" xor {t}" + f" = {f ^ t}")
print(f"{t}" + f" xor {f}" + f" = {t ^ f}")
print(f"{t}" + f" xor {t}" + f" = {t ^ t}")

