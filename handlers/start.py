from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAEDF6Rgrcl1kZNSrAABqO7L-kVd4tWK48MAAi0BAAIw1J0REIYEuS-exNEeBA")
    await message.reply_text(
        f"""<b> Hey,👋 {message.from_user.first_name}!
\n Groups Music allows you to play music in your groups through the new voice chats recently introduced by Telegram Made Bye @ImTheekshana.e .
\nHit /help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BOT Developer", url="https://t.me/ImTheekshana",
                    )
                ],
                [
                    InlineKeyboardButton(
                       "𝙏𝙃𝙀𝙀𝙆𝙎𝙃𝘼𝙉𝘼 𝘽𝙊𝙏𝙨 Support", url="https://t.me/Theekshana_Support"
                    ),
                    InlineKeyboardButton(
                        " 𝙏𝙃𝙀𝙀𝙆𝙎𝙃𝘼𝙉𝘼 𝙊𝙁𝙁𝙄𝘾𝙄𝘼𝙇 ", url="https://t.me/Theekshana_Official"
                    ),
                    InlineKeyboardButton(
                        "", url="https://t.me/Theekshana_Official"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group 🎙 ", url="https://t.me/TheSaberMusicBot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
          "Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝘽𝙊𝙏𝙨 Support", url="https://t.me/Theekshana_Support"
                    ),
                    InlineKeyboardButton(
                        " 𝙏𝙃𝙀𝙀𝙆𝙎𝙃𝘼𝙉𝘼 𝙊𝙁𝙁𝙄𝘾𝙄𝘼𝙇", url="https://t.me/Theekshana_Official"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hey,{message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
Made By @ImTheekshana And @Pawan_Theekshana
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝘽𝙊𝙏𝙨 Support ", url="https://t.me/Theekshana_Support"
                    ),
                    InlineKeyboardButton(
                        "𝙏𝙃𝙀𝙀𝙆𝙎𝙃𝘼𝙉𝘼 𝙊𝙁𝙁𝙄𝘾𝙄𝘼𝙇", url="https://t.me/Theekshana_Official"
                    )
                ]
            ]
        )
    )    
