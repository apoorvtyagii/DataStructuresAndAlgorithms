import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)


from linkedlist import create, utility
import random 


class Main:
    def __init__(self, lis):
        self.lis = lis

    def main(self):
        head = create.LinkedList.linked_list(self.lis)
        print(head.data)
        uti = utility.Utility()
        print(uti.print_linked_list(head))
        reversed_head = uti.complete_reverse(head)
        print(uti.print_linked_list(reversed_head))



if __name__ == "__main__":
    # number of test cases
    n = 1
    for i in range(n):
        # len of a list
        m = 6
        lis = [random.randint(0,22) for _ in range(m)]
        m = Main(lis)
        m.main()

