def sing():
    lyrics = []

    for number in range(1,13):
        if number == 5:
            lyrics.append("whisper words of wisdom")
        elif number == 11:
            lyrics.append("there will be an answer")
        else:
            lyrics.append("let it be")

    print(', '.join(lyrics))

sing()