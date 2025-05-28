def celsius_zu_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_zu_celsius(f):
    return (f -32) * 5/9

print(f"{celsius_zu_fahrenheit(int(input("c -> f")))}")
print(f"{fahrenheit_zu_celsius(int(input("f -> c")))}")