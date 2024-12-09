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
            square_color = "white" if (row + col) % 2 == 0 else "purple"
            screen.draw.filled_rect(board[row][col], square_color)
            detect_coll()

def detect_coll():
    global square_color
    for row in range(rows):
        for col in range(cols):
            if cursor_rect.colliderect(board[row][col]):
                collided_field = board[row][col]
                square_color = "white" if (row + col) % 2 == 0 else "purple"
                square_color = "grey" if square_color == "white" else (135, 0, 135) if square_color == "purple" else square_color
                screen.draw.filled_rect(collided_field, square_color)

def on_key_down(key):
    if key == keys.ESCAPE:
        quit()

def on_mouse_move(pos):
    global cursor_rect
    x, y = pos
    cursor_rect = Rect((x, y), (1, 1))
    
def draw():
    screen.clear()
    draw_chessboard()
    draw_black_figures()
    draw_white_figures()
    
pgzrun.go()