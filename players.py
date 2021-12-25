class Player():
    def __init__(self, currently_sprite, front, front_right, front_left, back, back_right, back_left, right, right_right, right_left, left, left_right, left_left, pos_x, pos_y):
        # sprites:------
        self.currently_sprite = currently_sprite
        self.front = front
        self.front_right = front_right 
        self.front_left = front_left 
        self.back = back
        self.back_right = back_right
        self.back_left = back_left
        self.right = right
        self.right_right = right_right
        self.right_left = right_left
        self.left = left
        self.left_right = left_right
        self.left_left = left_left
        # position:
        self.position = (pos_x, pos_y)