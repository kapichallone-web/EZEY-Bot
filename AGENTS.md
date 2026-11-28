# Project instructions — EZEY-Bot

## About the owner

- **Preferred name:** Kapich Allone (GitHub/Cursor) · also uses **Huot ProsPich** on Railway
- **GitHub:** `kapichallone-web` · repo `EZEY-Bot`
- **Cursor email:** `kapichallone@gmail.com`
- **Railway email:** `huotprospich666@gmail.com`
- **Language:** Khmer first; keep replies short, simple English (or Khmer if asked)
- **Timezone:** Asia/Bangkok (UTC+7)
- **Working style:** Wants agents to **do the deploy**, not only give instructions. Prefer action over long explanations.

## What this project is

Telegram **auto-reply** bot (python-telegram-bot) that:

- Handles `/start`, `/account`, `/contact`
- Shows poster images + Khmer welcome text
- Reply keyboard: account / contact
- Inline button linking to `https://t.me/F7_service` (`@F7_service`)

Public bot display names seen in production include **SaBong24 Resigner** / Builder SB24 (token is for `@EzeyBuilder_bot`).

## Runtime & secrets

- Entry: `bot.py` (also `main.py` → `bot.main()`)
- Config: `config.py` — **requires** `TELEGRAM_TOKEN` or `BOT_TOKEN` from the environment
- **Never** commit tokens or API keys
- Long polling only (`run_polling`); delete stale webhooks if `Conflict` appears
- Only **one** process may poll the same bot token at a time

## Hosting (24/7)

Deployed on **Railway** (Hobby):

| Field | Value |
|-------|--------|
| Project | `rooster-bots` |
| Environment | `production` |
| This bot service | `ezey-bot` |
| Sibling services | `rooster1`, `rooster2` (other bots, **different** tokens) |
| Dashboard | https://railway.com/project/cb3049dd-e5d1-484f-90c2-84d8cf50b00c |

Deploy from repo root (Docker / `python -u bot.py`). Set both `TELEGRAM_TOKEN` and `BOT_TOKEN` on the service (same value).

CLI (when logged in as Huot ProsPich):

```bash
npx railway link -p rooster-bots -e production -s ezey-bot
npx railway up -s ezey-bot -d -y
npx railway logs -s ezey-bot --lines 50
```

## Agent preferences

- Communicate directly and briefly
- Prefer deploying/fixing over documenting alone
- Do not ask the owner to paste secrets in chat; use Railway/Cursor secrets or existing env
- Keep Khmer marketing copy and poster URLs unless the owner asks to change them
- After Railway deploy, stop any local/agent copy of the same bot to avoid `getUpdates` conflicts
