import telebot
from telebot import types
import json

TOKEN = '8355160126:AAEl-Ul_QLI1I7AwkHPfE1_r4a2MUC0MISU'
ADMIN_ID = "8213048876" #A
CHANNEL_ID = -1001574709061 #Usavyb

bot = telebot.TeleBot(TOKEN)

# bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
# bot.timeout = 60


# ====================== DB YUKLASH ============================
try:
    with open("db.json", "r", encoding="utf-8") as f:
        db = json.load(f)
except:
    db = {}
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4)

# =================== STATE (HOLAT) ============================
state = {}  
# state[user_id] = ["waiting_for_video"]
# state[user_id] = ["waiting_for_code", file_id]
# state[user_id] = ["waiting_for_delete"]

# =================== OBUNA TEKSHIRISH =========================
def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False


# =================== ADMIN PANEL =============================
def admin_panel(chat_id):
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add("🎬 Kino yuklash", "📂 Film ro'yxati")
    btn.add("❌ Film o'chirish", "🔙 Ortga")
    btn.add("📢 Xabar yuborish")
    bot.send_message(chat_id, "🔐 Admin Paneli", reply_markup=btn)


# ====================== START ================================
def save_user(msg):
    user_id=msg.from_user.id
    
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except:
        users = []

    if user_id not in users:
        users.append(user_id)
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

@bot.message_handler(commands=['start'])

def start(msg):
    user = msg.from_user.id
    
    save_user(msg)

    if not check_sub(user):
        btn = types.InlineKeyboardMarkup()
        btn.add(types.InlineKeyboardButton("📌 Kanalga obuna bo'lish", url="https://t.me/USAVYBE"))
        btn.add(types.InlineKeyboardButton("♻️ Tekshirish", callback_data="check"))
        
        bot.send_message(
            msg.chat.id,
            "❗ Botdan foydalanish uchun kanalga obuna bo'ling!",
            reply_markup=btn
        )
        return


    bot.send_message(msg.chat.id, "🎬 Kino kodini kiriting:")

@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):
    if check_sub(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "✔ Obuna tasdiqlandi!\n\nKino kodini yuboring:")
    else:
        bot.answer_callback_query(call.id, "❗ Hali obuna bo‘lmagansiz!")

# ====================== ADMIN PANEL ===========================
@bot.message_handler(commands=['panel'])
def panel(msg):
    if str(msg.from_user.id) == ADMIN_ID:
        admin_panel(msg.chat.id)
    else:
        bot.send_message(msg.chat.id, "❌ Siz admin emassiz.")

# ====================== ORTGA QAYTISH =========================
@bot.message_handler(func=lambda msg: msg.text == "🔙 Ortga")
def back(msg):
    if str(msg.from_user.id) != ADMIN_ID:
        return
    state.pop(str(msg.from_user.id), None)
    bot.send_message(msg.chat.id, "🎬 Kino kodini kiriting:", reply_markup=types.ReplyKeyboardRemove())
    
# ====================== KINO YUKLASH ==========================
@bot.message_handler(func=lambda msg: msg.text == "🎬 Kino yuklash")
def upload_movie(msg):
    if str(msg.from_user.id) != ADMIN_ID:
        return

    bot.send_message(msg.chat.id, "🎬 Video yuboring (video fayl ko‘rinishida).")
    state[str(msg.from_user.id)] = ["waiting_for_video"]

# ======== KINO KODINI QABUL QILISH ========
@bot.message_handler(content_types=['video'])
def catch_video(msg):
    user = str(msg.from_user.id)

    if user in state and state[user][0] == "waiting_for_video":
        file_id = msg.video.file_id
        state[user] = ["waiting_for_code", file_id]
        bot.send_message(msg.chat.id, "📌 Kino uchun kod kiriting:")

# ======== KINO NOMI ========
@bot.message_handler(func=lambda msg: str(msg.from_user.id) in state and state[str(msg.from_user.id)][0] == "waiting_for_code")
def movie_code(msg):
    user = str(msg.from_user.id)
    file_id = state[user][1]
    code = msg.text.strip()

    state[user] = ["waiting_for_name", file_id, code]
    bot.send_message(msg.chat.id, "🎬 Kino nomini kiriting:")

# ======== KINO JANRI ========
@bot.message_handler(func=lambda msg: str(msg.from_user.id) in state and state[str(msg.from_user.id)][0] == "waiting_for_name")
def movie_name(msg):
    user = str(msg.from_user.id)
    file_id = state[user][1]
    code = state[user][2]
    name = msg.text.strip()

    state[user] = ["waiting_for_genre", file_id, code, name]
    bot.send_message(msg.chat.id, "📚 Kino janrini kiriting:")


@bot.message_handler(func=lambda msg: str(msg.from_user.id) in state and state[str(msg.from_user.id)][0] == "waiting_for_genre")
def movie_genre(msg):
    user = str(msg.from_user.id)
    file_id = state[user][1]
    code = state[user][2]
    name = state[user][3]
    genre = msg.text.strip()

    state[user] = ["waiting_for_url", file_id, code, name, genre]
    bot.send_message(msg.chat.id, "💽Formati:")


# ======== KINO URL / INFO ========
@bot.message_handler(func=lambda msg: str(msg.from_user.id) in state and state[str(msg.from_user.id)][0] == "waiting_for_url")
def movie_url(msg):
    user = str(msg.from_user.id)
    file_id = state[user][1]
    code = state[user][2]
    name = state[user][3]
    genre = state[user][4]
    formati= msg.text.strip()

    # JSON ga saqlash ko‘rinishi:
    db[code] = {
        "file_id": file_id,
        "name": name,
        "formati": formati,
        "genre": genre,
        "url": "@dubHDkinolar",
        "urlbot":"@DubKinoBot"
    }

    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4, ensure_ascii=False)

    bot.send_message(msg.chat.id, "✅ Kino muvaffaqiyatli qo‘shildi!")

    del state[user]


