"""All available constants for this bot."""

from tgbot.misc import Tariff

SIGNUP_PAGE = "https://pavloshutz.github.io/signup-page/"

DATABASE = "lifecell_db.db"

BOT_INFO = """
🖐 Привіт і вітаю тебе у <b>Lifecell Тариф</b> боті!
Тут у тебе буде нагода обрати під себе саме той тариф від Lifecell
який підходитиме саме для тебе.
❗ Для того, аби користуватися моїми послугами, тобі варто зареєструватися.
"""

DEFAULT_BOT_TEXT = """
Обирай тарифний план, який підходитиме саме тобі!\n
Ось 📜 список доступних команд :\n
    /start         Запустити бота
    /choose     Обрати вигідний тариф для себе
"""


potuzhnyy = Tariff(weeks=4, internet=40, calls=float('inf'), price=100)
int_bezmezh = Tariff(weeks=4, internet=float('inf'), calls=250, price=100)
dzvinkiy = Tariff(weeks=4, internet=None, calls=float('inf'), price=100)
vilniy_life_reg = Tariff(weeks=4, internet=float('inf'), calls=1600, price=150)
vilniy_life = Tariff(weeks=4, internet=float('inf'), calls=1600, price=180)
smart_life = Tariff(weeks=4, internet=25, calls=800, price=120)
prosto_life = Tariff(weeks=4, internet=8, calls=300, price=90)
platinum_life = Tariff(weeks=4, internet=float('inf'), calls=3000, price=250)
shkilniy = Tariff(weeks=4, internet=7, calls=float('inf'), price=150)
gadget_bezpeka = Tariff(weeks=12, internet=0.15, calls=15, price=90)
gadget_smart21 = Tariff(weeks=4, internet=0.5, calls=50, price=150)
gadget_tab21 = Tariff(weeks=4, internet=50, calls=None, price=275)
gadget_rout21 = Tariff(weeks=4, internet=float('inf'), calls=None, price=375)
smart_family_s = Tariff(weeks=4, internet=20, calls=500, price=375)
smart_family_m = Tariff(weeks=4, internet=30, calls=750, price=425)
smart_family_l = Tariff(weeks=4, internet=50, calls=1500, price=500)
