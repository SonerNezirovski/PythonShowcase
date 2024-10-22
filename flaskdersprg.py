from flask import Flask, jsonify
from datetime import datetime, timedelta
import threading
import time
from plyer import notification

app = Flask(__name__)

# Ders programı
ders_programi = {
    "Monday": [
        {"ders": "Fizik (IX^2)", "baslangic": "09:45", "bitis": "10:25"},
        {"ders": "Matematik (VII^2)", "baslangic": "10:30", "bitis": "11:10"},
        {"ders": "Programlama (IX^2)", "baslangic": "11:15", "bitis": "11:55"},
        {"ders": "Kimya (VIII^2)", "baslangic": "12:00", "bitis": "12:40"},
        {"ders": "Matematik (VI^2)", "baslangic": "12:45", "bitis": "13:25"},
    ],
    "Tuesday": [
        {"ders": "Italyanca (VIII^1)", "baslangic": "11:15", "bitis": "11:55"},
        {"ders": "Matematik (VI^2)", "baslangic": "12:00", "bitis": "12:40"},
        {"ders": "Kimya (VIII^2)", "baslangic": "12:45", "bitis": "13:25"},
    ],
    "Wednesday": [
        {"ders": "Kimya (IX^2)", "baslangic": "08:00", "bitis": "08:40"},
        {"ders": "Matematik (VII^2)", "baslangic": "08:45", "bitis": "09:25"},
        {"ders": "Matematik (VI^2)", "baslangic": "10:30", "bitis": "11:10"},
        {"ders": "Fizik (VIII^2)", "baslangic": "11:15", "bitis": "11:55"},
        {"ders": "Fizik (IX^2)", "baslangic": "12:00", "bitis": "12:40"},
        {"ders": "Programlama (IX^2)", "baslangic": "12:45", "bitis": "13:25"},
    ],
    "Thursday": [
        {"ders": "Matematik (VI^2)", "baslangic": "11:15", "bitis": "11:55"},
        {"ders": "Matematik (VII^1)", "baslangic": "12:00", "bitis": "12:40"},
        {"ders": "Informatik (VII^2)", "baslangic": "12:45", "bitis": "13:25"},
    ],
    "Friday": [
        {"ders": "Matematik (VII^2)", "baslangic": "08:45", "bitis": "09:25"},
        {"ders": "Italyanca (VIII^1)", "baslangic": "10:30", "bitis": "11:10"},
        {"ders": "Matematik (VI^2)", "baslangic": "11:15", "bitis": "11:55"},
        {"ders": "Kimya (IX^2)", "baslangic": "12:00", "bitis": "12:40"},
        {"ders": "Kimya (VIII^2)", "baslangic": "12:45", "bitis": "13:25"},
    ]
}
def send_notifications():
    while True:
        now = datetime.now()
        gun = now.strftime("%A")
        saat = now.strftime("%H:%M")

        if gun not in ders_programi.keys():
            time.sleep(30)
            continue

        gun_adi = {
            "Monday": "Pazartesi",
            "Tuesday": "Salı",
            "Wednesday": "Çarşamba",
            "Thursday": "Perşembe",
            "Friday": "Cuma"
        }[gun]

        if gun_adi in ders_programi:
            for ders in ders_programi[gun_adi]:
                ders_baslangic = datetime.strptime(ders["baslangic"], "%H:%M")
                hatirlatma_zamani = (ders_baslangic - timedelta(minutes=5)).strftime("%H:%M")

                if saat == hatirlatma_zamani:
                    notification.notify(
                        title=f"{ders['ders']} Dersi",
                        message=f"{ders['baslangic']} de başlıyor. Hazırlan!",
                        timeout=10
                    )

        time.sleep(30)