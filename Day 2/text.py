text1 = "em tên: Mai Đình Luân/ ID: 95057"

text2 = "em tên: \"Mai Đình Luân\" \'ID: 95057"

text3 = "em tên: Mai Đình Luân \nID: 95057"

print (text1)
# em tên: Mai Đình Luân/ ID: 95057

print (text2)
# em tên: "Mai Đình Luân" 'ID: 95057

print (text3)
# em tên: Mai Đình Luân
# ID: 95057

print (r'C:\some\name')
# C:\some\name

# #########################################################################

x = 3 * "name" + "id"
y = "dja" + "ngo"
z = "mai"
k = "luan" + z

print(x)
# namenamenameid

print(y)
# django

print(k)
# luanmai

# #########################################################################

l = "dinhluan"
mai = l[-1]
dinh = l[4:8]
luan = l[5]

print(luan)
# u

print(mai)
# n

print(dinh)
# luan