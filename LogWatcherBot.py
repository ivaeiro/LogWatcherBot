import asyncio
import re
from datetime import datetime
from telegram import Bot

# Configuración del bot
BOT_TOKEN = 'TU-BOT-TOKEN'
CHAT_ID = 'TU-ID-CHAT'

bot = Bot(token=BOT_TOKEN)

async def enviar_alerta(servicio, ip_origen, estado, hora):
    mensaje = f"""🚨 *Alerta Seguridad*
Servicio: `{servicio}`
Estado: `{estado}`
IP origen: `{ip_origen}`
Hora: `{hora}`"""

    await bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')


# Monitoreo SSH (auth.log)
async def monitorear_ssh():
    with open('/var/log/auth.log', 'r') as log:
        log.seek(0, 2)
        while True:
            linea = log.readline()
            if not linea:
                await asyncio.sleep(1)
                continue

            m_ok = re.search(r'Accepted (\w+) for .* from (\d+\.\d+\.\d+\.\d+)', linea)
            if m_ok:
                metodo, ip = m_ok.groups()
                hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                await enviar_alerta("SSH", ip, f"Login exitoso ({metodo})", hora)

            m_fail = re.search(r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)', linea)
            if m_fail:
                ip = m_fail.group(1)
                hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                await enviar_alerta("SSH", ip, "Login fallido", hora)


# Monitoreo Fail2Ban (fail2ban.log)
async def monitorear_fail2ban():
    with open('/var/log/fail2ban.log', 'r') as log:
        log.seek(0, 2)
        while True:
            linea = log.readline()
            if not linea:
                await asyncio.sleep(1)
                continue

            ban = re.search(r'Ban (\d+\.\d+\.\d+\.\d+)', linea)
            if ban:
                ip = ban.group(1)
                hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                await enviar_alerta("Fail2Ban", ip, "🚫 IP baneada", hora)

            unban = re.search(r'Unban (\d+\.\d+\.\d+\.\d+)', linea)
            if unban:
                ip = unban.group(1)
                hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                await enviar_alerta("Fail2Ban", ip, "✅ IP desbaneada", hora)


# Ejecutar los dos monitores en paralelo
async def main():
    await asyncio.gather(
        monitorear_ssh(),
        monitorear_fail2ban()
    )

asyncio.run(main())


