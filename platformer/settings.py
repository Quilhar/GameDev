# create color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MOON = (246, 241, 213)
GREY = (182, 186, 183)
DARKGREEN = (31, 77, 35)
DARKYELLOW = (188, 194, 29)
LIGHTBLUE = (29, 186, 194)
ORANGE = (255, 165, 0)
OFFGRAY = (102, 86, 86)
BRICK = (188, 74, 60)
# BG_COLOR = (175, 242, 253, 1)
BG_COLOR = BLACK




# FPS
FPS = 60


GRAVITY = 1


LAYOUTS = [["1111111111111111111111111111111111",
            "1                                1",
            "1                                1",
            "1                                1",
            "1                                1",
            "1                                1",
            "1                                1",
            "1                                1",
            "1                                1",
            "1                                1",
            "1                                1",
            "1                                1",
            "1  p    ss  b     e      b  ss   d",
            "1gggggggggggggggggggggggggggggggg1"],

           ["1111111111111111111111111111111111",
            "1                                1",
            "1                               d1",
            "1                             1111",
            "1   c  1b e  b      11   1   11  1",
            "1   1    1111   1   1            1",
            "1 1                              1",
            "1                                1",
            "1  11   s              s         1",
            "1      111  1  1   1  11         1",
            "1                        1       1",
            "1                         1      1",
            "1  p    b      eb                1",
            "1ggggg  gggggggg   gggggggggggggg1"],
           
            ["1111111111111111111111111111111111",
             "1                                1",
             "1     b e  b                     1",
             "1d      1111b    e b     c       1",
             "1111        111111 1  1 1        1",
             "1                         1      1",
             "1                           1    1",
             "1                                1",
             "1                         111    1",
             "1            s     s  11         1",
             "1      s 1  11 1  111            1",
             "1 p   111                        1",
             "1111                             1",
             "1ssssssssssssssssssssssssssssssss1"],

            ["1111111111111111111111111111111111",
             "1                                1",
             "1                               d1",
             "1                      b e  b  111",
             "1                       1111     1",
             "1                    g           1",
             "1                g   1           1",
             "1             g  1   1           1",
             "1         g   1  1   1           1",
             "1      g  1   1  1   1           1",
             "1    g 1  1   1  1   1           1",
             "1   g1 1  1   1  1   1           1",
             "1p g11s1ss1sss1ss1sss1           1",
             "1gg1111111111111111111sssssssssss1"]]
             






BRICK_WIDTH = 50
BRICK_HEIGHT = 50


PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30


ENEMY_WIDTH = 30
ENEMY_HEIGHT = 30


BARRIER_WIDTH = 50
BARRIER_HEIGHT = 50


CHECKPOINT_WIDTH = 50
CHECKPOINT_HEIGHT = 50


# display parameters
DISPLAY_WIDTH = BRICK_WIDTH * len(LAYOUTS[0][1])
DISPLAY_HEIGHT = BRICK_HEIGHT * len(LAYOUTS[0])




