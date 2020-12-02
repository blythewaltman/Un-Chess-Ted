from classes.Piece import Piece

class Queen(Piece):
    def create(self, id,  color, position):
        self.id = id
        self.type = "Queen"
        self.color = color
        self.position = position
        self.isCaptured = False


    def getID(self):
        return self.id

    def giveMoveList(self, board):
        moveList = []

        row = self.position[0] + 1
        column = self.position[1]
        blocked = False

        while (row <= 7 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            row = row + 1

        row = self.position[0] - 1
        column = self.position[1]
        blocked = False

        while (row >= 0 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            row = row - 1

        row = self.position[0]
        column = self.position[1] + 1
        blocked = False

        while (column <= 7 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            column = column + 1

        row = self.position[0]
        column = self.position[1] - 1
        blocked = False

        while (column >= 0 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            column = column - 1

        row = self.position[0] + 1
        column = self.position[1] + 1
        blocked = False

        # Check all unblocked spaces diagonal up and right
        while (row <= 7 and column <= 7 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
                row = row + 1
                column = column + 1
            else:
                blocked = True

        row = self.position[0] + 1
        column = self.position[1] - 1
        blocked = False

        # Check all unblocked spaces diagonal up and left
        while (row <= 7 and column >= 0 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
                row = row + 1
                column = column - 1
            else:
                blocked = True

        row = self.position[0] - 1
        column = self.position[1] - 1
        blocked = False

        # Check all unblocked spaces diagonal down and left
        while (row >= 0 and column >= 0 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
                row = row - 1
                column = column - 1
            else:
                blocked = True

        row = self.position[0] - 1
        column = self.position[1] + 1
        blocked = False

        # Check all unblocked spaces diagonal down and right
        while (row >= 0 and column <= 7 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
                row = row - 1
                column = column + 1
            else:
                blocked = True

        return moveList

    def giveCaptureList(self, board):
        captureList = []

        row = self.position[0] + 1
        column = self.position[1]
        blocked = False

        while (row <= 7 and blocked == False):
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            row = row + 1

        row = self.position[0] - 1
        column = self.position[1]
        blocked = False

        while (row >= 0 and blocked == False):
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            row = row - 1

        row = self.position[0]
        column = self.position[1] + 1
        blocked = False

        while (column <= 7 and blocked == False):
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            column = column + 1

        row = self.position[0]
        column = self.position[1] - 1
        blocked = False

        while (column >= 0 and blocked == False):
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            column = column - 1

        row = self.position[0] + 1
        column = self.position[1] + 1
        blocked = False

        # Check all unblocked spaces diagonal up and right
        while (row <= 7 and column <= 7 and blocked == False):
            if (board.getPiece(row, column) != None):
                if (board.getPiece(row, column).getColor() != self.color):
                    captureList.append([row, column])
                    blocked = True
                else:
                    blocked = True
            else:
                row = row + 1
                column = column + 1

        row = self.position[0] + 1
        column = self.position[1] - 1
        blocked = False

        # Check all unblocked spaces diagonal up and left
        while (row <= 7 and column >= 0 and blocked == False):
            if (board.getPiece(row, column) != None):
                if (board.getPiece(row, column).getColor() != self.color):
                    captureList.append([row, column])
                    blocked = True
                else:
                    blocked = True
            else:
                row = row + 1
                column = column - 1

        row = self.position[0] - 1
        column = self.position[1] - 1
        blocked = False

        # Check all unblocked spaces diagonal down and left
        while (row >= 0 and column >= 0 and blocked == False):
            if (board.getPiece(row, column) != None):
                if (board.getPiece(row, column).getColor() != self.color):
                    captureList.append([row, column])
                    blocked = True
                else:
                    blocked = True
            else:
                row = row - 1
                column = column - 1

        row = self.position[0] - 1
        column = self.position[1] + 1
        blocked = False

        # Check all unblocked spaces diagonal down and right
        while (row >= 0 and column <= 7 and blocked == False):
            if (board.getPiece(row, column) != None):
                if (board.getPiece(row, column).getColor() != self.color):
                    captureList.append([row, column])
                    blocked = True
                else:
                    blocked = True
            else:
                row = row - 1
                column = column + 1

        return captureList