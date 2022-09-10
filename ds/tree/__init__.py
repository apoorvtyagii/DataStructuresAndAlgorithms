import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)


from tree import create, utility
import random 


class Main:
    def __init__(self, lis):
        self.lis = lis

    def main(self):
        head = create.Tree.tree(self.lis)
        print(self.lis)
        print(head.data)
        uti = utility.Utility()
        print(uti.print_tree(head))



if __name__ == "__main__":
    # number of test cases
    n = 1
    for i in range(n):
        # len of a list
        m = 8
        sett = (0, 1, 3, 4, 5, 6, 7, 9)
        lis = [3, 4, 'N', 2, 7, 'N', 2, 1, 'N', 9, 1]
        lis = [1, 2, 3, 'N', 'N', 4, 6, 'N', 5, 'N', 'N' ,7, 'N']
        # while len(sett) < m:
        #     sett.add(random.randint(0,9))
        m = Main(lis)
        m.main()

