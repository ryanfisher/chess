#!/usr/bin/env python2.7

import math
DEFAULT_TEAM1 = "White"
DEFAULT_TEAM2 = "Black"


class Board(object):
    '''
    Describes the chess board. Represented by an array of arrays,
    each of length 8.
    '''

    class _Piece(object):
        '''
        Parent class for all pieces.
        '''
    
        def __init__(self, team):
            self.team = team
        
    class _Queen(_Piece):
    
        def __init__(self, team):
            self.team = team
        
        def get_legal_moves(self, start, board):
            '''
            Returns a list of all possible moves the queen at position
            start can legally make given the context of the board.
            This functions similarly in all other pieces.
            
            Return element takes form [(row,col),(row,col)] where
            (row,col) is a legal ending spot and the list can contain
            any number of possible tuples.
            '''
            possible_moves = []
            for row in range(8):
                for col in range(8):
                    if self.is_legal_move(start, (row, col), board):
                        possible_moves.append((row, col))
            return possible_moves
        
        def is_legal_move(self, start, end, board):
            '''
            Returns True if the move from start to end is legal given
            the context of the board. Otherwise, returns False.
            '''
            
            #Checks if a piece on the same team is blocking
            if (board[end[0]][end[1]] is not None and
                board[end[0]][end[1]].team == self.team):
                return False
            #If moving within the same row
            if start[0] == end[0]:
                if start[1] < end[1]:
                    col_step = 1
                else:
                    col_step = -1
                for col in range(start[1], end[1], col_step):
                    if (board[start[0]][col] is not None and
                        board[start[0]][col] != board[start[0]][start[1]]):
                        return False
                return True
            #If moving within the same column
            elif start[1] == end[1]:
                if start[0] < end[0]:
                    row_step = 1
                else:
                    row_step = -1
                for row in range(start[0], end[0], row_step):
                    if (board[row][start[1]] is not None and
                        board[row][start[1]] != board[start[0]][start[1]]):
                        return False
                return True
            #If move is not diagonal
            elif math.fabs(start[0] - end[0]) != math.fabs(start[1] - end[1]):
                return False
            #If move is diagonal
            else:
                row_step = -1
                col_step = -1
                if start[0] < end[0]: row_step = 1
                if start[1] < end[1]: col_step = 1
                for row, col in zip(range(start[0], end[0], row_step),
                                    range(start[1], end[1], col_step)):
                    if (board[row][col] is not None and
                        board[row][col] != board[start[0]][start[1]]):
                        return False
                if board[end[0]][end[1]] is None:
                    return True
                elif board[end[0]][end[1]].team == self.team:
                    return False
                else:
                    return True
        
    class _King(_Piece):
    
        def __init__(self, team):
            self.team = team
            
        def get_legal_moves(self, start, board):               
            possible_moves = []
            for row in range(8):
                for col in range(8):
                    if self.is_legal_move(start, (row, col), board):
                        possible_moves.append((row, col))
            return possible_moves
            
        def is_legal_move(self, start, end, board):
            if (board[end[0]][end[1]] is not None and
                board[end[0]][end[1]].team == self.team):
                return False
            if (math.fabs(start[0] - end[0]) > 1 or
                math.fabs(start[1] - end[1]) > 1):
                return False
            else:
                return True
        
    class _Pawn(_Piece):

        def __init__(self, team):
            self.team = team
        
        def get_legal_moves(self, start, board):
            possible_moves = []
            for row in range(8):
                for col in range(8):
                    if self.is_legal_move(start, (row, col), board):
                        possible_moves.append((row, col))
            return possible_moves
            
        def is_legal_move(self, start, end, board):
            #end_piece is piece currently in desired end location
            end_piece = board[end[0]][end[1]]
            # if the end spot is empty
            if end_piece is None:
                if end[1] != start[1]:
                    return False
                elif self.team == DEFAULT_TEAM1:
                    if start[0] - end[0] == 1:
                        return True
                    elif start[0] - end[0] == 2 and start[0] == 6:
                        return True
                    else:
                        return False
                else:
                    if end[0] - start[0] == 1:
                        return True
                    elif end[0] - start[0] == 2 and start[0] == 1:
                        return True
                    else:
                        return False
            elif end_piece.team == self.team:
                return False
            else:
                if math.fabs(start[1] - end[1]) != 1:
                    return False
                elif self.team == DEFAULT_TEAM1:
                    if start[0] - end[0] == 1:
                        return True
                    else:
                        return False
                else:
                    if end[0] - start[0] == 1:
                        return True
                    else:
                        return False
        
    class _Rook(_Piece):
        
        def __init__(self, team):
            self.team = team
        
        def get_legal_moves(self, start, board):
            possible_moves = []
            for row in range(8):
                for col in range(8):
                    if self.is_legal_move(start, (row, col), board):
                        possible_moves.append((row, col))
            return possible_moves
            
        def is_legal_move(self, start, end, board):
            if (board[end[0]][end[1]] is not None and
                board[end[0]][end[1]].team == self.team):
                return False
            if start[0] == end[0]:
                if start[1] < end[1]:
                    col_step = 1
                else:
                    col_step = -1
                for col in range(start[1], end[1], col_step):
                    if (board[start[0]][col] is not None and
                        board[start[0]][col] != board[start[0]][start[1]]):
                        return False
                return True
            elif start[1] == end[1]:
                if start[0] < end[0]:
                    row_step = 1
                else:
                    row_step = -1
                for row in range(start[0], end[0], row_step):
                    if (board[row][start[1]] is not None and
                        board[row][start[1]] != board[start[0]][start[1]]):
                        return False
                return True
            else:
                return False
                
    class _Knight(_Piece):
        
        def __init__(self, team):
            self.team = team
        
        def get_legal_moves(self, start, board):
            possible_moves = []
            for row in range(8):
                for col in range(8):
                    if self.is_legal_move(start, (row, col), board):
                        possible_moves.append((row, col))
            return possible_moves
            
        def is_legal_move(self, start, end, board):
            if (board[end[0]][end[1]] is not None and
                board[end[0]][end[1]].team == self.team):
                return False
            if (math.fabs(start[0] - end[0]) == 2 and
                math.fabs(start[1] - end[1]) == 1):
                return True
            elif (math.fabs(start[0] - end[0]) == 1 and
                  math.fabs(start[1] - end[1]) == 2):
                return True
            else:
                return False
            
    class _Bishop(_Piece):
    
        def __init__(self, team):
            self.team = team
        
        def get_legal_moves(self, start, board):
            possible_moves = []
            for row in range(8):
                for col in range(8):
                    if self.is_legal_move(start, (row, col), board):
                        possible_moves.append((row, col))
            return possible_moves
            
        def is_legal_move(self, start, end, board):
            if (board[end[0]][end[1]] is not None and
                board[end[0]][end[1]].team == self.team):
                return False
            if math.fabs(start[0] - end[0]) != math.fabs(start[1] - end[1]):
                return False
            else:
                row_step = -1
                col_step = -1
                if start[0] < end[0]: row_step = 1
                if start[1] < end[1]: col_step = 1
                for row, col in zip(range(start[0], end[0], row_step),
                                    range(start[1], end[1], col_step)):
                    if (board[row][col] is not None and
                        board[row][col] != board[start[0]][start[1]]):
                        return False
                if board[end[0]][end[1]] is None:
                    return True
                elif board[end[0]][end[1]].team == self.team:
                    return False
                else:
                    return True
        
    def __init__(self):    
        self.board = []
        for j in range(8):
            row = []
            for i in range(8):
                row.append(None)
            self.board.append(row)
        
    def _set_piece(self, piece, row, col):
        self.board[row][col] = piece
    
    def set_board(self, team1=DEFAULT_TEAM1, team2=DEFAULT_TEAM2):
        """
        Sets board for a standard chess game where teams names
        for individual pieces are defined by team1 and team2.
        """
        self._set_piece(self._Rook(team1), 7, 0)
        self._set_piece(self._Rook(team2), 0, 0)
        self._set_piece(self._Rook(team2), 0, 7)
        self._set_piece(self._Rook(team1), 7, 7)
        self._set_piece(self._Knight(team1), 7, 1)
        self._set_piece(self._Knight(team1), 7, 6)
        self._set_piece(self._Knight(team2), 0, 1)
        self._set_piece(self._Knight(team2), 0, 6)
        self._set_piece(self._Bishop(team1), 7, 2)
        self._set_piece(self._Bishop(team1), 7, 5)
        self._set_piece(self._Bishop(team2), 0, 2)
        self._set_piece(self._Bishop(team2), 0, 5)
        self._set_piece(self._Queen(team2), 0, 3)
        self._set_piece(self._Queen(team1), 7, 3)
        self._set_piece(self._King(team2), 0, 4)
        self._set_piece(self._King(team1), 7, 4)
        for i in range(8):
            self._set_piece(self._Pawn(team1), 6, i)
            self._set_piece(self._Pawn(team2), 1, i)
        return True
            
    def move_piece(self, start, end):
        '''
        Moves piece at start location to end location. start and end
        must be tuples. If move is legal return True, otherwise return
        False.
        '''
        piece = self.board[start[0]][start[1]]
        if piece.is_legal_move(start, end, self.board):
            self.board[start[0]][start[1]] = None
            self.board[end[0]][end[1]] = piece
            return True
        else:
            return False
    
    def get_legal_moves(self, position):
        '''
        Returns of a list of locations the piece at position can
        legally move to. Position must be a tuple of coordinates
        on the board. The returned list will contained tuples of
        all coordinates the piece at position can move to.
        '''
        piece = self.board[position[0]][position[1]]
        return piece.get_legal_moves(position, self.board)
    
    def check_moves(self, moves, team):
        '''
        Takes a list of moves and checks if a piece is blocking
        the moves. At which point it cuts the list off and returns
        the cut off list. If the the piece that cuts off the list
        is the same as the team parameter, that move is not included.
        Otherwise the move is included.
        '''
        valid = []
        for move in moves:
            if board[move[0]][move[1]] is None:
                valid.append(move)
            elif board[move[0]][move[1]].team == team:
                return valid
            else:
                valid.append(move)
                return valid
        return valid
            
    def display(self):
        print self.board
        
    def set_queen(self, row, col, team=DEFAULT_TEAM1):
        self._set_piece(self._Queen(team), row, col)
        
    def set_king(self, row, col, team=DEFAULT_TEAM1):
        self._set_piece(self._King(team), row, col)
        
    def set_rook(self, row, col, team=DEFAULT_TEAM1):
        self._set_piece(self._Rook(team), row, col)
        
    def set_knight(self, row, col, team=DEFAULT_TEAM1):
        self._set_piece(self._Knight(team), row, col)
        
    def set_bishop(self, row, col, team=DEFAULT_TEAM1):
        self._set_piece(self._Bishop(team), row, col)
        
    def set_pawn(self, row, col, team=DEFAULT_TEAM1):
        self._set_piece(self._Pawn(team), row, col)