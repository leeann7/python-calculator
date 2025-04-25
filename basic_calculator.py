operator = input("What operator would you like to use? (+ - * /)")

num1 = float(input("First number?"))
num2 = float(input("Second number?"))

if operator == "+":
    res = num1+num2
    print("result is: ", round(res, 3))
elif operator == "-":
    res = num1-num2
    print("result is: ", round(res,3))
elif operator == "*":
    res = num1*num2
    print("result is: ", round(res,3))
elif operator == "/":
    res = num1/num2
    print("result is: ", round(res,3))
else:
    print("you typed: ", operator)
    print("unfort. that operator makes no sense :(")