def count_vowels(word):
    vowels="aeiou"
    count=0
    for char in word:
        if char in vowels:
            count+=1
    return count
result=count_vowels("biomedical engineering")
print(result)

