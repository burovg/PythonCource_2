try:
    num1 = int(raw_input("Enter first number"))
    num2 = int(raw_input("Enter second number"))
    print num1/num2
except ValueError as e:
    print "Value error"
    print str(e)
except ZeroDivisionError as e1:
    print "Divide by zero"
    print str(e1)
finally:
    print "Continue"

