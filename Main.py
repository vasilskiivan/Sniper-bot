import requests
import time

# Твоят API ключ от API-Football
API_KEY = "6897cc90b1f8d06072d5a11a79a8355e"
TELEGRAM_TOKEN = "8732584803:AAEjAaDEeA0pw2d6GFAEgjBqnRujoh8bKnU"
CHAT_ID = "5448271360"

def send_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

def get_live_matches():
    url = "https://v3.football.api-sports.io/fixtures?live=all"
    headers = {"x-apisports-key": API_KEY}
    return requests.get(url, headers=headers).json()

print("Снайперът е зареден и следи...")

while True:
    try:
        data = get_live_matches()
        for fixture in data.get("response", []):
            minute = fixture["fixture"]["status"]["elapsed"]
            
            # Логика за трите модела
            if 29 <= minute <= 32:
                # Тук добавяме проверка за коефициент и липса на гол
                send_alert(f"🚨 ППГ СИГНАЛ: {fixture['teams']['home']['name']} - {fixture['teams']['away']['name']} (Мин: {minute})")
            
            elif 61 <= minute <= 64:
                send_alert(f"🚨 1,5 В ТОРБАТА: {fixture['teams']['home']['name']} - {fixture['teams']['away']['name']} (Мин: {minute})")
                
            elif 74 <= minute <= 77:
                send_alert(f"🚨 FINNISH HIM: {fixture['teams']['home']['name']} - {fixture['teams']['away']['name']} (Мин: {minute})")

        # Пауза от 5 минути, за да пестим лимита от 100 заявки на ден
        time.sleep(300) 
        
    except Exception as e:
        print(f"Грешка: {e}")
        time.sleep(300)
      
