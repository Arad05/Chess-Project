from ChessPiece import ChessPiece
from ChessBoard import ChessBoard

class Queen(ChessPiece):

    def __init__(self,name,white):
        super().__init__(name, white)
    
    def __str__(self):
        return super().__str__()
        

    def possibleMoves(self,cordsX,cordsY):
        ret = []
        return ret