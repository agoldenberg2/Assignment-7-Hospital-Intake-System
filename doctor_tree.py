class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None
    def insert(self, parent_name, doctor_name, side, current_node=None):
        if self.root is None:
            return

        if side not in ["left", "right"]:
            print("Invalid side")
            return

        if current_node is None:
            current_node = self.root

        if current_node.name == parent_name:
            if getattr(current_node, side) is None:
                setattr(current_node, side, DoctorNode(doctor_name))
            else:
                print("That position is already taken")
            return

        if current_node.left:
            self.insert(parent_name, doctor_name, side, current_node.left)

        if current_node.right:
            self.insert(parent_name, doctor_name, side, current_node.right)
    def preorder(self, node):
        if node is None:
            return []

        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result

    def inorder(self, node):
        if node is None:
            return []

        result = []
        result += self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)
        return result

    def postorder(self, node):
        if node is None:
            return []

        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)
        return result

# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print("Preorder:", tree.preorder(tree.root))
print("Inorder:", tree.inorder(tree.root))
print("Postorder:", tree.postorder(tree.root))

tree.insert("Dr. Smith", "Dr. Lee", "left")
tree.insert("Dr. Croft", "Dr. Lee", "middle")