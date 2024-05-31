def ask_ok(prompt, retries=2, reminder='Please try again!'):
    # prompt: (string) dùng để hiển thị thông báo cho người dùng.yêu cầu người dùng nhập câu trả lời (yes/no).
    # retries: Nó xác định số lần người dùng có thể thử lại nếu họ không nhập đúng câu trả lời.
    # reminder: Là tham số tùy chọn mặc định là “Please try again!”. Hiển thị nếu người dùng nhập sai.
    while True:
        reply = input(prompt)
        if reply in {'y', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok('Do you really want to quit?')

# #########################################################################

i = 5
def f(arg=i):
    print(arg)

i = 6
f()

# #########################################################################

def f0(a, L=[]):
    L.append(a)
    return L
print(f0(int(input("number: "))))


def f(a, L=[]):
    L.append(a)
    return L
print(f(2))
print(f(3))


def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f2(5))