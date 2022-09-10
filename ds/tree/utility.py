from linkedlist import create

class Utility:
    def print_tree(self, root):
        '''
        -Print the tree
        -Return: dict
        '''
        if root is None:
            print("tree is empty")
            return
        cur = root
        dictionary = {}
        queue = [root]
        while len(queue) > 0 and cur:
            cur = queue.pop(0)
            if cur.data != 'N':
                dictionary[cur.data] = []
                if cur.left:
                    dictionary[cur.data].append(cur.left.data)
                else:
                    dictionary[cur.data].append('N')
                if cur.right:
                    dictionary[cur.data].append(cur.right.data)
                else:
                    dictionary[cur.data].append('N')
            if cur.left:
                queue.append(cur.left)
                print(cur.left.data)
            if cur.right:
                print(cur.right.data)
                queue.append(cur.right)
        return dictionary
    
    def left_bt(self, root):
        '''
        Left View of Binary Tree
        Return: list
        '''
        pass

