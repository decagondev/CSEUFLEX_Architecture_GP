f=open("file","rb")
# f.seek(256, 0)
num=list(f.read())
# print(len(num))
# print(f"{num[0]:02X}")
# print(f"{num[256]:02X}")
data = []
for i in range(255, len(num)):

    # print(f"{num[i]:02X}")
    data.append(num[i])
print(data[2])
f.close()