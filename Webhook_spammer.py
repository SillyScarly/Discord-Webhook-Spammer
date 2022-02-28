import pyautogui
from dhooka import Webhook

Webhook1 =pyautogui.prompt(text=Enter Webhook Url', title='Discord Webhook Spammer')
                           
hook = Webhook(Webhook1)           
                           
MessageToSpam = pyautogui.prompt(text='Message To Spam', title='Discord Webhook Spammer')
while True:
                           hook.send(f"@everyone {MessageToSpam}")
                           
