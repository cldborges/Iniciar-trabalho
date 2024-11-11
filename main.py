import os
import datetime
import easygui

'''import webbrowser
chrome_path = 'C:/PortableApps/PortableApps/GoogleChromePortable/App/Chrome-bin/chrome.exe %s'
webbrowser.get(chrome_path).open('http://docs.python.org/')

caminho = os.path.normpath("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
os.startfile(caminho)'''

#os.startfile("C:\Users\z0026jjc\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe")
#caminho = os.path.normpath (r'C:\Users\z0026jjc\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe")')

#teams antigo
# os.system('C:/Users/z0026jjc/AppData/Local/Microsoft/Teams/Update.exe --processStart "Teams.exe"')

# Obtém o horário atual
hora_atual = datetime.datetime.now().hour

# Verifica se a hora está entre 07h e 09h
if 7 <= hora_atual < 9:
    easygui.msgbox('Tomar os remédios!!')

for caminho in r"C:\PortableApps\PortableApps\GoogleChromePortable\GoogleChromePortable.exe", "outlook", "C:\Program Files\WindowsApps\MSTeams_23306.3315.2560.6525_x64__8wekyb3d8bbwe\ms-teams.exe":
#for caminho in r"C:\Users\z0026jjc\OneDrive - Atos\5m.exe", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe":
    os.path.normpath(caminho)
    os.startfile(caminho)
