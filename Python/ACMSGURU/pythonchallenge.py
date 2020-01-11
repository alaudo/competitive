text = '''map'''
print()
decoded = []

for l in text:
    if l == ' ':
        decoded.append(l)
    else: 
        decoded.append( chr( ((ord(l) + 2) - ord('a')) % 26 + ord('a') ))

print("".join(decoded))
 

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
text = text.strip(".()").split() 
for l in range(len(text)):
    for i in range(len(alphabet)):
        if alphabet[i] == text[l]:
            text[l] = alphabet[26 % i+2]
print(text)
