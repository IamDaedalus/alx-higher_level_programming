#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1

    def do_calc():
        """Simple terminal calculator"""
        argc = len(sys.argv)

        if argc != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            sys.exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            op = sys.argv[2]

            match op:
                case "+":
                    print("{} {} {} = {}"
                          .format(a, op, b, calculator_1.add(a, b)))
                case "-":
                    print("{} {} {} = {}"
                          .format(a, op, b, calculator_1.sub(a, b)(a, b)))
                case "*":
                    print("{} {} {} = {}"
                          .format(a, op, b, calculator_1.mul(a, b)))
                case "/":
                    print("{} {} {} = {}"
                          .format(a, op, b, calculator_1.div(a, b)(a, b)))
                case _:
                    print("Unknown operator. Available operators: +, -, * and /")
                    sys.exit(1)

    do_calc()
