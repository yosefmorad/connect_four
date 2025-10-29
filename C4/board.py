def create_board (cols:int=7 , rows:int=6) ->list[list[str]]:
    board =  [["|  |"] * cols] * rows

    for row in board:
        print(row)
    print(len(board))
    return board

def column_is_full(broad:list[list[str]] ) ->  bool:
    if " " in broad:
        return False
    return False

def drop_dick(broad:list[list[str]] , col:int ,mark:str):
    if column_is_full(broad):
        return None
    else:
        broad[5][col]= mark
    return broad

print(drop_dick(create_board() ,3 ,"X"))
print(drop_dick(create_board() ,4 ,"X"))
print(drop_dick(create_board() ,4 ,"X"))
print(drop_dick(create_board() ,4 ,"X"))
print(drop_dick(create_board() ,4 ,"X"))
print(drop_dick(create_board() ,4 ,"X"))
print(drop_dick(create_board() ,4 ,"X"))




