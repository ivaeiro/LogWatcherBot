# LogWatcherBot
Este proyecto es un bot de Telegram que monitorea eventos de seguridad en un servidor, como inicios de sesión SSH y cambios en el estado de IPs en Fail2Ban. Envía alertas en tiempo real sobre logins exitosos, fallidos y bloqueos/desbloqueos de IPs.

## Requisitos

- Python 3.7 o superior
- Paquetes de Python: asyncio, re, datetime, telegram
- Acceso a los archivos de log del sistema (/var/log/auth.log y /var/log/fail2ban.log)
- Token de un bot de Telegram
- ID de chat de Telegram

## Instalación

1. Clonar el repositorio:

```bash
  git clone https://github.com/ivaeiro/SecurityAlertBot.git
  cd my-project
```

2. Instalar dependencias:

```bash
pip install python-telegram-bot
```

3. Configurar el bot de Telegram:

- Crea un bot de Telegram a través de BotFather.
- Guarda el token de tu bot.

4. Obtener el ID de chat de Telegram:

- Inicia una conversación con tu bot de Telegram.

- Usa el siguiente comando en tu navegador para obtener tu ID de chat (reemplaza <bot_token> por el token de tu bot):

```bash
https://api.telegram.org/bot<bot_token>/getUpdates
```
- En el JSON de respuesta, busca el campo chat y anota el valor de id.

5. Configurar el script:

```bash
BOT_TOKEN = 'tu-bot-token'
CHAT_ID = 'tu-id-de-chat'
```

6. Permisos de acceso a los logs del sistema:

Asegúrate de que el script tiene acceso a los archivos de log /var/log/auth.log y /var/log/fail2ban.log. Si es necesario, ejecuta el script con privilegios elevados.

## Ejecución

Para ejecutar el bot, solo necesitas correr el script:

```python
python security_alert_bot.py

```

El bot comenzará a monitorear los logs y enviará alertas en tiempo real a tu chat de Telegram.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, por favor sigue estos pasos:

1. Fork este repositorio.

2. Crea una nueva rama (git checkout -b feature-nueva).

3. Haz tus cambios y confirma (git commit -am 'Añadir nueva función').

4. Sube tus cambios (git push origin feature-nueva).

5. Crea un Pull Request.

## Licencia

Este proyecto está bajo la licencia [MIT](https://choosealicense.com/licenses/mit/)
