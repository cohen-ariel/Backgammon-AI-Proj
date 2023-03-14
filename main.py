import pygame
from board import Board
import random
from h_set import H_Set

'''--------------- CONSTANTS ---------------'''

WINDOW_H = 780
WINDOW_L = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLACK_P = (60, 60, 60)
WHITE_P = (240, 240, 240)
GREEN = (65, 220, 65)
RED1 = (160, 0, 0)
RED2 = (100, 0, 0)
RED3 = (60, 0, 0)
DARK_GRAY = (150, 150, 150)
GRAY = (75, 75, 75)

X_MSG = 727
Y_MSG0 = 530
Y_MSG26 = 70

B = 'b'
W = 'w'
N = 'n'

LEFT = 1
SCROLL = 2
RIGHT = 3

IMAGE = "Wood2.jpg"

'''--------------- STARTING ---------------'''

pygame.init()
pygame.display.set_caption("Backgammon - Ariel Cohen")
size = (WINDOW_H, WINDOW_L)
screen = pygame.display.set_mode(size)
pygame.display.flip()
font = pygame.font.Font('freesansbold.ttf', 15)
img = pygame.image.load(IMAGE)
background_surf = pygame.Surface(size)
background_surf.blit(img, (0, 0))

'''--------------- FUNCTIONS ---------------'''


def opening_window():
    # shows the opening window graphically on screen
    # receives input - a "click" on the 'READY' or 'INSTRUCTIONS' button
    pygame.draw.rect(screen, DARK_GRAY, [22, 22, 745, 560])
    show_message("SMART  BACKGAMMON  -  ARIEL  COHEN", DARK_GRAY, 390, 90)
    show_message("PRESS 'INSTRUCTIONS' TO LEARN HOW TO PLAY", DARK_GRAY, 390, 150)
    show_message("OR 'READY' TO START PLAYING!", DARK_GRAY, 390, 180)

    show_message("INSTRUCTIONS", GRAY, 300, 280)
    show_message("      READY      ", GRAY, 480, 280)

    pygame.display.flip()


def instructions_window():
    # shows the instructions window graphically on screen
    # receives input - a "click" on the 'GOT IT!' button

    pygame.draw.rect(screen, DARK_GRAY, [22, 22, 745, 560])
    show_message("SMART  BACKGAMMON  -  ARIEL  COHEN", DARK_GRAY, 390, 90)
    show_message("INSTRUCTIONS", DARK_GRAY, 390, 150)

    # how to play the game
    show_message("It is a two-player game where each player has fifteen pieces that move", DARK_GRAY, 390, 150)
    show_message("between twenty-four triangles according to the roll of two dice.", DARK_GRAY, 390, 180)
    show_message("You can't move to a triangle which has enemy pips, unless it's one pip, then you can 'eat' it", DARK_GRAY, 390, 210)
    show_message("If you have one or more of your pips 'eaten', you have to get them on board them first", DARK_GRAY, 390, 240)
    show_message("The objective of the game is to be first to move all fifteen checkers off the board.", DARK_GRAY, 390, 270)

    # how to use the program (application)
    show_message("To play, click once on a pip your color to tag it. Second click wherever to put it!", DARK_GRAY, 390, 360)
    show_message("If the intended move is illegal, a message will pop up, but the tag will remain", DARK_GRAY, 390, 390)
    show_message("on the same pip. Click again on the tagged pip to reset the tag.", DARK_GRAY, 390, 420)
    show_message("Every dice roll, the dices will be shown both graphically and as numbers in the middle.", DARK_GRAY, 390, 450)
    show_message("When it's the computer's turn, a message asking to wait will pop up;", DARK_GRAY, 390, 480)
    show_message("Unless it does, it's your turn!", DARK_GRAY, 390, 510)
    show_message("Whenever a pip is eaten, it will be shown in the rightest cell of the player.", DARK_GRAY, 390, 540)
    show_message("Click 'GOT IT!' to continue. Good luck!", DARK_GRAY, 390, 570)

    show_message("GOT  IT!", GRAY, 390, 330)

    pygame.display.flip()


