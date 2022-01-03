def search4vowel(word:str) -> set:
    vowels = set('aeiou')
    x = vowels.intersection(set(word))
    return sorted(x)
