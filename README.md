# Telegram Channel Join Request Approver UserBot

A simple Pyrogram-based UserBot written in Python to help you automatically or manually accept pending join requests for your Telegram channel(s).

---

## ✨ Features

* **Approve Pending Requests:** Easily accept users waiting to join your channel.
* **Simple Commands:** Control the approval process with straightforward commands.
* **Flexible Command Prefixes:** Use `.`, `!`, or `/` as command prefixes.
* **Built with Pyrogram:** Leverages the modern and asynchronous Pyrogram library.

---

## 🚀 Prerequisites

Before you begin, ensure you have the following:

1.  **Python 3.7+:** Download from [python.org](https://www.python.org/downloads/).
2.  **Telegram API ID and API Hash:** Obtain these from [my.telegram.org](https://my.telegram.org/apps).
    * Log in with your Telegram account.
    * Go to "API development tools" and fill out the form.
    * You'll receive your `api_id` and `api_hash`. **Keep these confidential!**
    * You are required to generate the pyrogram string session.
3.  **Git:** To clone the repository.

---

## 🛠️ Commands

Once the UserBot is running and you are logged into your Telegram account (the one that is an admin in the target channel), you can use the following commands in any chat with yourself (e.g., Saved Messages) or a specific chat if the bot is configured to listen elsewhere.

**Command Prefixes:** `.`, `!`, `/`

* **To START accepting requests for a channel:**
    * `.run [channel_username_or_id]`
    * `!run [channel_username_or_id]`
    * `/run [channel_username_or_id]`
    * `.approve [channel_username_or_id]`
    * `!approve [channel_username_or_id]`
    * `/approve [channel_username_or_id]`

    *(Note: You might need to specify which channel the bot should work on if it's not hardcoded. If it processes for a pre-configured channel, the `[channel_username_or_id]` part might not be needed.)*

* **To STOP accepting requests:**
    * `.stop`
    * `!stop`
    * `/stop`
    * `.cancel`
    * `!cancel`
    * `/cancel`

---

## ⚠️ Important Notes

* **UserBot Responsibility:** UserBots operate under your personal Telegram account. Use this bot responsibly and be mindful of Telegram's Terms of Service to avoid any restrictions on your account.
* **Rate Limits:** Telegram has API rate limits. If you have a very large number of requests to approve, the bot should ideally handle these gracefully (e.g., with built-in delays).
* **Channel Admin Rights:** The account running the UserBot **must** be an administrator in the target channel with permissions to approve new members.

---

## 🤝 Contributing (Optional)

Contributions, issues, and feature requests are welcome! Feel free to check [issues page]([https://github.com/AbOutMeDK/tgReqAccept/issues]).

---
