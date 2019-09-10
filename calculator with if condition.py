num1 = input('plz enter 1st number :')
num2 = input('plz enter 2st number :')
# read operation
op = input('plz enter operation :')
# convert operation to numbers
num1 = float(num1)
num2 = float(num2)
if op == '+' :
    res = num1+num2
    print("SUM = ",res)
elif op == '-' :
    res = num1-num2
    print("SUB = ",res)
elif op == '*' or op == 'x' or op == 'X' :
    res = num1*num2
    print("Mul = ",res)
elif op == '/' or op =='\\' :
    res = num1/num2
    print("DIV = ",res)