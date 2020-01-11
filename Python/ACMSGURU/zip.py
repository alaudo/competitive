# def gcd(a,b):
#     while True:
#         if b != 0:
#             x = a
#             a = b
#             b = x % b
#         else:
#             return a

# def gcd2(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a 

# def lcm(a,b):
#     return a * b // gcd(a,b)

# lcm2 = lambda a,b: a * b // gcd(a,b)
# print(lcm2(270,192))

# print(lcm(270,192))
# #gcd(13,5)
# #print(gcd2(270,192))

text = """On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."""

def papadontkillme(text):
    x = 0
    y = 0
    text = text.split()
    for s in range(len(text)):
        for s2 in range(len(text)):
            if text[s].strip(".,:") == text[s2].strip(".,:") and s != s2:
                x += 1
        if x > y:
            word = text[s]
            y = x
        x = 0
    return y , text[s]


# print(papadontkillme(text))


def countword(word, d):
    word = word.lower()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

def count_in_sentence(text):
    words = text.split()
    d = {}
    for word in words:
        countword(word,d)
    
    return sorted(d.values())

print(count_in_sentence(text))


