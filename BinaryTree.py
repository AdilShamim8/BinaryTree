
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * (4 * self.get_level())
        prefix = spaces + "|___" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    @staticmethod
    def build_product_tree():
        root = TreeNode("Nilpul (CEO)")

        cto = TreeNode("Chinmoy (CTO)")
        infra_head = TreeNode("Vishwa (Infrastructure Head)")
        infra_head.add_child(TreeNode("Dhaval (Cloud Manager)"))
        infra_head.add_child(TreeNode("Abhijit (App Manager)"))
        app_head = TreeNode("Aamir (Application Head)")

        hr_head = TreeNode("Gels (HR Head)")
        hr_head.add_child(TreeNode("Peter (Recruitment Manager)"))
        hr_head.add_child(TreeNode("Waqas (Policy Manager)"))

        root.add_child(cto)
        root.add_child(infra_head)
        root.add_child(app_head)
        root.add_child(hr_head)

        root.print_tree()


if __name__ == '__main__':
    TreeNode.build_product_tree()























class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()