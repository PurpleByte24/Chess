import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "100, 100"
import pgzrun

## Screen variables
TITLE = "CHESS"
HEIGHT = 380
WIDTH = 380

## Back-End Gameplay
class WHITE:
    def __init__(self):
        self.chosenField = None
        self.mode = None
        self.locRook1 = [1, 7, "r"]
        self.locKnight1 = [2, 7, "kn"]
        self.locBishop1 = [3, 7, "b"]
        self.locKing = [4, 7, "ki"]
        self.locQueen = [5, 7, "q"]
        self.locBishop2 = [6, 7, "b"]
        self.locKnight2 = [7, 7, "kn"]
        self.locRook2 = [8, 7, "r"]
        self.locPawn1 = [1, 8, "p"]
        self.locPawn2 = [2, 8, "p"]
        self.locPawn3 = [3, 8, "p"]
        self.locPawn4 = [4, 8, "p"]
        self.locPawn5 = [5, 8, "p"]
        self.locPawn6 = [6, 8, "p"]
        self.locPawn7 = [7, 8, "p"]
        self.locPawn8 = [8, 8, "p"]
        self.locs = [self.locRook1, self.locKnight1, self.locBishop1, self.locKing, self.locQueen, self.locBishop2, self.locKnight2, self.locRook2,
                     self.locPawn1, self.locPawn2, self.locPawn3, self.locPawn4, self.locPawn5, self.locPawn6, self.locPawn7, self.locPawn8]
        
        self.pawn1HasMoved = False
        self.pawn2HasMoved = False
        self.pawn3HasMoved = False
        self.pawn4HasMoved = False
        self.pawn5HasMoved = False
        self.pawn6HasMoved = False
        self.pawn7HasMoved = False
        self.pawn8HasMoved = False
        self.allPawnsHasMoved = [self.pawn1HasMoved, self.pawn2HasMoved, self.pawn3HasMoved, self.pawn4HasMoved,
                                 self.pawn5HasMoved, self.pawn6HasMoved, self.pawn7HasMoved, self.pawn8HasMoved]
        self.kingHasMoved = False 
        self.rook1HasMoved = False
        self.rook2HasMoved = False
        
        
    def getLocs(self):
        self.locs = [self.locRook1, self.locKnight1, self.locBishop1, self.locKing, self.locQueen, self.locBishop2, self.locKnight2, self.locRook2,
                     self.locPawn1, self.locPawn2, self.locPawn3, self.locPawn4, self.locPawn5, self.locPawn6, self.locPawn7, self.locPawn8]
        self.allPawnsHasMoved = [self.pawn1HasMoved, self.pawn2HasMoved, self.pawn3HasMoved, self.pawn4HasMoved,
                                 self.pawn5HasMoved, self.pawn6HasMoved, self.pawn7HasMoved, self.pawn8HasMoved]
        return self.locs
    
    def moveRook(self, locs):        
        if field1[0] == field2[0]: #check if the clicked fields have the same x coords
            for loc in locs:
                if loc[0] == field1[0]: 
                    if min(field1[1], field2[1]) < loc[1] < max(field1[1], field2[1]): #check if any figures are between the clicked fields
                        pass
                    else:
                        self.moveFigureVisually()
                    
        if field1[1] == field2[1]: #check if the clicked fields have the same y coords
            for loc in locs:
                if loc[1] == field1[1]:
                    if min(field1[0], field2[0]) < loc[0] < max(field1[0], field2[0]):
                        pass
                    else:                        
                        self.moveFigureVisually()
                

    def moveKnight(self, deltaX, deltaY):
        print("knight")

    def moveBishop(self, deltaX, deltaY):
        print("bishop")

    def moveKing(self, deltaX, deltaY):
        print("king")

    def moveQueen(self, deltaX, deltaY):
        print("queen")

    def movePawn(self, locs, index):
        pawnHasMoved = self.allPawnsHasMoved[index]
        goingFurther = True 
        for loc in locs:
            if field2 == loc:
                goingFurther = False
                break                 
        if goingFurther:
            if field1[0] == field2[0]:
                if not pawnHasMoved:
                    self.allPawnsHasMoved[index] = True 
                    if field1[1] == field2[1]+2:
                        self.moveFigureVisually()
                if field1[1] == field2[1]+1:
                        self.moveFigureVisually()
            else:
                pass
    
    def moveFigureVisually(self): #todo
        print("would move but wasnt build")
    
    def locateField(self): #check if field has a figure on it
        if self.mode == 1:
            for index, loc in enumerate(self.locs):
                if self.chosenField[0] == loc[0] and self.chosenField[1] == loc[1]:
                    return True, index                
            return False, None #only happens if 'return' on upper line was not executed
        
        elif self.mode == 2:
            for loc in self.locs:
                if self.chosenField[0] == loc[0] and self.chosenField[1] == loc[1]:
                    return False                
            return True #only happens if 'return' on upper line was not executed
        
    def classController(self, field, mode):
        self.chosenField = field
        self.mode = mode
        if self.mode == 1:
            goingFurther, index = self.locateField()
            if goingFurther:
                return 2, index #return index for comparison of fields later on
            else:
                return 1, None
            
        elif self.mode == 2:
            goingFurther = self.locateField()
            return goingFurther
        
