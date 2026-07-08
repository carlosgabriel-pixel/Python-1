import datetime

agora = datetime.datetime.now()

# Formata garantindo dois dígitos precedidos por zero se necessário
print(f"Data: {agora.day:02d}/{agora.month:02d}/{agora.year}")
print(f"Hora: {agora.hour:02d}:{agora.minute:02d}")