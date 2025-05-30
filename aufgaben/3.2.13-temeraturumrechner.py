def celsius_zu_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_zu_celsius(f):
    return (f - 32) * 5/9

def main():
    while True:
        input_string = input("Temperatur: ").strip().lower().replace(' ','').replace('°','')
        if input_string.__contains__("s") or input_string.__contains__("q"):
            break
        try:
            for char in input_string:
                if char == 'c':
                    print(f"Das sind {celsius_zu_fahrenheit(float(input_string.split('c')[0]))}°F")
                    break
                if char == 'f':
                    print(f"Das sind {fahrenheit_zu_celsius(float(input_string.split('f')[0]))}°C")
                    break
            else:
                print("Bitte gib die Einheit mit an.")
        except:
            print("Ungültige Eingabe")
    
if __name__ == "__main__":
    main()