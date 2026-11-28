import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    BotCommand,
)
from telegram.constants import ParseMode
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import config

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def post_init(application):
    """Automatically configure Menu Button Commands in Telegram."""
    try:
        commands = [BotCommand(cmd, desc) for cmd, desc in config.BOT_COMMANDS]
        await application.bot.set_my_commands(commands)
        logger.info("Bot menu commands successfully set.")
    except Exception as e:
        logger.error(f"Failed to set bot commands: {e}")


def get_reply_keyboard():
    """Create persistent reply keyboard with 2 buttons."""
    keyboard = [
        [
            KeyboardButton(config.BTN_ACCOUNT),
            KeyboardButton(config.BTN_CONTACT),
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def get_inline_link_keyboard(button_text="👉 ចូលទៅកាន់ @F7_service"):
    """Create inline button linking to https://t.me/F7_service."""
    keyboard = [
        [InlineKeyboardButton(button_text, url=config.CHANNEL_URL)]
    ]
    return InlineKeyboardMarkup(keyboard)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command: sends welcome poster, text, inline link, and keyboard buttons."""
    reply_markup = get_reply_keyboard()
    inline_link = get_inline_link_keyboard("👉 ចូលទៅកាន់ @F7_service")

    try:
        await update.message.reply_photo(
            photo=config.POSTER_WELCOME,
            caption=config.WELCOME_TEXT,
            parse_mode=ParseMode.HTML,
            reply_markup=inline_link,
        )
    except Exception as e:
        logger.error(f"Failed to send welcome poster photo: {e}")
        await update.message.reply_text(
            text=config.WELCOME_TEXT,
            parse_mode=ParseMode.HTML,
            reply_markup=inline_link,
        )

    # Show reply keyboard buttons below
    await update.message.reply_text(
        "👇 សូមជ្រើសរើសជម្រើសខាងក្រោម៖",
        reply_markup=reply_markup,
    )


async def account_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle 1st button / command ('បើកអាខោនFree' / 'បង្កើតអាខោន')."""
    inline_link = get_inline_link_keyboard("🎁 ចុចទីនេះដើម្បីបង្កើតអាខោន (@F7_service)")

    try:
        await update.message.reply_photo(
            photo=config.POSTER_ACCOUNT,
            caption=config.ACCOUNT_TEXT,
            parse_mode=ParseMode.HTML,
            reply_markup=inline_link,
        )
    except Exception as e:
        logger.error(f"Failed to send account poster photo: {e}")
        await update.message.reply_text(
            text=config.ACCOUNT_TEXT,
            parse_mode=ParseMode.HTML,
            reply_markup=inline_link,
        )


async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle 2nd button / command ('ទំំនាក់ទំនងផ្ទាល' / 'ទំនាក់ទំនងផ្ទាល់')."""
    inline_link = get_inline_link_keyboard("💬 ចុចទីនេះដើម្បីទំនាក់ទំនងផ្ទាល់ (@F7_service)")

    try:
        await update.message.reply_photo(
            photo=config.POSTER_CONTACT,
            caption=config.CONTACT_TEXT,
            parse_mode=ParseMode.HTML,
            reply_markup=inline_link,
        )
    except Exception as e:
        logger.error(f"Failed to send contact poster photo: {e}")
        await update.message.reply_text(
            text=config.CONTACT_TEXT,
            parse_mode=ParseMode.HTML,
            reply_markup=inline_link,
        )


async def message_dispatcher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Dispatch user text inputs or button clicks."""
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()
    logger.info(f"Received message from user: '{text}'")

    if config.BTN_ACCOUNT in text or "អាខោន" in text or "បង្កើត" in text or "បើក" in text:
        await account_handler(update, context)
    elif config.BTN_CONTACT in text or "ទំនាក់ទំនង" in text or "ទំំនាក់" in text:
        await contact_handler(update, context)
    else:
        await start_command(update, context)


def main():
    """Initialize and run the Telegram bot."""
    print("==================================================")
    print(" Starting Auto-Reply Bot for @Botteasads_bot")
    print(" Channel Target: https://t.me/F7_service")
    print("==================================================")

    # Ensure an asyncio event loop exists on Python 3.14+
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    application = (
        ApplicationBuilder()
        .token(config.BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler(["account", "create_account"], account_handler))
    application.add_handler(CommandHandler(["contact", "support"], contact_handler))

    # Register message handler for keyboard markup buttons
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_dispatcher)
    )

    print("Bot is active and listening for messages...")
    # Clear any stale webhook so long-polling can receive /start reliably.
    application.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    import asyncio
    from telegram.error import Conflict

    for attempt in range(1, 4):
        try:
            main()
            break
        except Conflict:
            logger.error(
                "Webhook conflict on attempt %s — deleting webhook and retrying...",
                attempt,
            )
            try:
                import urllib.request

                token = config.BOT_TOKEN
                urllib.request.urlopen(
                    f"https://api.telegram.org/bot{token}/deleteWebhook"
                    "?drop_pending_updates=true",
                    timeout=20,
                ).read()
            except Exception as e:
                logger.error("Failed to delete webhook: %s", e)
            if attempt == 3:
                raise
