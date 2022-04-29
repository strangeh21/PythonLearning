# Demonstrates (unintended) concatenation of strings

# Prompt user for two integers
x = float(input("What's x? "))
y = float(input("What's y? "))

# Print sum
z = round(x + y)
print(f"{z:,}")


try:
    print("X")
except:
    pass
else:
    print("lalala")
finally:
    print("test")