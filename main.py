from telegram.ext import  *
from telegram import *
from config import PORT,TOKEN


material_1=['BAACAgQAAxkBAANJYdakgsKEg_ZP71nkqWAxa5jTGUIAAokJAALwc-FSZSNAip0tgSUjBA','BAACAgQAAxkBAANKYdakgi_xLMkois-ZMSIjVn-W58IAApgJAALwc-FSEZHmK8cQD8ojBA','BAACAgQAAxkBAANLYdakgiDbNWTkov4FDEkAAeaCUwuFAAKiDQACVJOxUnVspvgsASfOIwQ']

material_3 = ['BAACAgQAAxkBAANoYdc47g9fEWRkI4yyxbhQ8bsqWMUAAsEMAAInONFRK6SjVofD9LQjBA','BAACAgQAAxkBAANpYdc47iPmpmWWppQvKRam68nV2NwAAkwLAAJ7UNlRJo-yhSYOfa8jBA','BAACAgQAAxkBAANqYdc47nZ6hugufWpaZ2Ca7NV1MYAAAnwMAAJ7UNFRRNJFSBPC79cjBA']

material_5 = ['BAACAgQAAxkBAAO9YddOsoXmEW3CMCdDNgy3y6yALbkAAk0LAAJ7UNlRrEIm-0b9DokjBA','BAACAgQAAxkBAAO-YddOskhJN89S_3pcTyjKv_rXSO8AAk4LAAJ7UNlRJ4vjguSv49ojBA','BAACAgQAAxkBAAO_YddOsgahMTbcW2PFgzcb7Z4KTzoAAlQLAAJ7UNlR_oH7J1v2VKUjBA']

def start(update:Update,context:CallbackContext):
	options= [[InlineKeyboardButton('Material of Mechanics',callback_data='material')],[InlineKeyboardButton('Analogue Electronics',callback_data='electronics')],[InlineKeyboardButton('Complex Functions',callback_data='complex')],[InlineKeyboardButton('Electerical Circuite Theory',callback_data='electerical')],[InlineKeyboardButton('Programming Language C',callback_data='programming')],[InlineKeyboardButton('Special Intergrating Functions',callback_data='special')],[InlineKeyboardButton('Drawing [Power-Control] Circuits',callback_data='drawing')]]
	
	
	
	context.bot.send_message(chat_id=update.effective_chat.id,text="Hi bro👋!!\nChoose your courses",reply_markup=InlineKeyboardMarkup(options),parse_mode='Markdown')
	
	
	

def Query(update:Update,context:CallbackContext):
	data = update.callback_query.data
	update.callback_query.answer()
	
#########material###############

	if data == 'material':
		
		buttons = [[InlineKeyboardButton('Lect1',callback_data='material_lec1')],[InlineKeyboardButton('Lect2',callback_data='material_lec2')],[InlineKeyboardButton('Lect3',callback_data='material_lec3')],[InlineKeyboardButton('Lect4',callback_data='material_lec4')],[InlineKeyboardButton('Lect5',callback_data='material_lec5')],[InlineKeyboardButton('Back to home',callback_data='back')]]
		
		update.callback_query.edit_message_text(text='Material of Mechanics Course',reply_markup=InlineKeyboardMarkup(buttons))
		
#########material_1#############

	if data == 'material_lec1':
		
		for i in material_1:
			context.bot.sendVideo(chat_id=update.effective_chat.id,video=f'{i}')
			
		context.bot.sendDocument(chat_id=update.effective_chat.id,document='BQACAgQAAxkBAAIBE2HX0N4HX87yQEkCLAPszArnfe-IAAKDCwACmA1gUkYy8IBmUMAaIwQ')
			
#########material_3#############

	elif data == 'material_lec3':
		
		for i in material_3:
			context.bot.sendVideo(chat_id=update.effective_chat.id,video=f'{i}')
			
		context.bot.sendDocument(chat_id=update.effective_chat.id,document='BQACAgQAAxkBAANrYdc47s3BOxY8YhIrdtKfl1jeSVoAAoULAAKYDWBSvVcB9C6qo2cjBA')
		
#########material_5#############

	elif data == 'material_lec5':
		
		for i in material_5:
			context.bot.sendVideo(chat_id=update.effective_chat.id,video=f'{i}')
			
		context.bot.sendDocument(chat_id=update.effective_chat.id,document='BQACAgQAAxkBAAPAYddOsiENS4f2YFM2PdGi2H-S2mQAAgcLAAIHiVlSPnTzvGmCpPcjBA')

#########back_to_home##########
	
	elif data == 'back':
		options= [[InlineKeyboardButton('Material of Mechanics',callback_data='material')],[InlineKeyboardButton('Analogue Electronics',callback_data='electronics')],[InlineKeyboardButton('Complex Functions',callback_data='complex')],[InlineKeyboardButton('Electerical Circuite Theory',callback_data='electerical')],[InlineKeyboardButton('Programming Language C',callback_data='programming')],[InlineKeyboardButton('Special Intergrating Functions',callback_data='special')],[InlineKeyboardButton('Drawing [Power-Control] Circuits',callback_data='drawing')]]
	
		update.callback_query.edit_message_text("Hi bro 👋!!\nChoose your courses",reply_markup=InlineKeyboardMarkup(options))
		

		
#########Document_id###########
def Document_app(update:Update,context:CallbackContext):
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"'id :\n{update.effective_message.document.file_id}'")
	
#########Video_id###############
def Video_app(update:Update,context:CallbackContext):
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"'id :\n{update.effective_message.video.file_id}'")



def main():
	updater = Updater('5011582345:AAHMjJHyPqUz_OiW90v6TfkmP5Qh1jEfy3Y')
	dispatsher = updater.dispatcher
	##############################
		
	dispatsher.add_handler(CommandHandler('start',start))
	
	dispatsher.add_handler(MessageHandler(Filters.document,Document_app))
	dispatsher.add_handler(MessageHandler(Filters.video,Video_app))
	
	dispatsher.add_handler(CallbackQueryHandler(Query))
		
##############################
	
	updater.start_webhook('0.0.0.0',PORT,TOKEN,webhook_url='https://telegramtest606.herokuapp.com/'+TOKEN)

	updater.idle()
	
##############################
if __name__=='__main__':
	main()
	
