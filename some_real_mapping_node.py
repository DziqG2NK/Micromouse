from directions import Direction

class Node:
    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.down_child = None
        self.up_child = None

    def create_child(self, direction):
        if direction == Direction.LEFT:
            if self.left_child is not None:
                raise ValueError("Left child already exists. Cannot create another child in this direction.")
            self.left_child = Node()
            self.left_child.right_child = self
            return self.left_child
        elif direction == Direction.RIGHT:
            if self.right_child is not None:
                raise ValueError("Right child already exists. Cannot create another child in this direction.")
            self.right_child = Node()
            self.right_child.left_child = self
            return self.right_child
        elif direction == Direction.DOWN:
            if self.down_child is not None:
                raise ValueError("Down child already exists. Cannot create another child in this direction.")
            self.down_child = Node()
            self.down_child.up_child = self
            return self.down_child
        elif direction == Direction.UP:
            if self.up_child is not None:
                raise ValueError("Up child already exists. Cannot create another child in this direction.")
            self.up_child = Node()
            self.up_child.down_child = self
            return self.up_child
        else:
            raise ValueError("Invalid direction. Use Direction.LEFT, Direction.RIGHT, Direction.UP, or Direction.DOWN.")

    def does_child_exist(self, direction):
        if direction == Direction.LEFT:
            return self.left_child is not None
        elif direction == Direction.RIGHT:
            return self.right_child is not None
        elif direction == Direction.DOWN:
            return self.down_child is not None
        elif direction == Direction.UP:
            return self.up_child is not None
        else:
            raise ValueError("Invalid direction. Use Direction.LEFT, Direction.RIGHT, Direction.UP, or Direction.DOWN.")
