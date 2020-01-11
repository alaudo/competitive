import math
import urllib.request
num = "62381"
while True:
    response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+num)
    html = response.read()
    pups = str(html).split()
    num = pups[-1][0:-1]
    print(html)
    if num.isnumeric():
        continue
    else:
        break
print(num)