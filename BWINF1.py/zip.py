import zipfile
archive = zipfile.ZipFile(r'D:\XXX\Desktop\MyZip.zip', 'r')
print(archive.getinfo("firstobj.1").comment)