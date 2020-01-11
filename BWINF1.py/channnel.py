import zipfile
num = 85503

archive = zipfile.ZipFile('/Users/alexgalkin/Downloads/channel.zip', 'r')
# for name in archive.namelist():
#     print(name)

comments = []

while True:
    with archive.open('%d.txt' % num ) as pickle_file:
        comments.append(str(archive.getinfo('%d.txt' % num).comment.decode("utf-8")))
        text = str(pickle_file.read())
        print(text)
        ploop = text.split()
        num = ploop[-1]
        print(ploop)
        num = num.strip("'")
        if not(num.isnumeric()):
            break
        num = int(num)

print("".join(comments))