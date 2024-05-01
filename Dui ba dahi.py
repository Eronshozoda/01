def BinariNumber2To10(number):
    cnt=0
    binary=0
    one_number=0
    while number>0:
        one_number=number%10
        binary+=one_number*2**cnt
        cnt+=1
        number//=10
    return binary
num = int(input())
print(BinariNumber2To10(num))