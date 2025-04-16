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
BG_COLOR = (175, 242, 253, 1)
SCALEFACTOR = 2
TILESIZE = 16 * SCALEFACTOR


# FPS
FPS = 60

GRAVITY = 1


LAYOUTS = [["1111111111111111111111111111111111111111111111111",
            "1    00                                         1",
            "1    00                                         1",
            "1    00                                         1",
            "1    000                                        1",
            "1     000                                       1",
            "1      0000                                     1",
            "1       0000                                    1",
            "1        00000                                  1",
            "1         00000                                 1",
            "1          00000000000000000000000000000000000001",
            "1           0000000000000000000000000000000000001",
            "1            000000                             1",
            "1             000000                            1",
            "1              000000                           1",
            "1               000000                          1",
            "1                0000000                        1",
            "1                 0000000                       1",
            "1                  0000000                      1",
            "1                   0000000                     1",
            "1                    0000000                    1",
            "1                     0000000                   1",
            "1                      0000000                  1",
            "1111111111111111111111111111111111111111111111111"]]



# display parameters
DISPLAY_WIDTH = 30 * TILESIZE 
DISPLAY_HEIGHT = 20 * TILESIZE 

MAP_WIDTH = 30 * TILESIZE 
MAP_HEIGHT = 20 * TILESIZE 

print(MAP_WIDTH, MAP_HEIGHT)

# DISPLAY_WIDTH = len(LAYOUTS[0][0]) * TILESIZE 
# DISPLAY_HEIGHT = len(LAYOUTS[0]) * TILESIZE 
