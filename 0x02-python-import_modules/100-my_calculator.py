0x02-python-import_modules
================================

0-add.py


#!/usr/bin/python3
if _name_ == '_main_':
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))

____________________________________________________________

0-import_add.py


_import_("0-add")


____________________________________________________________

1-calculation.py
#!/usr/bin/python3
if _name_ == '_main_':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))


____________________________________________________________


100-my_calculator.py


#!/usr/bin/python3
if _name_ == "_main_":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv[1:]
    argv_count = len(argv)
    operators = ["+", "-", "*", "/"]
    if argv_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif sys.argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))



