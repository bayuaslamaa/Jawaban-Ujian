def cek_kata(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] = 1
        else:
            counts[word] = 1

    return counts

print(len(cek_kata("ini adalah sebuah kata")),"/4")
print(len(cek_kata("2pasang sandal hilang")),"/4")
