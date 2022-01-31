# Import Stuff
import kahoot

# Global variables
game_code = 0
bot_name = ""
bot_amount = 0
counter = 0
i = 0

# Function to get inputs from user
def get_input():
    global game_code, bot_name, bot_amount
    game_code = input("Enter the Kahoot game code: ")
    bot_name = input("Enter bot name: ")
    bot_amount = input("Enter bot amount: ")

def handle_join():
    print(f"Bot {full_name} joined the Kahoot")

# Letting the bots join with a while loop; they join until the bot_amount is reached
get_input()
bot = kahoot.client()
while int(i) <= int(bot_amount):
    full_name = str(bot_name) + str(i)
    bot.join(game_code, full_name)
    bot.on("Joined", handle_join())
    i += 1