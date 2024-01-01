def emoji(msg):
    words = msg.split(" ")
    out = ''
    emojis = {"love": "❤️", "you": "🫵🏼", "ais": "🍦", ":)": "😁", "Amma": "👱🏻‍"}
    for word in words:
        out += emojis.get(word, word) + " "
    return out


print(emoji("Hi i love you Amma"))
