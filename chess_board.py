#!/usr/bin/env python27
# encoding: utf-8
"""
@file:
@brief:

@author:
@coauthor:
@created:
@modified:
"""


class Piece(object):
    pawn = 0
    knight = 1
    bishop = 2
    rook = 3
    queen = 4
    king = 5


class Color(object):
    white = 0
    black = 1


class PieceColor(object):

    def __init__(self, piece, color):
        self.piece = piece
        self.color = color


class Chessboard(object):

    blackPawn = PieceColor(Piece.pawn, Color.black)
    blackRook = PieceColor(Piece.pawn, Color.black)
    blackKnight = PieceColor(Piece.pawn, Color.black)
    blackBishop = PieceColor(Piece.pawn, Color.black)
    blackKing = PieceColor(Piece.pawn, Color.black)
    blackQueen = PieceColor(Piece.pawn, Color.black)
    whitePawn = PieceColor(Piece.pawn, Color.black)
    whiteRook = PieceColor(Piece.pawn, Color.black)
    whiteKnight = PieceColor(Piece.pawn, Color.black)
    whiteBishop = PieceColor(Piece.pawn, Color.black)
    whiteKing = PieceColor(Piece.pawn, Color.black)
    whiteQueen = PieceColor(Piece.pawn, Color.black)

    def __init__(self):
        self.board = [[self.whiteRook, self.whiteKnight, self.whiteBishop, self.whiteKing,
                        self.whiteQueen, self.whiteBishop, self.whiteKnight, self.whiteRook],
                      [self.whitePawn, self.whitePawn, self.whitePawn, self.whitePawn,
                       self.whitePawn, self.whitePawn, self.whitePawn, self.whitePawn],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [self.blackPawn, self.blackPawn, self.blackPawn, self.blackPawn,
                       self.blackPawn, self.blackPawn, self.blackPawn, self.blackPawn],
                      [self.blackRook, self.blackKnight, self.blackBishop, self.blackKing,
                       self.blackQueen, self.blackBishop, self.blackKnight, self.blackRook]]
        self.history = []

    def move(self, start, end):

        def decode_position(position):
            assert len(position) == 2
            return [ord(position[0])-97, int(position[1])-1]

        start = decode_position(start)
        end = decode_position(end)

        piece = self.board[start[1]][start[0]]
        if piece is None:
            return False

        self.history.append([self.board, piece])

        self.board[end[1]][end[0]] = piece
        self.board[start[1]][start[0]] = None

        return True

chess = Chessboard()

chess.move('a1', 'a2')

# print chess.board
print chess.history
