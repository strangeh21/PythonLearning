expression = input("Expression: ").strip()
try:
    x, y, z = expression.split(" ")
except ValueError:
    x = expression[0]
    y = expression[1]
    z = expression[2]
finally:
    x = int(x)
    z = int(z)

match y:
    case "+":
        solution = (x + z)
    case "-":
        solution = (x - z)
    case ("*" | "x"):
        solution = (x * z)
    case "/":
        solution = (x / z)
    case _:
        print("Something went wrong. Could not detect Y as any math operator.")

print(f"{solution:.1f}")