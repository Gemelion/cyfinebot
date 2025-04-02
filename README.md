
# CyfineBot — Telegram штраф-бот для Кипра

## 🛠️ Установка и деплой на Render

1. Создай новый **Web Service** на [https://render.com](https://render.com)
2. Укажи репозиторий с этими файлами или загрузи вручную

### ⚙️ Настройки

- **Build Command:**
  ```bash
  pip install -r requirements.txt
  ```

- **Start Command:**
  ```bash
  uvicorn bot_webhook:app --host 0.0.0.0 --port 10000
  ```

- **Environment Variables:**

| Key           | Value                                  |
|----------------|----------------------------------------|
| `BOT_TOKEN`    | ваш токен Telegram-бота               |
| `WEBHOOK_URL`  | например: https://cyfinebot.onrender.com |
| `SECRET_KEY`   | (опционально) ключ шифрования или оставить пустым |

---

## 🔐 GDPR

- Все данные шифруются
- Пользователь даёт явное согласие
- Есть встроенные команды:
  - `/info` — права пользователя
  - `/contact` — запрос на удаление
  - `/admin`, `/deluser` — для владельца