class BLACK:
    def __init__(self):
        self.chosenField = None
        self.mode = None
        self.locRook1 = [1, 1, "r"]
        self.locKnight1 = [2, 1, "kn"]
        self.locBishop1 = [3, 1, "b"]
        self.locKing = [4, 1, "ki"]
        self.locQueen = [5, 1, "q"]
        self.locBishop2 = [6, 1, "b"]
        self.locKnight2 = [7, 1, "kn"]
        self.locRook2 = [8, 1, "r"]
        self.locPawn1 = [1, 2, "p"]
        self.locPawn2 = [2, 2, "p"]
        self.locPawn3 = [3, 2, "p"]
        self.locPawn4 = [4, 2, "p"]
        self.locPawn5 = [5, 2, "p"]
        self.locPawn6 = [6, 2, "p"]
        self.locPawn7 = [7, 2, "p"]
        self.locPawn8 = [8, 2, "p"]
        self.locs = [self.locRook1, self.locKnight1, self.locBishop1, self.locKing, self.locQueen, self.locBishop2, self.locKnight2, self.locRook2,
                     self.locPawn1, self.locPawn2, self.locPawn3, self.locPawn4, self.locPawn5, self.locPawn6, self.locPawn7, self.locPawn8]
        
    def getLocs(self):
        self.locs = [self.locRook1, self.locKnight1, self.locBishop1, self.locKing, self.locQueen, self.locBishop2, self.locKnight2, self.locRook2,
                     self.locPawn1, self.locPawn2, self.locPawn3, self.locPawn4, self.locPawn5, self.locPawn6, self.locPawn7, self.locPawn8]
        return self.locs
    
    def moveRook(self):
        print(1)

    def moveKnight(self):
        print(1)

    def moveBishop(self):
        print(1)

    def moveKing(self):
        print(1)

    def moveQueen(self):
        print(1)

    def movePawn(self):
        print(1)
    
    def locateField(self): #check if field has a figure on it
        if self.mode == 2:
            for index, loc in enumerate(self.locs):
                if self.chosenField[0] == loc[0] and self.chosenField[1] == loc[1]:
                    if self.locs[index][2] == "ki": #check if king is on targeted field (cant kill king)
                        return False, None
                    else:
                        return True, index
            return True, None
        
    def classController(self, field, mode):
        self.chosenField = field
        self.mode = mode
        if self.mode == 2:
            goingFurther, index = self.locateField()
            if goingFurther:
                return True, index 
            else:
                return False, None
        
        


## Board and its fields 
field_length = 35
rows, cols = 8, 8
edge = 50
board = [[Rect((row * field_length + edge, col * field_length + edge), (field_length, field_length)) for col in range(cols)] for row in range(rows)]

square_color = None
purple = "purple"
darkPurple = (135, 0, 135)
white = "white"
grey = "grey"

## Game
cursor_rect = Rect((0, 0), (0, 0))

player1 = WHITE()
player2 = BLACK()

