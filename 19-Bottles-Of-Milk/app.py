def number_of_bottles():
    lyrics = []
    
    for i in range (99, 0, -1):
        lyrics.append(f"{i} bottles of milk on the wall, {i} bottles of milk.")

        if i - 1 == 0:
            lyrics.append("Take one down and pass it around, no more bottles of milk on the wall. No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            lyrics.append(f"Take one down and pass it around, {i - 1} bottles of milk on the wall.")  
    
    print(' '.join(lyrics))

number_of_bottles()