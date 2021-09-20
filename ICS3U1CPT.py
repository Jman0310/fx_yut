##
# This program is a remake of the classic Korean board game 'Yut', created with FX designs and
# themes. 
# @author Ian Chen, Jaiman Patel
# @course ICS3U
# @date 2018/06/15
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
# Import
import pygame
import math
import random

# Start pygame
pygame.init()

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
darkred = (100, 0, 0)
blue = (0, 0, 255)
darkblue = (0, 0, 75)
yellow = (255, 215, 0)
lightbrown = (210, 105, 30)

# Board class
class Board():
    def __init__(self):
        self.space_start = (729, 558)
        self.space_up1 = (728,454)
        self.space_up2 = (729, 373)
        self.space_up3 = (730, 290)
        self.space_up4 = (727, 206)
        self.space_topright = (727, 104)
        self.space_left1 = (638, 109)
        self.space_left2 = (554, 109)
        self.space_left3 = (469, 109)
        self.space_left4 = (383, 108)
        self.space_topleft = (289, 105)
        self.space_down1 = (288, 204)
        self.space_down2 = (288, 291)
        self.space_down3 = (288, 373)
        self.space_down4 = (289, 460)
        self.space_bottomleft = (289, 551)
        self.space_right1 = (384, 560)
        self.space_right2 = (470, 559)
        self.space_right3 = (556, 559)
        self.space_right4 = (639, 559)
        self.space_rightdowndiag1 = (364, 190)
        self.space_rightdowndiag2 = (438, 268)
        self.space_leftdowndiag1 = (664, 188)
        self.space_leftdowndiag2 = (590, 261)
        self.space_center = (512, 338)
        self.space_rightdowndiag3 = (589, 414)
        self.space_rightdowndiag4 = (664, 489)
        self.space_leftdowndiag3 = (439, 415)
        self.space_leftdowndiag4 = (364, 493)
        self.space_listnorm = [self.space_start,self.space_up1,self.space_up2,self.space_up3,self.space_up4,self.space_topright,
                           self.space_left1,self.space_left2,self.space_left3,self.space_left4,self.space_topleft,
                           self.space_down1,self.space_down2,self.space_down3,self.space_down4,self.space_bottomleft,
                           self.space_right1,self.space_right2,self.space_right3,self.space_right4]
        self.space_listleftdown = [self.space_topright,self.space_leftdowndiag1,self.space_leftdowndiag2,
                                   self.space_center,
                                   self.space_leftdowndiag3,self.space_leftdowndiag4]
        self.space_listrightdown = [self.space_topleft,self.space_rightdowndiag1,self.space_rightdowndiag2,
                                    self.space_center,
                                    self.space_rightdowndiag3,self.space_rightdowndiag4]
        
