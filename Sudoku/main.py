import pygame
import time
from helpers import get_board, update_time, initialize_graph_board, initialize_cnn_board
from solvers import backtrack_gui, graph_coloring_gui, neural_net_gui
from backtrack import Grid
start = time.time()

def main():
    global start
    win = pygame.display.set_mode((540,600))
    win.fill((255,255,255))
    pygame.display.set_caption("Sudoku")
    board = Grid(get_board(), 540, 540, win)
    board_reset = board.copy()
    run = True
    pause = False
    fast = False

    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_b:
                    backtrack_gui(board, start, fast)
                    pause = True
       
                elif event.key == pygame.K_g:
                    given, sudokuGraph = initialize_graph_board(board)
                    graph_coloring_gui(board, sudokuGraph,0,given, start, fast, m=9)
                    pause = True
                
                elif event.key == pygame.K_n:
                    game,model = initialize_cnn_board(board)
                    neural_net_gui(game,board,model,start, fast)

                    pause=True
                
                elif event.key == pygame.K_SPACE:
                    board = board_reset.copy()
                    pause = False
                
                elif event.key == pygame.K_f:
                    if fast == False:
                        fast = True
                    else:
                        fast = False

        if pause == False:
            win.fill((255,255,255))
            # draw grid
            board.draw()     
            # draw time   
            update_time(win, play_time)
        # update display
        pygame.display.update()


main()
pygame.quit()
