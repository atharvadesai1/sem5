def binary(a, b):
    a1 = abs(a)
    b1 = abs(b)
    com = [1, 0, 0, 0, 0, 0, 0, 0]
    anum = [0] * 8
    anumcp = [0] * 8
    bnum = [0] * 8
    acomp = [0] * 8
    bcomp = [0] * 8
    pro = [0] * 8
    res = [0] * 8
    for i in range(8):
        r = a1 % 2
        a1 = a1 // 2
        r2 = b1 % 2
        b1 = b1 // 2
        anum[i] = r
        anumcp[i] = r
        bnum[i] = r2
        if r2 == 0:
            bcomp[i] = 1
        if r == 0:
            acomp[i] = 1
    c = 0
    for i in range(8):
        res[i] = com[i] + bcomp[i] + c
        if res[i] >= 2:
            c = 1
        else:
            c = 0
        res[i] = res[i] % 2
        bcomp[i] = res[i]

    if a < 0:
        c = 0
        for i in range(8):
            res[i] = 0
        for i in range(8):
            res[i] = com[i] + acomp[i] + c
            if res[i] >= 2:
                c = 1
            else:
                c = 0
            res[i] = res[i] % 2
            anum[i] = res[i]
            anumcp[i] = res[i]
    if b < 0:
        for i in range(8):
            temp = bnum[i]
            bnum[i] = bcomp[i]
            bcomp[i] = temp
    return anum, bnum, bcomp, pro, anumcp

def add(num, pro, anumcp):
    res = [0] * 8
    c = 0
    for i in range(8):
        res[i] = pro[i] + num[i] + c
        if res[i] >= 2:
            c = 1
        else:
            c = 0
        res[i] = res[i] % 2
        pro[i] = res[i]
    return pro, anumcp

def arshift(pro, anumcp):
    temp = pro[7]
    temp2 = pro[0]
    for i in range(1, 8):
        pro[i - 1] = pro[i]
    pro[7] = temp
    for i in range(1, 8):
        anumcp[i - 1] = anumcp[i]
    anumcp[7] = temp2
    return pro, anumcp

def booth_multiplication(a, b):
    anum, bnum, bcomp, pro, anumcp = binary(a, b)
    q = 0
    result = []
    for i in range(8):
        if anum[i] == q:
            result.append(pro)
            pro, anumcp = arshift(pro, anumcp)
            q = anum[i]
        elif anum[i] == 1 and q == 0:
            result.append(pro)
            pro, anumcp = add(bcomp, pro, anumcp)
            pro, anumcp = arshift(pro, anumcp)
            q = anum[i]
        else:
            result.append(pro)
            pro, anumcp = add(bnum, pro, anumcp)
            pro, anumcp = arshift(pro, anumcp)
            q = anum[i]
    final_product = [0] * 16
    for i in range(8):
        final_product[i] = anumcp[i]
    for i in range(8, 16):
        final_product[i] = result[-1][i - 8]
    return final_product

if __name__ == "__main__":
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    if abs(a) > 255 or abs(b) > 255:
        print("Both numbers must be integers in the range (-256 to 255).")
    else:
        result = booth_multiplication(a, b)
        print("\nProduct is =", end=" ")
        for i in reversed(result):
            print(i, end="")
        print()