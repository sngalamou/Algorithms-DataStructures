def countVowels(phrase):
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    for char in phrase.lower():
        if char in vowels:
            count += 1
    print(count)
    return count

countVowels("Simeon")

def is_even(x):
    q, r = divmod(x, 2) 
    return r == 0

print(is_even(2))
