def isValidChessBoard(chess_dict):
    chess_board = []
    for i in range(1, 9):
        for j in range(97, 105):
            chess_board.append(str(i) + chr(j))

    chess_pieces = ["king", "queen", "knight", "bishop", "rook", "pawn"]
    all_chess_pieces = []
    for i in range(len(chess_pieces)):
        all_chess_pieces.append('w' + chess_pieces[i])
        all_chess_pieces.append('b' + chess_pieces[i])

    chess_dict_keys = list(chess_dict.keys())
    if not all(x in chess_board for x in chess_dict_keys):
        return False

    if "bking" not in chess_dict.values() or "wking" not in chess_dict.values():
        return False

    black_pieces = 0
    white_pieces = 0
    for color in chess_dict.values():
        if color[0] == 'b':
            black_pieces += 1
        elif color[0] == 'w':
            white_pieces += 1

    if black_pieces >= 17 or white_pieces >= 17:
        return False

    black_pawn = 0
    white_pawn = 0

    for pawn in chess_dict.values():
        if pawn == 'bpawn':
            black_pawn += 1
        elif pawn == 'wpawn':
            white_pawn += 1
    if black_pawn >= 9 or white_pawn >= 9:
        return False

    for names in chess_dict.values():
        if names[1:] not in chess_pieces:
            return False

    return True



print(isValidChessBoard({'1h': 'wqueen', '5c': 'bking', '11d': 'wpawn'}))
print(isValidChessBoard({'1h': 'wqueen', '5c': 'bking', '11d': 'wpawn', '2f':'wqueen'}))
print(isValidChessBoard({'1h': 'wqueen', '5c': 'bking', '4d': 'wpawn', '2f':'wking'}))

