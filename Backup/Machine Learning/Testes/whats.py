import pywhatkit as kit
from datetime import datetime

now = datetime.now()
hora = now.hour
minuto = now.minute+1

print(f'{hora}:{minuto}')

kit.sendwhatmsg("+5511943483056", "Mensagem enviada", hora, minuto)
