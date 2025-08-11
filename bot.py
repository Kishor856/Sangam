import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, ALLOWED_USERS
from utils import extract_course_links

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_USERS:
        await update.message.reply_text("❌ Access Denied!")
        return
    await update.message.reply_text("✅ Bot is running! Send /extract <url> to get links.")

async def extract(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_USERS:
        await update.message.reply_text("❌ Access Denied!")
        return
    if not context.args:
        await update.message.reply_text("Usage: /extract <URL>")
        return
    url = context.args[0]
    links = extract_course_links(url)
    await update.message.reply_text("\n".join(links))

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("extract", extract))

if __name__ == "__main__":
    app.run_polling()
