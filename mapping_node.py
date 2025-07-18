from directions import Direction

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left_child = None
        self.right_child = None
        self.down_child = None
        self.up_child = None
        self.is_finish = False

    def create_child(self, direction, x, y):
        if direction == "LEFT":
            if self.left_child is not None:
                raise ValueError("Left child already exists. Cannot create another child in this direction.")
            self.left_child = Node(x, y)
            self.left_child.right_child = self
            return self.left_child
        elif direction == "RIGHT":
            if self.right_child is not None:
                raise ValueError("Right child already exists. Cannot create another child in this direction.")
            self.right_child = Node(x, y)
            self.right_child.left_child = self
            return self.right_child
        elif direction == "DOWN":
            if self.down_child is not None:
                raise ValueError("Down child already exists. Cannot create another child in this direction.")
            self.down_child = Node(x, y)
            self.down_child.up_child = self
            return self.down_child
        elif direction == "UP":
            if self.up_child is not None:
                raise ValueError("Up child already exists. Cannot create another child in this direction.")
            self.up_child = Node(x, y)
            self.up_child.down_child = self
            return self.up_child
        else:
            raise ValueError("Invalid direction. Use Direction.LEFT, Direction.RIGHT, Direction.UP, or Direction.DOWN.")

    def does_child_exist(self, direction):
        if direction == "LEFT":
            return self.left_child is not None
        elif direction == "RIGHT":
            return self.right_child is not None
        elif direction == "DOWN":
            return self.down_child is not None
        elif direction == "UP":
            return self.up_child is not None
        else:
            raise ValueError("Invalid direction. Use Direction.LEFT, Direction.RIGHT, Direction.UP, or Direction.DOWN.")


