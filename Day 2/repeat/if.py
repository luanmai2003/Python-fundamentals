x = int(input("Điểm trung bình của học sinh: "))

if x == 0:
    print('Rớt phải thi lại!')
elif x <= 3:
    print('Học sinh yếu')
elif 4 <= x <= 6:
    print('Học sinh trung bình')
elif 7 <= x <= 8:
    print('Học sinh tiên tiến')
elif 9 <= x <= 10:
    print('Học sinh giỏi')
else:
    print('bạn đã nhập sai điểm')