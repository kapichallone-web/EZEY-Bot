import os

# Configuration for Telegram Auto Reply Bot (@Botteasads_bot)

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN") or os.getenv("TELEGREAM_TOKEN") or os.getenv("BOT_TOKEN", "8828926827:AAGTC0Mc3UV0NMiwNLC8Du6wbxiHDdzvINg")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AQ.Ab8RN6JkVEgPsl-bxbODU0yWQ35RHnNa9NyVqCB8B97KvrOhmw")
CHANNEL_URL = "https://t.me/F7_service"
CHANNEL_HANDLE = "@F7_service"

# Poster Image Links
POSTER_WELCOME = "https://plain-apac-prod-public.komododecks.com/202608/01/jRYAXnQgz6SUkTRmvH6S/image.png"
POSTER_ACCOUNT = "https://plain-apac-prod-public.komododecks.com/202608/05/JxXKbCEqDKvcU6nDcUQf/image.png"
POSTER_CONTACT = "https://plain-apac-prod-public.komododecks.com/202608/05/tCG5s28k1PK2dA1h7k27/image.png"

# Texts (Using HTML formatting for Telegram stability)
WELCOME_TEXT = (
    "<b>🎉 សូមស្វាគមន៍មកកាន់ (@F7_service)</b>\n\n"
    "✅ ផ្តល់សេវាកម្មរហ័សទាន់ចិត្ត 24/7 ✅ មានទំនុកចិត្ត និង សុវត្ថិភាពខ្ពស់\n"
    "👉 សូមជ្រើសរើសប៊ូតុងខាងក្រោមដើម្បីបង្កើតអាខោន ឬ ទំនាក់ទំនងផ្ទាល់៖"
)

ACCOUNT_TEXT = (
    "<b>🎉 សូមស្វាគមន៍មកកាន់ (@F7_service)</b>\n\n"
    "<b>🎁 បង្កើតអាខោនFree</b>\n"
    "✅ ផ្តល់សេវាកម្មរហ័សទាន់ចិត្ត 24/7 ✅ មានទំនុកចិត្ត និង សុវត្ថិភាពខ្ពស់\n\n"
    "👉 សូមចុចប៊ូតុងខាងក្រោមដើម្បីចូលទៅកាន់ @F7_service បង្កើតអាខោនដោយឥតគិតថ្លៃ!"
)

CONTACT_TEXT = (
    "<b>🎉 សូមស្វាគមន៍មកកាន់ (@F7_service)</b>\n\n"
    "<b>💬 ទំនាក់ទំនងផ្ទាល់</b>\n"
    "✅ ផ្តល់សេវាកម្មរហ័សទាន់ចិត្ត 24/7 ✅ មានទំនុកចិត្ត និង សុវត្ថិភាពខ្ពស់\n\n"
    "👉 សូមចុចប៊ូតុងខាងក្រោមដើម្បីទំនាក់ទំនងផ្ទាល់ជាមួយ @F7_service!"
)

# Button Labels (exact matching for user clicks)
BTN_ACCOUNT = "បើកអាខោនFree"
BTN_CONTACT = "ទំំនាក់ទំនងផ្ទាល"

# Menu Commands Setup
BOT_COMMANDS = [
    ("start", "🎉 ចាប់ផ្តើម (Start Bot)"),
    ("account", "🎁 បង្កើតអាខោនFree"),
    ("contact", "💬 ទំនាក់ទំនងផ្ទាល់"),
]
