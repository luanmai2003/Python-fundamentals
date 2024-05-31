number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = ["mai", "dinh", "luan"]

for i in number:
    print(i)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10

for i in text:
    print(i, len(i))
    # mai 3
    # dinh 4
    # luan 4

# #########################################################################

users = {"luan": "18 tuổi", "dong": "12 tuổi", "hieu": "9 tuổi", "thu": "18 tuổi"}

for user, status in users.copy().items():
    if status == "9 tuổi":
        del users[user]
        print(users)
        # {'luan': '18 tuổi', 'dong': '12 tuổi', 'thu': '18 tuổi'}

users2 = {}
for user, status in users.items():
    if status == "18 tuổi":
        users2[user] = status
        print("những người trên 18 tuổi: ", users2)
        # những người trên 18 tuổi:  {'luan': '18 tuổi'}
        # những người trên 18 tuổi:  {'luan': '18 tuổi', 'thu': '18 tuổi'}

# #########################################################################

for i in range(6):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5

print("lap tu 2 den 4:", list(range(2, 5)))
# lap tu 2 den 4: [2, 3, 4]

print("lap tu 2 den 4:", list(range(2, 5, 2)))
# lap tu 2 den 4: [2, 4]

# #########################################################################

abc = ["nam", "nay", "con", "bao", "nhieu", "tuoi"]
for i in range(len(abc)):
    print(i, abc[i])
    # 0 nam
    # 1 nay
    # 2 con
    # 3 bao
    # 4 nhieu
    # 5 tuoi

# #########################################################################

acb = sum(range(5))

print("tong", acb) # 0 + 1 + 2 + 3 + 4
# 10