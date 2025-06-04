from PIL import Image


class Map:
    def __init__(self, image_path):
        self.width = None
        self.height = None
        self.grid = None
        self.start = None
        self.finish = []
        self.load_from_image(image_path)

    def load_from_image(self, image_path):
        # Load map from image with white being 0 (empty space), black being 1 (wall),
        # green being the starting point, and red being the finish area.
        img = Image.open(image_path).convert('RGB')
        self.width, self.height = img.size
        self.grid = [[0 for _ in range(self.height)] for _ in range(self.width)]

        for x in range(self.width):
            for y in range(self.height):
                pixel = img.getpixel((x, y))
                if pixel == (255, 255, 255):  # White
                    self.grid[x][y] = 0
                elif pixel == (0, 0, 0):  # Black
                    self.grid[x][y] = 1
                elif pixel == (0, 255, 0):  # Green
                    self.start = (x, y)
                elif pixel == (255, 0, 0):  # Red
                    self.finish.append((x, y))

        img.close()

    def display_map(self):
        for y in range(self.height):
            print(' '.join(['#' if self.grid[x][y] == 1 else '.' for x in range(self.width)]))
        print(f"Map size: {self.width}x{self.height}")
        print(f"Starting point: {self.start}")
        print(f"Finish area: {self.finish}")

    def get_start(self):
        return self.start

    def is_in_finish(self, x, y):
        return (x, y) in self.finish