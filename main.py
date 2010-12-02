#!/usr/bin/env python2.7

import chess
import wx


class ChessWindow(object):
    def draw_board(self):
        pass

def main():
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Hello World")
    frame.Show(True)
    app.MainLoop()

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