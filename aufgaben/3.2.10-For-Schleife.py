def even_sum(limit):
    acc = 0
    for num in range(limit+1):
        acc += num * ((num + 1) % 2)
    return acc

print(f"Die Summe gerader Zahlen von 1 bis 100 ist gleich: {even_sum(100)}.")

limit = int(input("Bis zu welcher Zahl sollen die geraden Zahlen summiert werden? "))

print(f"Die Summe gerader Zahlen von 1 bis {limit} ist gleich: {even_sum(limit)}.")
