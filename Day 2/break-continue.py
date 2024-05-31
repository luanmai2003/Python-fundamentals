for j in range(2,10):

    for q in range(2, j):
        if j % q == 0:
            print(j,"bằng: ", q, "*", j//q)
            break
        else:
            print(j, "là số nguyên tố!")
        # 3 là số nguyên tố!
        # 4 bằng:  2 * 2
        # 5 là số nguyên tố!
        # 5 là số nguyên tố!
        # 5 là số nguyên tố!
        # 6 bằng:  2 * 3
        # 7 là số nguyên tố!
        # 7 là số nguyên tố!
        # 7 là số nguyên tố!
        # 7 là số nguyên tố!
        # 7 là số nguyên tố!
        # 8 bằng:  2 * 4
        # 9 là số nguyên tố!
        # 9 bằng:  3 * 3

# #########################################################################

for k in range(2, 10):
    if k % 2 == 0:
        print("Đã tìm thấy số chẵn: ", k)
        continue
    print("Đã tìm thấy số lẻ: ", k)
    # Đã tìm thấy số chẵn:  2
    # Đã tìm thấy số lẻ:  3
    # Đã tìm thấy số chẵn:  4
    # Đã tìm thấy số lẻ:  5
    # Đã tìm thấy số chẵn:  6
    # Đã tìm thấy số lẻ:  7
    # Đã tìm thấy số chẵn:  8
    # Đã tìm thấy số lẻ:  9