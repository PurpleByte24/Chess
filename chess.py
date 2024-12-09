import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 10"
import pgzrun

## Screen variables
TITLE = "CHESS"
HEIGHT = 380
WIDTH = 380

## Field 
field_length = 35
rows, cols = 8, 8
rand = 50
board = [[Rect((row * field_length + rand, col * field_length + rand), (field_length, field_length)) for col in range(cols)] for row in range(rows)]
square_color = None
cursor_rect = Rect((0, 0), (0, 0))

## Game
player1 = None
player2 = None
turn = None
game_mode = -1
chosen_field = None
keep_color = None 

## Actors
rook_l_b = Actor("rook_b.png", pos=(rand+0*field_length+field_length/2, HEIGHT-rand-field_length/2))
knight_l_b = Actor("knight_l_b.png", pos=(rand+1*field_length+field_length/2, HEIGHT-rand-field_length/2))
bishop_l_b = Actor("bishop_b.png", pos=(rand+2*field_length+field_length/2, HEIGHT-rand-field_length/2))
king_b = Actor("king_b.png", pos=(rand+3*field_length+field_length/2, HEIGHT-rand-field_length / 2))
queen_b = Actor("queen_b.png", pos=(rand+4*field_length+field_length/2, HEIGHT-rand-field_length/2))
bishop_r_b = Actor("bishop_b.png", pos=(rand+5*field_length+field_length/2, HEIGHT-rand-field_length/2))
knight_r_b = Actor("knight_r_b.png", pos=(rand+6*field_length+field_length/2, HEIGHT-rand-field_length/2))
rook_r_b = Actor("rook_b.png", pos=(rand+7*field_length+field_length/2, HEIGHT-rand-field_length/2))
pawn1_b = Actor("pawn_b.png", pos=(rand+0*field_length+field_length/2, HEIGHT-rand-field_length*1.5))
pawn2_b = Actor("pawn_b.png", pos=(rand+1*field_length+field_length/2, HEIGHT-rand-field_length*1.5))
pawn3_b = Actor("pawn_b.png", pos=(rand+2*field_length+field_length/2, HEIGHT-rand-field_length*1.5))
pawn4_b = Actor("pawn_b.png", pos=(rand+3*field_length+field_length/2, HEIGHT-rand-field_length*1.5))
pawn5_b = Actor("pawn_b.png", pos=(rand+4*field_length+field_length/2, HEIGHT-rand-field_length*1.5))
pawn6_b = Actor("pawn_b.png", pos=(rand+5*field_length+field_length/2, HEIGHT-rand-field_length*1.5))
pawn7_b = Actor("pawn_b.png", pos=(rand+6*field_length+field_length/2, HEIGHT-rand-field_length*1.5))
pawn8_b = Actor("pawn_b.png", pos=(rand+7*field_length+field_length/2, HEIGHT-rand-field_length*1.5))
black_figures = [king_b, queen_b, bishop_l_b, bishop_r_b, knight_l_b, knight_r_b, rook_l_b, rook_r_b, \
                 pawn1_b, pawn2_b, pawn3_b, pawn4_b, pawn5_b, pawn6_b, pawn7_b, pawn8_b]

rook_l_w = Actor("rook_w.png", pos=(rand+0*field_length+field_length/2, rand+field_length/2))
knight_l_w = Actor("knight_l_w.png", pos=(rand+1*field_length+field_length/2, rand+field_length/2))
bishop_l_w = Actor("bishop_w.png", pos=(rand+2*field_length+field_length/2, rand + field_length/2))
king_w = Actor("king_w.png", pos=(rand+3*field_length+field_length/2, rand+field_length/2))
queen_w = Actor("queen_w.png", pos=(rand+4*field_length+field_length/2, rand+field_length/2))
bishop_r_w = Actor("bishop_w.png", pos=(rand+5*field_length+field_length/2, rand+field_length/2))
knight_r_w = Actor("knight_r_w.png", pos=(rand+6*field_length+field_length/2, rand+field_length/2))
rook_r_w = Actor("rook_w.png", pos=(rand+7*field_length+field_length/2, rand+field_length/2))
pawn1_w = Actor("pawn_w.png", pos=(rand+0*field_length+field_length/2, rand+field_length*1.5))
pawn2_w = Actor("pawn_w.png", pos=(rand+1*field_length+field_length/2, rand+field_length*1.5))
pawn3_w = Actor("pawn_w.png", pos=(rand+2*field_length+field_length/2, rand+field_length*1.5))
pawn4_w = Actor("pawn_w.png", pos=(rand+3*field_length+field_length/2, rand+field_length*1.5))
pawn5_w = Actor("pawn_w.png", pos=(rand+4*field_length+field_length/2, rand+field_length*1.5))
pawn6_w = Actor("pawn_w.png", pos=(rand+5*field_length+field_length/2, rand+field_length*1.5))
pawn7_w = Actor("pawn_w.png", pos=(rand+6*field_length+field_length/2, rand+field_length*1.5))
pawn8_w = Actor("pawn_w.png", pos=(rand+7*field_length+field_length/2, rand+field_length*1.5))
white_figures = [king_w, queen_w, bishop_l_w, bishop_r_w, knight_l_w, knight_r_w, rook_l_w, rook_r_w, \
                 pawn1_w, pawn2_w, pawn3_w, pawn4_w, pawn5_w, pawn6_w, pawn7_w, pawn8_w]