field1 = None
field2 = None 
whiteFigToMoveInd = None
blackFigThatDiesInd = None

gamemode = 1

## Actors (initializing and positioning)
rook_WL = Actor("rook_w.png", pos=(edge+0*field_length+field_length/2, HEIGHT-edge-field_length/2))
knight_WL = Actor("knight_l_w.png", pos=(edge+1*field_length+field_length/2, HEIGHT-edge-field_length/2))
bishop_WL = Actor("bishop_w.png", pos=(edge+2*field_length+field_length/2, HEIGHT-edge-field_length/2))
king_W = Actor("king_w.png", pos=(edge+3*field_length+field_length/2, HEIGHT-edge-field_length/2))
queen_W = Actor("queen_w.png", pos=(edge+4*field_length+field_length/2, HEIGHT-edge-field_length/2))
bishop_WR = Actor("bishop_w.png", pos=(edge+5*field_length+field_length/2, HEIGHT-edge-field_length/2))
knight_WR = Actor("knight_r_w.png", pos=(edge+6*field_length+field_length/2, HEIGHT-edge-field_length/2))
rook_WR = Actor("rook_w.png", pos=(edge+7*field_length+field_length/2, HEIGHT-edge-field_length/2))
pawn1_W = Actor("pawn_w.png", pos=(edge+0*field_length+field_length/2, HEIGHT-edge-field_length*1.5))
pawn2_W = Actor("pawn_w.png", pos=(edge+1*field_length+field_length/2, HEIGHT-edge-field_length*1.5))
pawn3_W = Actor("pawn_w.png", pos=(edge+2*field_length+field_length/2, HEIGHT-edge-field_length*1.5))
pawn4_W = Actor("pawn_w.png", pos=(edge+3*field_length+field_length/2, HEIGHT-edge-field_length*1.5))
pawn5_W = Actor("pawn_w.png", pos=(edge+4*field_length+field_length/2, HEIGHT-edge-field_length*1.5))
pawn6_W = Actor("pawn_w.png", pos=(edge+5*field_length+field_length/2, HEIGHT-edge-field_length*1.5))
pawn7_W = Actor("pawn_w.png", pos=(edge+6*field_length+field_length/2, HEIGHT-edge-field_length*1.5))
pawn8_W = Actor("pawn_w.png", pos=(edge+7*field_length+field_length/2, HEIGHT-edge-field_length*1.5))

whiteFigures = [king_W, queen_W, bishop_WL, bishop_WR, knight_WL, knight_WR, rook_WL, rook_WR,
                 pawn1_W, pawn2_W, pawn3_W, pawn4_W, pawn5_W, pawn6_W, pawn7_W, pawn8_W]


rook_BL = Actor("rook_b.png", pos=(edge+0*field_length+field_length/2, edge+field_length/2))
knight_BL = Actor("knight_l_b.png", pos=(edge+1*field_length+field_length/2, edge+field_length/2))
bishop_BL = Actor("bishop_b.png", pos=(edge+2*field_length+field_length/2, edge + field_length/2))
king_B = Actor("king_b.png", pos=(edge+3*field_length+field_length/2, edge+field_length/2))
queen_B = Actor("queen_b.png", pos=(edge+4*field_length+field_length/2, edge+field_length/2))
bishop_BR = Actor("bishop_b.png", pos=(edge+5*field_length+field_length/2, edge+field_length/2))
knight_BR = Actor("knight_r_b.png", pos=(edge+6*field_length+field_length/2, edge+field_length/2))
rook_BR = Actor("rook_b.png", pos=(edge+7*field_length+field_length/2, edge+field_length/2))
pawn1_B = Actor("pawn_b.png", pos=(edge+0*field_length+field_length/2, edge+field_length*1.5))
pawn2_B = Actor("pawn_b.png", pos=(edge+1*field_length+field_length/2, edge+field_length*1.5))
pawn3_B = Actor("pawn_b.png", pos=(edge+2*field_length+field_length/2, edge+field_length*1.5))
pawn4_B = Actor("pawn_b.png", pos=(edge+3*field_length+field_length/2, edge+field_length*1.5))
pawn5_B = Actor("pawn_b.png", pos=(edge+4*field_length+field_length/2, edge+field_length*1.5))
pawn6_B = Actor("pawn_b.png", pos=(edge+5*field_length+field_length/2, edge+field_length*1.5))
pawn7_B = Actor("pawn_b.png", pos=(edge+6*field_length+field_length/2, edge+field_length*1.5))
pawn8_B = Actor("pawn_b.png", pos=(edge+7*field_length+field_length/2, edge+field_length*1.5))

