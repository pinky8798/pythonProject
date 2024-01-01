msg = input('>')
words=msg.split(" ")
out=''
emojis={"love" : "❤️" , "you":"🫵🏼" , "ais":"🍦" ,":)":"😁" , "Amma":"👱🏻‍" }
for word in words:
    out+= emojis.get(word,word) + " "
print(f"Hi \n {out}  \n ahhh shock ayyava!!!")