locs = None

grid = [[row, col] for row in range(1, 9) for col in range(1, 9)]
    
    
    
    
loc_rook_l_b = [1, 1]
loc_knight_l_b = [2, 1]
loc_bishop_l_b = [3, 1]
loc_king_b = [4, 1]
loc_queen_b = [5, 1]
loc_bishop_r_b = [6, 1]
loc_knight_r_b = [7, 1]
loc_rook_r_b = [8, 1]
loc_pawn1_b = [1, 2]
loc_pawn2_b = [2, 2]
loc_pawn3_b = [3, 2]
loc_pawn4_b = [4, 2]
loc_pawn5_b = [5, 2]
loc_pawn6_b = [6, 2]
loc_pawn7_b = [7, 2]
loc_pawn8_b = [8, 2]
loc_rook_l_w = [1, 7]
loc_knight_l_w = [2, 7]
loc_bishop_l_w = [3, 7]
loc_king_w = [4, 7]
loc_queen_w = [5, 7]
loc_bishop_r_w = [6, 7]
loc_knight_r_w = [7, 7]
loc_rook_r_w = [8, 7]
loc_pawn1_w = [1, 8]
loc_pawn2_w = [2, 8]
loc_pawn3_w = [3, 8]
loc_pawn4_w = [4, 8]
loc_pawn5_w = [5, 8]
loc_pawn6_w = [6, 8]
loc_pawn7_w = [7, 8]
loc_pawn8_w = [8, 8]


    
b_locs = [loc_rook_l_b, loc_knight_l_b, loc_bishop_l_b, loc_king_b, loc_queen_b, loc_bishop_r_b, loc_knight_r_b, loc_rook_r_b,
          loc_pawn1_b, loc_pawn2_b, loc_pawn3_b, loc_pawn4_b, loc_pawn5_b, loc_pawn6_b, loc_pawn7_b, loc_pawn8_b]
w_locs = [loc_rook_l_w, loc_knight_l_w, loc_bishop_l_w, loc_king_w, loc_queen_w, loc_bishop_r_w, loc_knight_r_w, loc_rook_r_w,
          loc_pawn1_w, loc_pawn2_w, loc_pawn3_w, loc_pawn4_w, loc_pawn5_w, loc_pawn6_w, loc_pawn7_w, loc_pawn8_w]

locs = b_locs + w_locs



player1 = w_locs
player2 = b_locs
turn = player1

## Gameplay
def draw_black_figures():
    for figure in black_figures:
        figure.draw()

def draw_white_figures():
    for figure in white_figures:
        figure.draw()

def draw_chessboard():
    global square_color
    for row in range(rows):
        for col in range(cols):
            square_color = "white" if (row + col) % 2 == 0 else "purple" #setting color for each field
            screen.draw.filled_rect(board[row][col], square_color) #draw field with corresponding color
            detectMouseOnBoard()
            keep_field()

def detectMouseOnBoard():
    global square_color
    for row in range(rows):
        for col in range(cols):
            if cursor_rect.colliderect(board[row][col]):
                collided_field = board[row][col]
                #print(square_color, (row + col / 2))
                #square_color = "white" if (row + col) % 2 == 0 else "purple"
                #print(square_color)
                square_color = "grey" if square_color == "white" else (135, 0, 135) if square_color == "purple" else square_color
                screen.draw.filled_rect(collided_field, square_color)

def keep_field(): #todo
    global game_mode, keep_color
    if game_mode == 1:
        for row in range(rows):
            for col in range(cols):
                if cursor_rect.colliderect(board[row][col]):
                    color = "white" if (row + col) % 2 == 0 else "purple"
                    keep_color="grey" if color=="white" else (135, 0, 135) if color == "purple" else "red"
                    game_mode = 2
                    break
                
    if game_mode == 2:   
        screen.draw.filled_rect(chosen_field, keep_color)
    
def on_key_down(key):
    if key == keys.ESCAPE:
        quit()

def on_mouse_move(pos):
    global cursor_rect
    x, y = pos
    cursor_rect = Rect((x, y), (1, 1))

def on_mouse_down(pos):
    global game_mode, chosen_field
    if cursor_rect.left >= rand and cursor_rect.right <= WIDTH-rand and cursor_rect.top >= rand and cursor_rect.bottom <= HEIGHT-rand:
        for loc in turn:
            if cursor_rect.colliderect(loc):
                if game_mode == 0:
                    chosen_field = loc            
                    game_mode = 1
        if game_mode == 2:
            for field in board:
                print(chosen_field)

                if field == chosen_field:
                    
                    print("1")


                    
        
def draw():
    screen.clear()
    draw_chessboard()
    draw_black_figures()
    draw_white_figures()
    #allocation()
    
pgzrun.go()