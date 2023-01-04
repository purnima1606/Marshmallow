import zipfile

# with zipfile.ZipFile("hello.zip") as z:
#     l = z.namelist()
#     c = z.getinfo(l[0])
#     print(c.file_size)
#     print(c.date_time)


with zipfile.ZipFile("hello.zip") as z:
    # z.write("zip_.py")x
    for i in z.infolist():
        print(i.file_size, i.date_time, i.compress_size)
