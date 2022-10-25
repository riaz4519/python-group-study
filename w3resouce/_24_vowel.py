def test_vowel(l):
    if l in ["a", "e", "i", "o", "u"]:
        print(l, "is a vowel")
    else:
        print(l, "is a consonant")

test_vowel("a")
test_vowel("b")