import kahoot

counter = 0
name = input("Enter your bots names: ")
code = input("Enter the code: ")


while counter < 10:
    bot = kahoot.client()
    bot.join(code, name + str(counter))
    def joinHandle():
        print("Bot joined")
    bot.on("joined", joinHandle)
    counter += 1
# Tomas ist GAY