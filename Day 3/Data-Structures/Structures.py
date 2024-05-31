fruits = ['luan', 'manh', 'nguyen', 'thoi', 'nhat', 'phuong', 'thoi']

# count: Trả về số lần x xuất hiện trong danh sách.
print(fruits.count('thoi')) # 2
print(fruits.count('manh')) # 1

# index: tìm giá trị đang ở vị trí nào
print(fruits.index('thoi')) # 3
print(fruits.index('thoi', 4)) # 6

# reverse: Đảo ngược các phần tử của danh sách tại chỗ.
fruits.reverse()
print(fruits)

# print(fruits.append('grape'))

# print(fruits.sort())

# print(fruits.pop())