# Piece class
class Piece(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("stfx_logo.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.place = 0
        self.turn = True
        self.flipped = False
        self.winner = False
        self.senthome = False
    def pos(self):
        self.rect.x = 0
        self.rect.y = 0

        
# Stick class
class Stick(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.flipped = False
    def draw(self):
        self.image = pygame.image.load("yut_stick_front.png").convert()
        self.image.set_colorkey(white)
        screen.blit(self.image,[self.x,self.y])
    def drop(self):
        self.num = int(random.randint(1,5))

# Game class which allows program to restart after a game
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.end = False
        self.restart = False
        self.clicked = False
        self.image = pygame.image.load("reset.png").convert()
        self.rect = self.image.get_rect()
    def pos(self):
        self.rect.x = 0
        self.rect.y = 0
        
# List of sprites
piece_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# Set the width and height of the screen [width, height]
size = (1080, 720)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("FX Yut")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Player 1 piece starting location and values
p1_piece = Piece()
p1_piece.rect.x = 20
p1_piece.rect.y = 600
p1_piece.turn = True
p1_piece.flipped = False
p1_piece.winner = False
p1_piece.senthome = False
piece_list.add(p1_piece)
all_sprites_list.add(p1_piece)

# Player 2 piece starting location and values
p2_piece = Piece()
p2_piece.rect.x = 1000
p2_piece.rect.y = 600
p2_piece.image = pygame.image.load("stfx_logo2.png").convert()
p2_piece.image.set_colorkey(white)
p2_piece.turn = False
p2_piece.flipped = False
p2_piece.winner = False
p2_piece.senthome = False
piece_list.add(p2_piece)
all_sprites_list.add(p2_piece)


# Stick instance    
stick = Stick()
stick.num = 0
stick.x = 75
stick.y = 250
stick.flipped = True
stick2 = Stick()
stick2.image = pygame.image.load("yut_stick_back.png").convert()
stick2.image.set_colorkey(black)
stick2.x = 3000
stick2.y = 3000
stick2.flipped = False

# Calling the board
board = Board()

# Mouse input
handled = False

# Game instance and reset button
game = Game()
game.rect.x = 500
game.rect.y = 675
all_sprites_list.add(game)

# Background image
background_image = pygame.image.load("tiger.png").convert()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.end == False:
                if p1_piece.turn == True and p1_piece.flipped == False and stick.flipped == True:
                    stick.drop()
                    stick.x = 3000
                    stick.y = 3000
                    stick2.x = 79
                    stick2.y = 270
                    p1_piece.flipped = True
                    stick.flipped = False
                    stick2.flipped = True
                elif p2_piece.turn == True and p2_piece.flipped == False and stick.flipped == True:
                    stick.drop()
                    stick.x = 3000
                    stick.y = 3000
                    stick2.x = 79
                    stick2.y = 270
                    p2_piece.flipped = True
                    stick.flipped = False
                    stick2.flipped = True

        # Player 1s piece
        # Adapted from https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
        elif pygame.mouse.get_pressed()[0] and p1_piece.rect.collidepoint(pygame.mouse.get_pos()) and not handled and stick.num != 0 and p1_piece.turn and game.end == False and p1_piece.flipped == True:
            # Manipulate piece depending on input
            if p1_piece.place <= 20:
                # Land in top right
                if (p1_piece.rect.x, p1_piece.rect.y) == board.space_topright:
                    p1_piece.place = 0
                    p1_piece.place += stick.num
                    (p1_piece.rect.x, p1_piece.rect.y) = board.space_listleftdown[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_leftdowndiag1:
                    if stick.num == 5:
                        p1_piece.place = 15
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                    else:
                        p1_piece.place = 1
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listleftdown[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_leftdowndiag2:
                    if stick.num >= 4:
                        p1_piece.place = 11
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                    else:
                        p1_piece.place = 2
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listleftdown[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_leftdowndiag3:
                    if stick.num >= 2:
                        p1_piece.place = 13
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                    else:
                        p1_piece.place = 4
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listleftdown[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_leftdowndiag4:
                    p1_piece.place = 14
                    p1_piece.place += stick.num
                    (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                # Land in top left
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_topleft:
                    p1_piece.place = 0
                    p1_piece.place += stick.num
                    (p1_piece.rect.x, p1_piece.rect.y) = board.space_listrightdown[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_rightdowndiag1:
                    if stick.num >= 5:
                        p1_piece.place = 0
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                        p1_piece.winner = True
                        game.end = True
                    else:
                        p1_piece.place = 1
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listrightdown[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_rightdowndiag2:
                    if stick.num >= 4:
                        p1_piece.place = 0
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                        p1_piece.winner = True
                        game.end = True
                    else:
                        p1_piece.place = 2
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listrightdown[p1_piece.place]
                # Land in the center
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_center:
                    if stick.num >= 3:
                        p1_piece.place = 0
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                        p1_piece.winner = True
                        game.end = True
                    else:
                        p1_piece.place = 3
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listrightdown[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_rightdowndiag3:
                    if stick.num >= 2:
                        p1_piece.place = 0
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                        p1_piece.winner = True
                        game.end = True
                    else:
                        p1_piece.place = 4
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listrightdown[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_rightdowndiag4:
                    p1_piece.place = 0
                    (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                    p1_piece.winner = True
                    game.end = True
                # Land in bottom left
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_bottomleft:
                    if stick.num >= 5:
                        p1_piece.place = 0
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                        p1_piece.winner = True
                        game.end = True
                    else:
                        p1_piece.place = 15
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_right1:
                    if stick.num >= 4:
                        p1_piece.place = 0
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                        p1_piece.winner = True
                        game.end = True
                    else:
                        p1_piece.place = 16
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_right2:
                    if stick.num >= 3:
                        p1_piece.place = 0
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                        p1_piece.winner = True
                        game.end = True
                    else:
                        p1_piece.place = 17
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_right3:
                    if stick.num >= 2:
                        p1_piece.place = 0
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                        p1_piece.winner = True
                        game.end = True
                    else:
                        p1_piece.place = 18
                        p1_piece.place += stick.num
                        (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                elif (p1_piece.rect.x, p1_piece.rect.y) == board.space_right4:
                    p1_piece.place = 0
                    (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
                    p1_piece.winner = True
                    game.end = True
                # Regular pathing
                else:
                    p1_piece.place += stick.num
                    (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
            handled = pygame.mouse.get_pressed()[0]

            # Switch turns
            p1_piece.turn = False
            p2_piece.turn = True
            p1_piece.flipped = True
            p2_piece.flipped = False
            stick.flipped = True
            stick2.flipped = False
        # Player 2s piece
        elif pygame.mouse.get_pressed()[0] and p2_piece.rect.collidepoint(pygame.mouse.get_pos()) and not handled and stick.num != 0 and p2_piece.turn and game.end == False and p2_piece.flipped == True:
            # Manipulate piece depending on input
            if p2_piece.place <= 20:
                # Land in top right
                if (p2_piece.rect.x, p2_piece.rect.y) == board.space_topright:
                    p2_piece.place = 0
                    p2_piece.place += stick.num
                    (p2_piece.rect.x, p2_piece.rect.y) = board.space_listleftdown[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_leftdowndiag1:
                    if stick.num == 5:
                        p2_piece.place = 15
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
                    else:
                        p2_piece.place = 1
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listleftdown[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_leftdowndiag2:
                    if stick.num >= 4:
                        p2_piece.place = 11
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
                    else:
                        p2_piece.place = 2
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listleftdown[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_leftdowndiag3:
                    if stick.num >= 2:
                        p2_piece.place = 13
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
                    else:
                        p2_piece.place = 4
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listleftdown[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_leftdowndiag4:
                    p2_piece.place = 14
                    p2_piece.place += stick.num
                    (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
                # Land in top left
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_topleft:
                    p2_piece.place = 0
                    p2_piece.place += stick.num
                    (p2_piece.rect.x, p2_piece.rect.y) = board.space_listrightdown[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_rightdowndiag1:
                    if stick.num >= 5:
                        p2_piece.place = 0
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]                      
                        p2_piece.winner = True
                        game.end = True
                    else:
                        p2_piece.place = 1
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listrightdown[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_rightdowndiag2:
                    if stick.num >= 4:
                        p2_piece.place = 0
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]                        
                        p2_piece.winner = True
                        game.end = True
                    else:
                        p2_piece.place = 2
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listrightdown[p2_piece.place]
                # Land in the center
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_center:
                    if stick.num >= 3:
                        p2_piece.place = 0
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]                        
                        p2_piece.winner = True
                        game.end = True
                    else:
                        p2_piece.place = 3
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listrightdown[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_rightdowndiag3:
                    if stick.num >= 2:
                        p2_piece.place = 0
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]                        
                        p2_piece.winner = True
                        game.end = True
                    else:
                        p2_piece.place = 4
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listrightdown[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_rightdowndiag4:
                    p2_piece.place = 0
                    (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]                  
                    p2_piece.winner = True
                    game.end = True
                # Land in bottom left
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_bottomleft:
                    if stick.num >= 5:
                        p2_piece.place = 0
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]                        
                        p2_piece.winner = True
                    else:
                        p2_piece.place = 15
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_right1:
                    if stick.num >= 4:
                        p2_piece.place = 0
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]                        
                        p2_piece.winner = True
                        game.end = True
                    else:
                        p2_piece.place = 16
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_right2:
                    if stick.num >= 3:
                        p2_piece.place = 0
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]  
                        p2_piece.winner = True
                        game.end = True
                    else:
                        p2_piece.place = 17
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_right3:
                    if stick.num >= 2:
                        p2_piece.place = 0
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
                        p2_piece.winner = True
                        game.end = True
                    else:
                        p2_piece.place = 18
                        p2_piece.place += stick.num
                        (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
                elif (p2_piece.rect.x, p2_piece.rect.y) == board.space_right4:
                    p2_piece.place = 0
                    (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]                    
                    p2_piece.winner = True
                    game.end = True
                # Regular pathing
                else:
                    p2_piece.place += stick.num
                    (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
            handled = pygame.mouse.get_pressed()[0]
            p1_piece.turn = True
            p2_piece.turn = False
            p1_piece.flipped = False
            p2_piece.flipped = True
            stick.flipped = True
            stick2.flipped = False
        # Restarting the game
        elif pygame.mouse.get_pressed()[0] and game.rect.collidepoint(pygame.mouse.get_pos()) and not handled and game.end == True:
            game.clicked = True
        else:
            handled = False
    # --- Game logic should go here

    # Restarting game
    if game.end == True and game.clicked == True:
        p1_piece.rect.x = 20
        p1_piece.rect.y = 600
        p1_piece.turn = True
        p1_piece.winner = False
        p1_piece.flipped = False
        p1_piece.place = 0

        p2_piece.rect.x = 1000
        p2_piece.rect.y = 600
        p2_piece.turn = False
        p2_piece.winner = False
        p2_piece.flipped = False
        p2_piece.place = 0

        game.end = False
        game.clicked = False
        stick.flipped = True
        stick2.flipped = False
        
    # Evaluate player turn
    if p2_piece.turn == True:
        piece_collided = pygame.sprite.collide_rect(p1_piece, p2_piece)
        if piece_collided == True:
            p2_piece.place = 0
            (p2_piece.rect.x, p2_piece.rect.y) = board.space_listnorm[p2_piece.place]
            p2_piece.senthome = True
    elif p1_piece.turn == True:
        piece_collided = pygame.sprite.collide_rect(p2_piece, p1_piece)
        if piece_collided == True:
            p1_piece.place = 0
            (p1_piece.rect.x, p1_piece.rect.y) = board.space_listnorm[p1_piece.place]
            p1_piece.senthome = True
            
    # Evaluate stick orientation
    if stick.flipped == True:
        stick.x = 75
        stick.y = 250
        stick2.x = 3000
        stick2.y = 3000
    # --- Screen-clearing code goes here
 
    screen.fill(white)
    
    # --- Drawing code should go here
    
    # Drawing Background
    screen.blit(background_image,[0,0])
    
    # Draw board and UI
    pygame.draw.rect(screen,lightbrown,[240,60,600,600])
    pygame.draw.rect(screen,darkblue,[240,60,600,600],5)
    pygame.draw.rect(screen,yellow,[250,70,580,580],5)
    pygame.draw.ellipse(screen,darkblue,[725,550,70,70])
    font_home = pygame.font.SysFont('Calibri', 25, True, False)
    text_home = font_home.render("HOME",True,white)
    screen.blit(text_home, [725, 575])
    pygame.draw.ellipse(screen,yellow,[725,100,70,70])
    pygame.draw.ellipse(screen,yellow,[285,100,70,70])
    pygame.draw.ellipse(screen,yellow,[285,550,70,70])
    x_offset1=75
    y_offset1=75
    x_offset2=75
    y_offset2=75
    for i in range(0,200,40):
        x_offset1+=75
        y_offset1+=75
        pygame.draw.ellipse(screen,black,[220+x_offset1,45+y_offset1,50,50],5)
    for i in range(0,200,40):
        x_offset2+=75
        y_offset2+=75
        pygame.draw.ellipse(screen,black,[820-x_offset2,45+y_offset2,50,50],5)
    pygame.draw.ellipse(screen,yellow,[510,335,70,70])
    for y_offset in range(0,320,85):
        pygame.draw.ellipse(screen,black,[735,465-y_offset,50,50],5)
    for x_offset in range(0,320,85):
        pygame.draw.ellipse(screen,black,[390+x_offset,115,50,50],5)
    for y_offset in range(0,320,85):
        pygame.draw.ellipse(screen,black,[295,210+y_offset,50,50],5)
    for x_offset in range(0,320,85):
        pygame.draw.ellipse(screen,black,[390+x_offset,565,50,50],5)
    pygame.draw.rect(screen,darkred,[10,590,80,80])
    pygame.draw.rect(screen,red,[10,590,80,80],5)
    pygame.draw.rect(screen,darkblue,[990,590,80,80])
    pygame.draw.rect(screen,blue,[990,590,80,80],5)
    # Display player turn
    pygame.draw.rect(screen,yellow,[875,340,170,45])
    if p1_piece.turn == True:
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Player 1s Turn ", True,red)
        screen.blit(text, [885,350])
    else:
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Player 2s Turn ", True,blue)
        screen.blit(text, [885,350])    

    # Draw all sprites
    all_sprites_list.draw(screen)

    # Draw stick
    stick.draw()
    screen.blit(stick2.image, [stick2.x,stick2.y])
    font2 = pygame.font.SysFont('Calibri', 50, True, False)
    stick_number = font2.render("0",True,black)
    if stick.num == 1:
        stick_number = font2.render("1",True,black)
    elif stick.num == 2:
        stick_number = font2.render("2",True,black)
    elif stick.num == 3:
        stick_number = font2.render("3",True,black)
    elif stick.num == 4:
        stick_number = font2.render("4",True,black)
    elif stick.num == 5:
        stick_number = font2.render("5",True,black)
    if stick2.flipped == True:
        screen.blit(stick_number, [110,370])
    
    # Display rules
    pygame.draw.rect(screen,yellow,[0,0,1080,55])
    font3 = pygame.font.SysFont('Calibri', 18, True, False)
    text1 = font3.render("RULES:",True,black)
    text2 = font3.render("1) Player 1 is RED and Player 2 is BLUE.",True,black)
    text3 = font3.render("2) When it is your turn, press 'space' to flip the stick.",True,black)
    text4 = font3.render("3) If you land on a yellow corner tile, you will be able to cut across the middle.",True,black)
    text5 = font3.render("4) The objective is to get back to the blue tile or HOME.",True,black)
    screen.blit(text1, [520, 0])
    screen.blit(text2, [230, 15])
    screen.blit(text3, [530, 15])
    screen.blit(text4, [20, 30])
    screen.blit(text5, [630, 30])

    # Display winner
    if p1_piece.winner == True:
        font4 = pygame.font.SysFont('Calibri', 150, True, False)
        text = font4.render("PLAYER 1 WINS!", True,red)
        screen.blit(text, [50,275])
        font5 = pygame.font.SysFont('Calibri', 50, True, False)
        text = font5.render("Press reset on the bottom to reset the game.", True,red)
        screen.blit(text, [73, 385])
    elif p2_piece.winner == True:
        font4 = pygame.font.SysFont('Calibri', 150, True, False)
        text = font4.render("PlAYER 2 WINS!", True,blue)
        screen.blit(text, [50,275])
        font5 = pygame.font.SysFont('Calibri', 50, True, False)
        text = font5.render("Press reset on the bottom to reset the game.", True,blue)
        screen.blit(text, [73, 385])

    # Text for sent home
    if p1_piece.senthome == True:
        font6 = pygame.font.SysFont('Calibri', 20, True, False)
        text = font6.render("PLAYER 1 WAS SENT HOME!",True,white)
        screen.blit(text, [845, 150])
        if p1_piece.turn == False:
            p1_piece.senthome = False
    if p2_piece.senthome == True:
        font6 = pygame.font.SysFont('Calibri', 20, True, False)
        text = font6.render("PLAYER 2 WAS SENT HOME!",True,white)
        screen.blit(text, [845, 150])
        if p2_piece.turn == False:
            p2_piece.senthome = False
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
