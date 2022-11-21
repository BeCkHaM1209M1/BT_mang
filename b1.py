def so_nguyen_to(S):
    lst_so_nguyen_to = []
    number_inS = []
    i = 0

    #Lay cac so co trong chuoi
    while i < len(S):
        if len(S)-i == 0:
            break
        elif 47 < ord(S[i]) < 58:
            strings = ""
            strings += S[i]
            for j in range(i+1, len(S)):
                if 47 < ord(S[j]) < 58:
                    strings += S[j]
                else:
                    i = j+1
                    break
            number_inS.append(int(strings))
        else:
            i += 1

    #check so nguyen to
    flag = 1
    for n in number_inS:
        if (n < 2):
            flag = 0
        for p in range(2, n):
            if n % p == 0:
                flag = 0
        if flag == 1:
            lst_so_nguyen_to.append(n)
    print(
        f"Cac so nguyen to trong chuoi la : {','.join([str(i) for i in lst_so_nguyen_to])}")


so_nguyen_to('s3oe2oea15pea9')
