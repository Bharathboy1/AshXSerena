import requests
from SaitamaRobot import dispatcher

from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async


@run_async
def tms(update: Update, context: CallbackContext):
    
    
      parse_mode=ParseMode.MARKDOWN,

                disable_web_page_preview=True,

                reply_markup=InlineKeyboardMarkup
   
        


(
            [
                        InlineKeyboardButton(
                            text="☑️ Add DELIBIRD to your group",
                            url="t.me/{}?startgroup=true".format(
                                context.bot.username))
                    ])
        message.reply_text("hi")
        
    




