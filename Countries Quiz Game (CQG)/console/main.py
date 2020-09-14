import learn_mode as lm
import practice_mode as pm
from sys import exit
import temp


def mode():
    temp.clear()
    print("Enter")
    print("1 : for practice mode")
    print("2 : for learning mode")
    n = temp.choices_to_n(1,2)
    return int(n)


def again():
    print("Do you want to enter new mode?\n")
    return temp.again()


if __name__ == '__main__':
    Continue = True
    while Continue:
        mode_ = mode()
        if mode_ == 1:
            pm.main()
        else:
            lm.main()
        Continue = again()
    print("thanks!")
    exit()