import kahoot

game_code = input('Enter the game code: ')
bot_name = input('Enter the bot name: ')

bot = kahoot.client()
bot.join(game_code, bot_name)
def handle_join():
	print('Bot joined')
bot.on('joined', handle_join())