def difficulty_window():
    # shows the difficulty window graphically on screen
    # receives input - a "click" on the 'EASY', 'MEDIUM' OR 'HARD' button

    pygame.draw.rect(screen, DARK_GRAY, [22, 22, 745, 560])
    show_message("SMART  BACKGAMMON  -  ARIEL  COHEN", DARK_GRAY, 390, 90)
    show_message("DIFFICULTY", DARK_GRAY, 390, 150)

    show_message("Choose what difficulty you want:", DARK_GRAY, 390, 120)
    show_message("(The higher the difficulty you pick, the more time you will have to wait", DARK_GRAY, 390, 150)
    show_message("for the game to start, and the computer's turn will take slightly longer)", DARK_GRAY, 390, 180)
    show_message("EASY - around 30min     MEDIUM - around 1hr     HARD - around 2hr", DARK_GRAY, 390, 210)
    show_message("EASY - INSTANT: The game will start immediately, and the turns will be short", DARK_GRAY, 390, 240)
    show_message("(for testing the game and not the algorithms)", DARK_GRAY, 390, 260)

    show_message(" EASY ", GRAY, 300, 300)
    show_message("MEDIUM", GRAY, 390, 300)
    show_message(" HARD ", GRAY, 480, 300)
    show_message("EASY - INSTANT", GRAY, 390, 340)

    pygame.display.flip()


def show_message(msg, color=WHITE, x=350, y=300):
    # gets text to show, the coordinates of where to show it and the color and shows it on screen
    text = font.render(msg, True, BLACK, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)
    pygame.display.flip()


def show_extra_pips(cell):
    # gets a Cell object, and shows the extra pips that can't be drawn (when pips > 5)
    num = cell.get_num()
    color = cell.get_color()
    pips = cell.get_pips()

    # set msg (+?)
    plus = pips - 5
    msg = "+"+str(plus)

    # set x and y
    if num == 0:
        y = 555
        x = X_MSG
    elif num == 25:
        y = 45
        x = X_MSG
    else:
        if num <= 12:
            x = 700 - 50 * num
            y = 555
            if num > 6:
                x -= 50
        else:
            x = 50 + 50 * (num-13)
            y = 45
            if num > 18:
                x += 50

    # set color
    if color == B:
        new_color = BLACK_P
    else:
        new_color = WHITE_P


    show_message(msg, new_color, x, y)


def background():
    # draws the background gradient with colors of choice
    screen.blit(img, (-13, -13))
    R = 190
    G = 40
    B = 20
    color = (R, G, B)
    x1 = 25
    x2 = 25
    y = 25
    leng1 = (WINDOW_H-180)/2
    leng2 = WINDOW_L-50

    for i in range(150):
        pygame.draw.rect(screen, color, [x1, y, leng1, leng2], 1)
        pygame.draw.rect(screen, color, [x2+350, y, leng1, leng2], 1)
        if i <= 150:
            x1 += 1
            x2 += 1
            y += 1
            leng1 -= 2
            leng2 -= 2
        if i % 5 == 0:
            R += 1
        if i % 5 == 0:
            G += 3
        color = (R, G, B)
        if i == 0:
            pygame.draw.rect(screen, BLACK, [x1, y, leng1, leng2], 6)
            pygame.draw.rect(screen, BLACK, [x2+350, y, leng1, leng2], 6)

    x1 = 675
    y1 = 575
    y2 = 350
    y3 = 25
    y4 = 250
    for i in range(12):
        if i == 6:
            x1 -= 50
        x2 = x1 - 50
        x3 = x1 - 25

        if i % 2 == 0:
            color1 = RED1
            color2 = RED2
        else:
            color1 = RED2
            color2 = RED1
        pygame.draw.polygon(screen, color1, [(x1, y1), (x2, y1), (x3, y2)], 0)
        pygame.draw.polygon(screen, color2, [(x1, y3), (x2, y3), (x3, y4)], 0)
        x1 = x2

    pygame.draw.rect(screen, RED3, [690, 25, 75, 225])
    pygame.draw.rect(screen, RED3, [690, 350, 75, 225])

    pygame.display.flip()


