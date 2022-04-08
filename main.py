import os

'''import webbrowser
chrome_path = 'C:/PortableApps/PortableApps/GoogleChromePortable/App/Chrome-bin/chrome.exe %s'
webbrowser.get(chrome_path).open('http://docs.python.org/')

caminho = os.path.normpath("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
print(caminho)
os.startfile(caminho)'''

#os.startfile("C:\Users\z0026jjc\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe")
#caminho = os.path.normpath (r'C:\Users\z0026jjc\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe")')
#print(caminho)



os.startfile("outlook")
os.system('C:/Users/z0026jjc/AppData/Local/Microsoft/Teams/Update.exe --processStart "Teams.exe"')
for caminho in r"C:\PortableApps\PortableApps\GoogleChromePortable\GoogleChromePortable.exe":
#for caminho in r"C:\Users\z0026jjc\OneDrive - Atos\5m.exe", r"C:\PortableApps\PortableApps\GoogleChromePortable\GoogleChromePortable.exe":
#for caminho in r"C:\Users\z0026jjc\OneDrive - Atos\5m.exe", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe":
    os.path.normpath(caminho)
    os.startfile(caminho)
