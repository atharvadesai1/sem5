import keyboard

print("Check if the number is even or odd:")
print("(enter ctrl+c to exit)\n")

try: 
    while True:
        x = int(input("Enter a number: "))

        if(x%2==0):
            print(f"{x} is even")
        else:
            print(f"{x} is odd")

except KeyboardInterrupt:
     print("\n\nExiting the program.")