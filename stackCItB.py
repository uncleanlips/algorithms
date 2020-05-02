from stack import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        r = dec_num % 2
        s.Push(r)
        dec_num = dec_num // 2

    bin_num = ''
    while  not s.isEmpty():
        bin_num += str(s.Pop())

    return bin_num

print(div_by_2(242))
