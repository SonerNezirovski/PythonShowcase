import time
from datetime import datetime, timedelta
from plyer import notification

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
def ders_hatirlatma():
    while True:
        now = datetime.now()
        gun = now.strftime("%A")
        saat = now.strftime("%H:%M")
        if gun in ders_programi:
            for ders in ders_programi[gun]:
                ders_baslangic = datetime.strptime(ders["baslangic"], "%H:%M")
                hatirlatma_zamani = (ders_baslangic - timedelta(minutes=5)).strftime("%H:%M")

                if saat == hatirlatma_zamani:
                    notification.notify(
                        title=f"{ders['ders']} Dersi",
                        message=f"{ders['baslangic']} de başlıyor. Hazırlan!",
                        timeout=10
                    )

                if saat == ders["baslangic"]:
                    notification.notify(
                        title=f"{ders['ders']} Dersi",
                        message="Ders başladı! İyi dersler.",
                        timeout=10
                    )

                if saat == ders["bitis"]:
                    notification.notify(
                        title=f"{ders['ders']} Dersi",
                        message="Ders bitti! Sonunda bitti.",
                        timeout=10
                    )

        time.sleep(30)

ders_hatirlatma()