def update_screen(board, marked_cell=None):
    # gets a board and shows it graphically on screen
    # optional: gets a cell to mark as well
    background()
    cells = board.get_board()
    down_row = cells[:13]
    x = 727
    change_x = 50
    change_y = 40
    for c in down_row:
        temp = c.get_color()
        num = c.get_num()
        pips = c.get_pips()
        y = 555

        if temp == B:
            color = BLACK_P
        else:
            color = WHITE_P

        for i in range(pips):
            if i < 5:
                pygame.draw.circle(screen, color, (x, y), 20)
                pygame.draw.circle(screen, BLACK, (x, y), 20, 2)
                more_than_5 = False
            else:
                show_extra_pips(c)
                more_than_5 = True

            if marked_cell == num and i == pips-1:
                if more_than_5:
                    pygame.draw.circle(screen, GREEN, (x, y + (pips-1)*change_y), 25, 3)
                else:
                    pygame.draw.circle(screen, GREEN, (x, y), 25, 3)
            y -= change_y

        x -= change_x
        if num == 0:
            x -= 27
        if num == 6:
            x -= change_x

    up_row = cells[13:]
    x = 50
    change_x = 50
    change_y = 40
    for c in up_row:
        temp = c.get_color()
        num = c.get_num()
        pips = c.get_pips()
        y = 45

        if temp == B:
            color = BLACK_P
        else:
            color = WHITE_P

        for i in range(pips):
            if i < 5:
                pygame.draw.circle(screen, color, (x, y), 20)
                pygame.draw.circle(screen, BLACK, (x, y), 20, 2)
                more_than_5 = False
            else:
                show_extra_pips(c)
                more_than_5 = True

            if marked_cell == num and i == pips-1:
                if more_than_5:
                    pygame.draw.circle(screen, GREEN, (x, y - (pips-1)*change_y), 25, 3)
                else:
                    pygame.draw.circle(screen, GREEN, (x, y), 25, 3)
            y += change_y

        x += change_x
        if num == 24:
            x += 27
        if num == 18:
            x += change_x

    pygame.display.flip()


