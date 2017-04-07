# tg-forwarder
Service for forwarding messages to Telegram


Usage:


curl -i -H "Content-Type: application/json" -X POST -d '{"text":"YOUR MESSAGE", "chatid":"CHATID", "token":"BOTFATHER_GENERATED_TOKEN"}' http://127.0.0.1:8079
