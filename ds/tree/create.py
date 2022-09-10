class Leaf:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def tree(lis):
        lis = list(lis)
        leaf = Leaf(lis[0])
        root = leaf
        queue = [leaf]
        s = [root.data]
        i = 1
        while i < len(lis):
            leaf = queue.pop(0)
            if leaf.data != 'N':
                leaf.left = Leaf(lis[i])
                s.append(lis[i])
                queue.append(leaf.left)
                i += 1
                if i < len(lis):
                    leaf.right = Leaf(lis[i])
                    s.append(lis[i])
                    queue.append(leaf.right)
                    i += 1
        print(s)
        return root

    
    