def what_cell(x, y):
    # gets x and y values and returns number of cell in that position (if any)
    if 350 <= y <= 575:
        if 675 >= x >= 375:
            num = 13-((x-25)//50)
        elif 25 <= x <= 325:
            num = 12-((x-25)//50)
        elif 690 <= x <= 765:
            num = 0
        else:
            num = None
    elif 25 <= y <= 250:
        if 25 <= x <= 325:
            num = ((x-25)//50)+13
        elif 375 <= x <= 675:
            num = ((x-25)//50)+12
        elif 690 <= x <= 765:
            num = 25
        else:
            num = None
    else:
        num = None

    return num


def roll_dices():
    # returns a tuple of 2 random ints
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    tup = (n1, n2)
    show_message(str(tup), WHITE, 350, 200)

    show_dices(tup)

    return tup


def show_dices(tup):
    # gets a double of dices and shows them on screen
    pygame.draw.rect(screen, WHITE, [330, 230, 40, 40])
    pygame.draw.rect(screen, WHITE, [330, 330, 40, 40])

    pygame.draw.rect(screen, BLACK, [330, 230, 40, 40], 2)
    pygame.draw.rect(screen, BLACK, [330, 330, 40, 40], 2)

    for i in range(2):
        if tup[i] is None and tup[1-i] is not None:
            pygame.draw.line(screen, RED1, (330, 230 + 100 * i), (370, 270 + 100 * i), 6)
            pygame.draw.line(screen, RED1, (330, 270 + 100 * i), (370, 230 + 100 * i), 6)
        else:
            if tup[i] == 1 or tup[i] == 3 or tup[i] == 5:
                pygame.draw.circle(screen, BLACK, (350, 250 + 100 * i), 4)
            if tup[i] != 1:
                pygame.draw.circle(screen, BLACK, (338, 262 + 100 * i), 4)
                pygame.draw.circle(screen, BLACK, (362, 238 + 100 * i), 4)
            if tup[i] == 4 or tup[i] == 5 or tup[i] == 6:
                pygame.draw.circle(screen, BLACK, (338, 238 + 100 * i), 4)
                pygame.draw.circle(screen, BLACK, (362, 262 + 100 * i), 4)
            if tup[i] == 6:
                pygame.draw.circle(screen, BLACK, (338, 250 + 100 * i), 4)
                pygame.draw.circle(screen, BLACK, (362, 250 + 100 * i), 4)

    pygame.display.flip()


def which_move(tup_move):
    # gets tuple (from cell A, to cell B)
    # returns what type of move is done (conquer / add / eat)
    cell_a = tup_move[0]
    cell_b = tup_move[1]
    color_a = cell_a.get_color()
    color_b = cell_b.get_color()
    pips_b = cell_b.get_pips()

    if pips_b == 0:
        return "conquer"
    if pips_b == 1:
        if color_a == color_b:
            return "add"
        else:
            return "eat"

    return "add"


def make_move(board, tup_nums):
    # gets a board and a tuple with 2 cells numbers, and moves a pip from cell A to cell B.

    from_cell = board.get_board()[tup_nums[0]]
    to_cell = board.get_board()[tup_nums[1]]
    turn = board.get_turn()

    tup_cells = (from_cell, to_cell)
    type_move = which_move(tup_cells)
    if (turn == B and to_cell.get_num() == 25) or (turn == W and to_cell.get_num() == 0):
        pass
    elif type_move == "conquer":
        to_cell.conquer(turn)
    elif type_move == "eat":
        board.eat(to_cell)
    elif type_move == "add":
        to_cell.add()
    else:
        pass
    from_cell.take_off()


def players_turn(board):
    # rolls 2 dices and shows them. gets a board and receives 2 click inputs from screen every time;
    # moves a pip on players turn from first cell clicked to second one clicked and updates the
    # screen. Does that twice if dices are different, and 4 times if dices are the same (whenever gets stuck -
    # if ever - stops). Returns the new board.

    dice1, dice2 = roll_dices()
    dice_tuple = (dice1, dice2)

    stuck = board.is_stuck(dice_tuple)
    main_count = 0
    if dice1 == dice2:
        while main_count < 4 and not stuck:
            cnt = 0
            while cnt < 2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return "finish"

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                        x, y = pygame.mouse.get_pos()
                        if cnt == 0:
                            from_cell = what_cell(x, y)
                            if from_cell is not None:  # if a certain cell was chosen (None = no cell)
                                if board.from_legal(from_cell):
                                    cnt += 1
                                    update_screen(board, from_cell)
                                    show_dices(dice_tuple)
                                else:
                                    update_screen(board)
                                    show_message("Can't move this one!")

                        elif cnt == 1:
                            to_cell = what_cell(x, y)
                            if to_cell is not None:  # if a certain cell was chosen (None = no cell)
                                if to_cell == from_cell:
                                    cnt = 0
                                    update_screen(board)
                                    show_dices(dice_tuple)
                                elif board.legal_move((from_cell, to_cell), dice_tuple):
                                    cnt += 1
                                    make_move(board, (from_cell, to_cell))
                                    update_screen(board)
                                    show_dices(dice_tuple)
                                else:
                                    update_screen(board)
                                    show_message("Can't go to this one!!!")

                        else:
                            break

            if board.is_stuck(dice_tuple):
                update_screen(board)
                show_message("STUCK! Changing turns!")
                break
            main_count += 1

    else:
        while main_count < 2 and not stuck:
            cnt = 0
            while cnt < 2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return "finish"
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:

                        x, y = pygame.mouse.get_pos()
                        if cnt == 0:
                            from_cell = what_cell(x, y)
                            if from_cell is not None:  # if a certain cell was chosen (None = no cell)
                                if board.from_legal(from_cell):
                                    cnt += 1
                                    update_screen(board, from_cell)
                                    show_dices(dice_tuple)
                                else:
                                    show_message("Can't move this pip!")

                        elif cnt == 1:
                            to_cell = what_cell(x, y)
                            if to_cell is not None:  # if a certain cell was chosen (None = no cell)
                                if to_cell == from_cell:
                                    cnt = 0
                                    update_screen(board)
                                    show_dices(dice_tuple)
                                elif board.legal_move((from_cell, to_cell), dice_tuple):
                                    make_move(board, (from_cell, to_cell))
                                    cnt += 1
                                    update_screen(board)

                                    if abs(to_cell - from_cell) == dice1:
                                        dice_tuple = (None, dice2)
                                    else:
                                        dice_tuple = (dice1, None)

                                    show_dices(dice_tuple)


                                else:
                                    show_message("Can't go to this place!!!")

                        else:
                            break

            if board.is_stuck(dice_tuple):
                update_screen(board)
                show_message("STUCK! Changing turns!")
                break

            main_count += 1

    # Switch turns
    board.switch_turn()
    return board


def get_sons(state, tup_dices):
    # if gets tuple of dices, returns all the possible moves to make with those dices.
    # if not given, returns all possible moves using any possible dices.

    original_board = state.copy_board()
    cells = state.get_board()
    sons = []

    different_dices = []
    same_dices = []

    if tup_dices is None:
        for dice1 in range(1, 7):
            for dice2 in range(1, 7):
                if dice1 != dice2:
                    different_dices.append((dice1, dice2))
                else:
                    same_dices.append((dice1, dice1))

    else:
        dice1 = tup_dices[0]
        dice2 = tup_dices[1]

        if dice1 != dice2:
            different_dices = [(dice1, dice2), (dice2, dice1)]
        else:
            same_dices = [(dice1, dice2)]

    for tup in different_dices:
        dice1 = tup[0]
        dice2 = tup[1]

        for from_cell1 in cells:
            cnt = 0
            state = original_board.copy_board()
            from_color1 = from_cell1.get_color()
            from_num1 = from_cell1.get_num()

            if state.from_legal(from_num1):
                if from_color1 == B:
                    to_num1 = from_num1 + dice1
                if from_color1 == W:
                    to_num1 = from_num1 - dice1

                if 0 <= to_num1 <= 25:
                    tup_cells1 = (from_num1, to_num1)
                    tup_dices1 = (dice1, None)
                    if state.legal_move(tup_cells1, tup_dices1):
                        make_move(state, tup_cells1)
                        cnt += 1
                        stuck = state.is_stuck((dice2, None))
                        if stuck:
                            state.switch_turn()
                            theres_same = False
                            for s in sons:
                                if s[0].is_same(state):
                                    theres_same = True
                                    s[1] += 1

                            if not theres_same:
                                lis = [state, 1]
                                sons.append(lis)
                        else:
                            cells2 = state.get_board()
                            for from_cell2 in cells2:
                                cnt = 1
                                after_first_move = state.copy_board()
                                from_color2 = from_cell2.get_color()
                                from_num2 = from_cell2.get_num()

                                if state.from_legal(from_num2):
                                    if from_color2 == B:
                                        to_num2 = from_num2 + dice2
                                    if from_color2 == W:
                                        to_num2 = from_num2 - dice2

                                    if 0 <= to_num2 <= 25:
                                        tup_cells2 = (from_num2, to_num2)
                                        tup_dices2 = (dice2, None)
                                        if after_first_move.legal_move(tup_cells2, tup_dices2):
                                            make_move(after_first_move, tup_cells2)
                                            cnt += 1

                                            if cnt == 2 or stuck:
                                                after_first_move.switch_turn()
                                                theres_same = False
                                                for s in sons:
                                                    if s[0].is_same(after_first_move):
                                                        theres_same = True
                                                        s[1] += 1

                                                if not theres_same:
                                                    lis = [after_first_move, 1]
                                                    sons.append(lis)



    for tup in same_dices:
        dice = tup[0]
        for from_cell1 in cells:
            cnt = 0
            state = original_board.copy_board()
            from_color1 = from_cell1.get_color()
            from_num1 = from_cell1.get_num()

            if state.from_legal(from_num1):
                if from_color1 == B:
                    to_num1 = from_num1 + dice
                if from_color1 == W:
                    to_num1 = from_num1 - dice

                if 0 <= to_num1 <= 25:
                    tup_cells1 = (from_num1, to_num1)
                    tup_dices1 = (dice, None)
                    if state.legal_move(tup_cells1, tup_dices1):
                        make_move(state, tup_cells1)
                        cnt += 1
                        stuck = state.is_stuck((dice, None))

                        if stuck:
                            state.switch_turn()
                            theres_same = False
                            for s in sons:
                                if s[0].is_same(state):
                                    theres_same = True
                                    s[1] += 2

                            if not theres_same:
                                lis = [state, 2]
                                sons.append(lis)
                        else:
                            cells2 = state.get_board()
                            for from_cell2 in cells2:
                                cnt = 1
                                after_first_move = state.copy_board()
                                from_color2 = from_cell2.get_color()
                                from_num2 = from_cell2.get_num()

                                if state.from_legal(from_num2):
                                    if from_color2 == B:
                                        to_num2 = from_num2 + dice
                                    if from_color2 == W:
                                        to_num2 = from_num2 - dice

                                    if 0 <= to_num2 <= 25:
                                        tup_cells2 = (from_num2, to_num2)
                                        tup_dices2 = (dice2, None)
                                        if after_first_move.legal_move(tup_cells2, tup_dices2):
                                            make_move(after_first_move, tup_cells2)
                                            cnt += 1
                                            stuck = after_first_move.is_stuck((dice, None))

                                            if stuck:
                                                after_first_move.switch_turn()
                                                theres_same = False
                                                for s in sons:
                                                    if s[0].is_same(after_first_move):
                                                        theres_same = True
                                                        s[1] += 2

                                                if not theres_same:
                                                    lis = [after_first_move, 2]
                                                    sons.append(lis)
                                            else:
                                                cells3 = after_first_move.get_board()
                                                for from_cell3 in cells3:
                                                    cnt = 2
                                                    after_second_move = after_first_move.copy_board()
                                                    from_color3 = from_cell3.get_color()
                                                    from_num3 = from_cell3.get_num()

                                                    if after_second_move.from_legal(from_num3):
                                                        if from_color3 == B:
                                                            to_num3 = from_num3 + dice
                                                        if from_color3 == W:
                                                            to_num3 = from_num3 - dice

                                                        if 0 <= to_num3 <= 25:
                                                            tup_cells3 = (from_num3, to_num3)
                                                            tup_dices3 = (dice, None)
                                                            if after_second_move.legal_move(tup_cells3, tup_dices3):
                                                                make_move(after_second_move, tup_cells3)
                                                                cnt += 1
                                                                stuck = after_second_move.is_stuck((dice, None))

                                                                if stuck:
                                                                    after_second_move.switch_turn()
                                                                    theres_same = False
                                                                    for s in sons:
                                                                        if s[0].is_same(after_second_move):
                                                                            theres_same = True
                                                                            s[1] += 2

                                                                    if not theres_same:
                                                                        lis = [after_second_move, 2]
                                                                        sons.append(lis)
                                                                else:
                                                                    cells4 = after_second_move.get_board()
                                                                    for from_cell4 in cells4:
                                                                        cnt = 3
                                                                        after_third_move = after_second_move.copy_board()
                                                                        from_color4 = from_cell4.get_color()
                                                                        from_num4 = from_cell4.get_num()

                                                                        if after_third_move.from_legal(from_num4):
                                                                            if from_color4 == B:
                                                                                to_num4 = from_num4 + dice
                                                                            if from_color4 == W:
                                                                                to_num4 = from_num4 - dice

                                                                            if 0 <= to_num4 <= 25:
                                                                                tup_cells4 = (from_num4, to_num4)
                                                                                tup_dices4 = (dice, None)
                                                                                if after_third_move.legal_move(tup_cells4, tup_dices4):
                                                                                    make_move(after_third_move, tup_cells4)
                                                                                    cnt += 1

                                                                                    if cnt == 4 or stuck:
                                                                                        after_third_move.switch_turn()
                                                                                        theres_same = False
                                                                                        for s in sons:
                                                                                            if s[0].is_same(after_third_move):
                                                                                                theres_same = True
                                                                                                s[1] += 2

                                                                                        if not theres_same:
                                                                                            lis = [after_third_move, 2]
                                                                                            sons.append(lis)

    return sons


def computers_turn(board, depth, h_set):
    # gets the board, the depth to go in the expectimax algorithm, and an h_set for the computer to "play by".
    # makes a computer turn and returns the new board.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    tup_dices = (dice1, dice2)

    show_dices(tup_dices)

    sons = get_sons(board, tup_dices)
    if sons is not []:
        lis_board = [board, 0]
        new_board = expectimax(lis_board, tup_dices, W, depth, h_set)[0][0].copy_board()
    else:
        new_board = board.copy_board()

    update_screen(new_board)
    return new_board


def expectimax(state, tup_dices, agent, d, h_set, is_probability=False):
    # the expectimax algorithm: gets the current state (board), dices, agent, depth (how far or "deep"
    # the function will search), h_set (weights to calculate the h value by), and a boolean if the node is
    # a probability node. returns the "best move" the function found, according to the algorithm.

    turn = state[0].get_turn()
    winner = state[0].get_winner()

    if winner is not None or d == 0:
        return state, state[0].get_h_value(h_set)

    if is_probability:  # checks if the node is a probability node (every 2nd node is)
        probability = state[1]/36
        return state, probability * expectimax(state, tup_dices, agent, d-1, h_set, not is_probability)[1]

    sons = get_sons(state[0], tup_dices)

    if turn == agent:
        cur_max = -1000000000

        # if sons == []
        if not sons:
            state[0].switch_turn()
            return state, cur_max

        for s in sons:
            v = expectimax(s, tup_dices, agent, d-1, h_set, not is_probability)
            cur_max = max(v[1], cur_max)
        return s, cur_max

    else:
        cur_min = 1000000000

        # if sons == []
        if not sons:
            state[0].switch_turn()
            return state, cur_min

        for s in sons:
            v = expectimax(s, tup_dices, agent, d-1, h_set, not is_probability)
            cur_min = min(v[1], cur_min)
        return s, cur_min


def two_set_game(h_set1, h_set2):
    # gets two h_set's and conducts a game between them.
    # h_set1 will always be BLACK, and h_set2 will always WHITE.
    # returns the number of wins that each h_set got out of 5 games.

    board = Board()
    is_win = False
    turns_cnt = 0

    max_son = None
    while not is_win:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        tup_dices = (dice1, dice2)

        sons = get_sons(board, tup_dices)
        turns_cnt += 1
        max_h = -100
        for s in sons:
            turn = s[0].get_turn()
            if turn == B:
                new_h = s[0].get_h_value(h_set1) * s[1] / 36
            if turn == W:
                new_h = s[0].get_h_value(h_set2) * s[1] / 36

            if new_h > max_h:
                max_h = new_h
                max_son = s[0].copy_board()

        board = max_son.copy_board()
        winner = board.get_winner()
        if winner is not None:
            is_win = True
        else:
            is_win = False

    return winner, turns_cnt


def copy_h_set(h_set1, h_set2):
    # gets two h_set objects, copies one's weights into the other one, and changes them a little bit.
    # (not fully a 100% copy)
    change_w1 = random.randint(1, 9) / 1000
    change_w2 = random.randint(1, 9) / 1000
    change_w3 = random.randint(1, 9) / 1000

    if h_set1.get_w1() < 0.99:
        h_set2.set_w1(h_set1.get_w1() + change_w1)
    else:
        h_set2.set_w1(h_set1.get_w1() - change_w1)

    if h_set1.get_w2() < 0.99:
        h_set2.set_w2(h_set1.get_w2() + change_w2)
    else:
        h_set2.set_w2(h_set1.get_w2() - change_w2)

    if h_set1.get_w3() < 0.99:
        h_set2.set_w3(h_set1.get_w3() + change_w3)
    else:
        h_set2.set_w3(h_set1.get_w3() - change_w3)


def genetic_algorithm(population, generations):
    # the genetic algorithm: gets how big the population will be and how many
    # generations there will be (both int values). searches for the best weights according
    # to the algorithm, and returns them as an h_set object.

    h_sets = []
    for i in range(generations):
        if i == 0:
            for j in range(population):
                # a "tup_set" has the h_set in it, and the number of wins it got in the specific generation.
                lis_set = [H_Set(), 0]

                # "h_sets" is a list of "tup_sets"
                h_sets.append(lis_set)

        # run games between h_set's

        for j in range(population-1):
            current = h_sets[j]
            enemies = h_sets[j+1:]

            for enemy in enemies:
                winner = two_set_game(current[0], enemy[0])[0]
                # first argument of two_set_game is BLACK player, and the second is WHITE

                if winner == "BLACK":
                    current[1] += 1
                else:
                    enemy[1] += 1

        #  finding top 2 sets with most wins
        max_sets = []

        max_wins = -1
        index_to_pop = 0
        for j in range(population):
            if h_sets[j][1] > max_wins:
                max_wins = h_sets[j][1]
                index_to_pop = j
        max_sets.append(h_sets.pop(index_to_pop))

        if i == generations - 1:
            # if it's the last generation, return the best h_set
            return max_sets[0][0]

        else:
            max_wins = -1
            index_to_pop = 0
            for j in range(population-1):
                if h_sets[j][1] > max_wins:
                    max_wins = h_sets[j][1]
                    index_to_pop = j
            max_sets.append(h_sets.pop(index_to_pop))

            # "crossbreeding" and "copying"
            length_h_sets = len(h_sets)
            for ind in range(length_h_sets):
                if ind < length_h_sets // 2:
                    if ind < length_h_sets // 4:
                        copy_h_set(h_sets[ind][0], max_sets[0][0])
                    else:
                        copy_h_set(h_sets[ind][0], max_sets[1][0])

                else:
                    if ind - (length_h_sets // 2) < length_h_sets // 4:
                        ind_w1 = 0
                        ind_w2 = 1
                        ind_w3 = 0

                    else:
                        ind_w1 = 1
                        ind_w2 = 0
                        ind_w3 = 1

                    h_sets[ind][0].set_w1(max_sets[ind_w1][0].get_w1())
                    h_sets[ind][0].set_w2(max_sets[ind_w2][0].get_w2())
                    h_sets[ind][0].set_w3(max_sets[ind_w3][0].get_w3())

            h_sets = h_sets + max_sets

            # "mutation" of 1/3 of the population
            random_indexes = []
            cnt = 0
            while cnt < population//3:
                rnd_num = random.randint(1, population-1)
                if rnd_num not in random_indexes:
                    h_sets[rnd_num][0].mutation()
                    random_indexes.append(rnd_num)
                    cnt += 1


'''--------------- MAIN ---------------'''

b = Board()
update_screen(b)
opening_window()

pygame.display.flip()

finish = False
picked_difficulty = False
got_it = False
instant = False

while not picked_difficulty and not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x, y = pygame.mouse.get_pos()
            if 240 <= x <= 360 and 270 <= y <= 290:
                # 'INSTRUCTIONS' pressed
                update_screen(b)
                instructions_window()
                while not got_it and not finish:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            finish = True
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                            x, y = pygame.mouse.get_pos()
                            if 360 <= x <= 420 and 320 <= y <= 340:
                                # 'GOT IT!' pressed
                                update_screen(b)
                                difficulty_window()
                                got_it = True
                        
            elif (430 <= x <= 530 and 270 <= y <= 290) or got_it:
                # 'READY' pressed
                update_screen(b)
                difficulty_window()
                while not picked_difficulty and not finish:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            finish = True
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                            x, y = pygame.mouse.get_pos()
                            if 275 <= x <= 325 and 290 <= y <= 310:
                                # 'EASY' pressed
                                depth = 2
                                population = 3
                                generations = 3
                                instant = False
                                picked_difficulty = True
                                
                            elif 360 <= x <= 420 and 290 <= y <= 310:
                                # 'MEDIUM' pressed
                                depth = 3
                                population = 3
                                generations = 6
                                instant = False
                                picked_difficulty = True

                            elif 450 <= x <= 510 and 290 <= y <= 310:
                                # 'HARD' pressed
                                depth = 4
                                population = 6
                                generations = 5
                                instant = False
                                picked_difficulty = True
                            
                            elif 330 <= x <= 450 and 330 <= y <= 350:
                                # 'EASY - INSTANT' pressed
                                depth = 1
                                instant = True
                                picked_difficulty = True

if finish:
    pygame.quit()

update_screen(b)

if instant:
    best_h_set = H_Set()
else:
    show_message("Please wait...")
    best_h_set = genetic_algorithm(population, generations)

best_h_set.print_h_set()
update_screen(b)

there_is_winner = False

while not finish:
    for event in pygame.event.get():
        winner = b.get_winner()
        if event.type == pygame.QUIT:
            finish = True

        elif winner is not None:
            update_screen(b)
            if winner == "BLACK":
                show_message("BLACK WON!")
            else:
                show_message("WHITE WON!")
            finish = True
            there_is_winner = True

        else:
            if b.get_turn() == 'b':
                pygame.display.set_caption("Backgammon - BLACK's turn")
                new_board = players_turn(b)
                if new_board == "finish":
                    finish = True
                else:
                    b = new_board.copy_board()

            else:
                pygame.display.set_caption("Backgammon - WHITE's turn")
                show_message("Please wait (WHITE's turn)")
                new_board = computers_turn(b, depth, best_h_set)
                b = new_board.copy_board()
                update_screen(b)

        if finish:
            break

if there_is_winner:
    finish = False
    if winner == "BLACK":
        show_message("BLACK WON!")
    else:
        show_message("WHITE WON!")
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

pygame.quit()