blackFigures = [king_B, queen_B, bishop_BL, bishop_BR, knight_BL, knight_BR, rook_BL, rook_BR,
                 pawn1_B, pawn2_B, pawn3_B, pawn4_B, pawn5_B, pawn6_B, pawn7_B, pawn8_B]

## Front-End Gameplay
def draw_Chessboard():
    global square_color
    for row in range(rows):
        for col in range(cols):
            square_color = white if (row + col) % 2 == 0 else purple #setting color for each field
            screen.draw.filled_rect(board[row][col], square_color) #draw field with corresponding color
            highlightField()
            
def highlightField():
    for row in range(rows):
        for col in range(cols):
            if cursor_rect.colliderect(board[row][col]):
                touchedField = board[row][col]
                square_color = grey if (row+col) % 2 == 0 else darkPurple 
                screen.draw.filled_rect(touchedField, square_color)


def draw_WhiteFigures():
    for figure in whiteFigures:
        figure.draw()
        
def draw_BlackFigures():
    for figure in blackFigures:
        figure.draw()

def callFigureFunc(index):
    if gamemode == 2:
        player = player1
        
    else: #todo NEEDS TO BE CHANGED TO THE RIGHT GAMEMODE
        player = player2
        
    #print(field1, field2)
    deltaX = field1[0] - field2[0]
    deltaY = field1[1] - field2[1]
    
    whiteFigLocs, blackFigLocs = player1.getLocs(), player2.getLocs()
    currentLocs = blackFigLocs + whiteFigLocs
    editedLocs = []
    for loc in currentLocs:
        loc = loc[:-1]
        editedLocs.append(loc)
    currentLocs = editedLocs #all locations wihtout the reference string    


    if index == 8 or index == 15:
        player.moveRook(currentLocs)
    elif index == 9 or index == 14:
        player.moveKnight(deltaX, deltaY, currentLocs)
    elif index == 10 or index == 13:
        player.moveBishop(deltaX, deltaY, currentLocs)
    elif index == 11:
        player.moveKing(deltaX, deltaY), currentLocs
    elif index == 12:
        player.moveQueen(deltaX, deltaY, currentLocs)
    elif index <= 7:
        player.movePawn(currentLocs, index) #give index for 'HasMoved' list
        
def on_key_down(key):
    if key == keys.ESCAPE:
        quit()

def on_mouse_move(pos):
    global cursor_rect
    x, y = pos
    cursor_rect = Rect((x, y), (1, 1))
    
def on_mouse_down(pos): #todo
    global gamemode, field1, field2, whiteFigToMoveInd, blackFigThatDiesInd
    for row in range(rows):
        for col in range(cols):            
            if cursor_rect.colliderect(board[row][col]):
                chosenField = [row+1, col+1]                
                if gamemode == 1: #white choses figure to move
                    field1 = chosenField
                    gamemode, whiteFigToMoveInd = player1.classController(chosenField, 1)                    
                    print(f"whiteFigToMoveInd: {whiteFigToMoveInd}")
                    
                elif gamemode == 2: #white choses field to move figure
                    field2 = chosenField
                    goingFurther = player1.classController(chosenField, 2) #white figure cant move onto white figure
                    if goingFurther:
                        goingFurther1, blackFigThatDiesInd = player2.classController(chosenField, 2) #check for black figures
                        if goingFurther1:
                            callFigureFunc(whiteFigToMoveInd)
                        else:
                            gamemode = 1
                    else:
                        gamemode = 1
                    
                    
                    
def draw():
    screen.clear()
    draw_Chessboard()
    draw_WhiteFigures()
    draw_BlackFigures()
    
    
pgzrun.go()