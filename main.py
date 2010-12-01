#!/usr/bin/env python2.7

import chess


def test():
    board = chess.Board()
    board.set_board()
    print board.display()
    if board.move_piece((6,3),(5,3)):
        print ""
        print ""
        print board.display()
    else:
        print ""
        print "That move is invalid."
    if board.move_piece((7,2),(2,7)):
        print ""
        print ""
        print board.display()
    else:
        print ""
        print "That move is invalid."
        
if __name__ == "__main__":
    test()