#!/usr/bin/env python2.7

import unittest
import chess



class KingMoves(unittest.TestCase):
    '''This tests the legal moves for a king.'''
    legal_moves = ( ((0,3), (0,4)),
                    ((0,3), (1,2)),
                    ((0,3), (1,4)),
                    ((0,3), (0,2)),
                  )
                  
    legal_moves_list = ( ([(5,1)],
                          [(4,0),(5,0),(6,0),(6,1),(6,2),(5,2),(4,2),
                           (4,1)]
                          ),
                        )
    def test_get_legal_moves(self):
        for pieces_list, legal_moves in self.legal_moves_list:
            piece = pieces_list[0]
            board = chess.Board()
            for pawn_coords in pieces_list[1:]:
                board.set_pawn(pawn_coords[0], pawn_coords[1])
            board.set_king(piece[0], piece[1])
            legal_moves_to_test = board.get_legal_moves(piece)
            self.assertItemsEqual(legal_moves, legal_moves_to_test)
    
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
                  
    legal_moves_list = ()
    
    def test_get_legal_moves(self):
        for pieces_list, legal_moves in self.legal_moves_list:
            piece = pieces_list[0]
            board = chess.Board()
            for pawn_coords in pieces_list[1:]:
                board.set_pawn(pawn_coords[0], pawn_coords[1])
            board.set_queen(piece[0], piece[1])
            legal_moves_to_test = board.get_legal_moves(piece)
            self.assertItemsEqual(legal_moves, legal_moves_to_test)
        
    def test_legal_moves(self):
        for start, end in self.legal_moves:
            board = chess.Board()
            board.set_queen(start[0], start[1])
            self.assertTrue(board.move_piece(start, end))

class PawnMoves(unittest.TestCase):
    legal_moves = ( ((6,1), (5,1)),
                    ((6,1), (4,1)),
                  )
    
    legal_moves_list = ()
    
    def test_get_legal_moves(self):
        for pieces_list, legal_moves in self.legal_moves_list:
            piece = pieces_list[0]
            board = chess.Board()
            for pawn_coords in pieces_list[1:]:
                board.set_pawn(pawn_coords[0], pawn_coords[1])
            board.set_pawn(piece[0], piece[1])
            legal_moves_to_test = board.get_legal_moves(piece)
            self.assertItemsEqual(legal_moves, legal_moves_to_test)
        
    def test_legal_moves(self):
        for start, end in self.legal_moves:
            board = chess.Board()
            board.set_pawn(start[0], start[1])
            self.assertTrue(board.move_piece(start, end))
    
class KnightMoves(unittest.TestCase):
    legal_moves = ( ((7,1), (6,3)),
                    ((0,1), (2,0)),
                  )
    
    legal_moves_list = ( ([(0,3)],
                          [(2,2),(2,4),(1,1),(1,5)]
                          ),
                       )
    
    def test_get_legal_moves(self):
        for pieces_list, legal_moves in self.legal_moves_list:
            piece = pieces_list[0]
            board = chess.Board()
            for pawn_coords in pieces_list[1:]:
                board.set_pawn(pawn_coords[0], pawn_coords[1])
            board.set_knight(piece[0], piece[1])
            legal_moves_to_test = board.get_legal_moves(piece)
            self.assertItemsEqual(legal_moves, legal_moves_to_test)
        
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
    
    legal_moves_list = ()
    
    def test_get_legal_moves(self):
        for pieces_list, legal_moves in self.legal_moves_list:
            piece = pieces_list[0]
            board = chess.Board()
            for pawn_coords in pieces_list[1:]:
                board.set_pawn(pawn_coords[0], pawn_coords[1])
            board.set_bishop(piece[0], piece[1])
            legal_moves_to_test = board.get_legal_moves(piece)
            self.assertItemsEqual(legal_moves, legal_moves_to_test)
        
    def test_legal_moves(self):
        for start, end in self.legal_moves:
            board = chess.Board()
            board.set_bishop(start[0], start[1])
            self.assertTrue(board.move_piece(start, end))
    
class RookMoves(unittest.TestCase):
    legal_moves = ( ((7,0), (0,0)),
                  )
                  
    legal_moves_list = ()
    
    def test_get_legal_moves(self):
        for pieces_list, legal_moves in self.legal_moves_list:
            piece = pieces_list[0]
            board = chess.Board()
            for pawn_coords in pieces_list[1:]:
                board.set_pawn(pawn_coords[0], pawn_coords[1])
            board.set_rook(piece[0], piece[1])
            legal_moves_to_test = board.get_legal_moves(piece)
            self.assertItemsEqual(legal_moves, legal_moves_to_test)
        
    def test_legal_moves(self):
        for start, end in self.legal_moves:
            board = chess.Board()
            board.set_rook(start[0], start[1])
            self.assertTrue(board.move_piece(start, end))
    
if __name__ == "__main__":
    unittest.main()