#============ADMIN XABARI===========
@bot.message_handler(func=lambda msg: msg.text == "📢 Xabar yuborish")
def ask_broadcast(msg):
    if str(msg.from_user.id) != ADMIN_ID:
        return

    bot.send_message(msg.chat.id, "📢 Yuboriladigan xabarni kiriting:")
    state[str(msg.from_user.id)] = ["admin_broadcast"]


@bot.message_handler(content_types=[
    'text','photo','video','document','audio','voice','sticker','animation'
])
def do_broadcast(msg):

    user = str(msg.from_user.id)

    # ❗ faqat admin va broadcast rejimida ishlaydi
    if user not in state:
        return
    if state[user] != "admin_broadcast":
        return

    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except:
        users = []
    
    count=0
    for user_id in users:
        try:
            bot.forward_message(user_id, msg.chat.id, msg.message_id)
            count += 1
        except:
            pass

    bot.send_message(msg.chat.id, f"✅ Xabar {count} ta foydalanuvchiga yuborildi!")
    del state[user]


# ====================== FILM O‘CHIRISH ========================
@bot.message_handler(func=lambda msg: msg.text == "❌ Film o'chirish")
def delete_movie(msg):
    if str(msg.from_user.id) != ADMIN_ID:
        return
    state[str(msg.from_user.id)] = ["waiting_for_delete"]
    bot.send_message(msg.chat.id, "❌ O‘chirmoqchi bo‘lgan kino kodini yuboring.")

# ====================== FILM RO‘YXATI =========================
@bot.message_handler(func=lambda msg: msg.text == "📂 Film ro'yxati")
def movie_list(msg):
    if str(msg.from_user.id) != ADMIN_ID:
        return
    if not db:
        bot.send_message(msg.chat.id, "📂 Bazada kino yo'q.")
        return
    text = "🎬 *Kino ro‘yxati:*\n\n"
    c=1
    for code, info in db.items():
        text += f"• {c}) {info['name']}--------#{code}\n"
        c+=1
    bot.send_message(msg.chat.id, text, parse_mode="Markdown")
# ====================== UMUMIY HANDLER ========================
@bot.message_handler(func=lambda msg: True)
def universal_handler(msg):
    user = msg.from_user.id
    text = msg.text.strip()

    # # --- 1) Admin kino kodi kiritayapti ---
    # if user in state and state[user][0] == "waiting_for_code":
    #     file_id = state[user][1]
    #     db[text] = file_id

    #     with open("db.json", "w", encoding="utf-8") as f:
    #         json.dump(db, f, indent=4)

    #     bot.send_message(msg.chat.id, f"✔ Kino saqlandi!\nKino kodi: {text}")
    #     del state[user]
    #     return

    # # --- 2) Admin kino o‘chirayapti ---
    # if user in state and state[user][0] == "waiting_for_delete":
    #     if text in db:
    #         del db[text]
    #         with open("db.json", "w", encoding="utf-8") as f:
    #             json.dump(db, f, indent=4)
    #         bot.send_message(msg.chat.id, "✔ Kino o‘chirildi.")
    #     else:
    #         bot.send_message(msg.chat.id, "❌ Bunday kod mavjud emas.")
    #     del state[user]
    #     return

    # --- 3) Oddiy foydalanuvchi kino kodi so‘rayapti ---
    if not check_sub(user):
        bot.send_message(msg.chat.id, "❗ Avval kanalga obuna bo‘ling.")
        return

    if text in db:
        movie = db[text]       # DICT
        file_id = movie["file_id"]
        #code=text 
        keys = [k for k, v in db.items() if v == movie] # shu koddan foydalanib,
        key = keys[0] if keys else None                 # kalitni chiqardim.
        
        bot.send_video(
            msg.chat.id,
            file_id,
            caption=f"🎬 {movie['name']} \n\t\t-------------------------\n"
                    f"💽Formati:{movie['formati']}\n"
                    f"🎞Janri: {movie['genre']}\n"
                    f"🆔Kod: #{key}\n" #ishladi
                    f"\n📹Kanalimiz: {movie['url']}\n"
                    f"🤖Bizning Bot: {movie['urlbot']}"
        )
    else:
        bot.send_message(msg.chat.id, "❌ Bunday kod bo‘yicha kino topilmadi.")

    # if text in db:
    #     bot.send_video(msg.chat.id, db[text])
    # else:
    #     bot.send_message(msg.chat.id, "❌ Bunday kod bo‘yicha kino topilmadi.")

# ==============================================================#
bot.polling(none_stop=True, timeout=60, long_polling_timeout=60)

#bot.polling()


# while True:
#     try:
#         bot.polling(non_stop=True, timeout=60, long_polling_timeout=60)
#     except requests.exceptions.ReadTimeout:
#         print("⚠️ ReadTimeout — bot qayta ishga tushmoqda...")
#         time.sleep(1)
#         continue
#     except requests.exceptions.ConnectionError:
#         print("⚠️ ConnectionError — internet uzildi. Qayta urinish...")
#         time.sleep(2)
#         continue
#     except Exception as e:
#         print("❗ Noma'lum xatolik:", e)
#         time.sleep(2)
#         continue