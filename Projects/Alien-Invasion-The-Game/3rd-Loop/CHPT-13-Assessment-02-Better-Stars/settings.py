class Settings():
    """Store game settings and variables"""

    def __init__(self):
        """Init game settings and variables"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.caption = "CHPT-13-Assessment-02: Better Stars"
        self.bg_color = (40, 40, 40)

        # Star settings
        self.star_spacing_factor = 3
        self.star_displacement_factor = (-30, 30)
