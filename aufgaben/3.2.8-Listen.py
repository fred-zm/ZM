def get_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens

zahlen = [4, 7, 2, 9, 1, 5, 3]

print(f"Zahlenliste: {zahlen}")
print(f"Länge: {len(zahlen)}")

print(f"Größte: {max(zahlen)}, Kleinste: {min(zahlen)}")
print(f"Durchschnitt {sum(zahlen)/len(zahlen)}")

reverse_zahlen = zahlen
reverse_zahlen.reverse()
print(f"Umgekehrt {reverse_zahlen}")

print(f"Nur die geraden Zahlen: {get_evens(zahlen)}")
