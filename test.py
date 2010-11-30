#!/usr/bin/env python2.7

import unittest
import chess



class KingMoves(unittest.TestCase):
    "This tests the legal moves for a king."
    legal_moves = ( ((0,3), (0,4)),
                    ((0,3), (1,2)),
                    ((0,3), (1,4)),
                    ((0,3), (0,2)),
                  )
    
    def test_legal_moves(self):
        for start, end in self.legal_moves:
            board = chess.Board()
            board.set_king(start[0], start[1])
            self.assertTrue(board.move_piece(start, end))
                        
class QueenMoves(unittest.TestCase):
    '''Tests legal moves for Queen Piece.'''
    legal_moves = ( ((0,4), (0,7)),
                    ((0,4), (4,0)),
                    ((0,0), (7,7)),
                  )
    
    def test_legal_moves(self):
        for start, end in self.legal_moves:
            board = chess.Board()
            board.set_queen(start[0], start[1])
            self.assertTrue(board.move_piece(start, end))

class PawnMoves(unittest.TestCase):
    legal_moves = ( ((6,1), (5,1)),
                    ((6,1), (4,1)),
                  )
    
    def test_legal_moves(self):
        for start, end in self.legal_moves:
            board = chess.Board()
            board.set_pawn(start[0], start[1])
            self.assertTrue(board.move_piece(start, end))
    
class KnightMoves(unittest.TestCase):
    legal_moves = ( ((7,1), (6,3)),
                    ((0,1), (2,0)),
                  )
                  
    def test_legal_moves(self):
        for start, end in self.legal_moves:
            board = chess.Board()
            board.set_knight(start[0], start[1])
            self.assertTrue(board.move_piece(start, end))
    
class BishopMoves(unittest.TestCase):
    legal_moves = ( ((7,0), (0,7)),
                    ((7,2), (5,4)),
                    ((5,3), (6,4)),
                  )
                  
    def test_legal_moves(self):
        for start, end in self.legal_moves:
            board = chess.Board()
            board.set_bishop(start[0], start[1])
            self.assertTrue(board.move_piece(start, end))
    
class RookMoves(unittest.TestCase):
    legal_moves = ( ((7,0), (0,0)),
                  )
                  
    def test_legal_moves(self):
        for start, end in self.legal_moves:
            board = chess.Board()
            board.set_rook(start[0], start[1])
            self.assertTrue(board.move_piece(start, end))
    
if __name__ == "__main__":
    unittest.main()