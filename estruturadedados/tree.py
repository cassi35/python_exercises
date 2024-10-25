class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []
        self.parent = None
    def add_child(self,child):
        self.children.append(child)
    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
def buld_product_tree():
    root = TreeNode("eletronics")
    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("mac"))
    laptop.add_child(TreeNode("surface"))
    laptop.add_child(TreeNode("thinkpad"))
    celphone = TreeNode("celphone")
    celphone.add_child(TreeNode("iphone"))
    celphone.add_child(TreeNode("google pixel"))
    celphone.add_child(TreeNode("vivo"))
    tv = TreeNode("tv")
    tv.add_child(TreeNode("samsumg"))
    tv.add_child(TreeNode("lg"))
    root.add_child(laptop)
    root.add_child(celphone)
    root.add_child(tv)

    return root
if __name__ == '__main__':
    root = buld_product_tree()
    root.print_tree()
    pass