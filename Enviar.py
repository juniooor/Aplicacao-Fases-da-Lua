import webbrowser
import time

url1 = 'wa.me//+55'
num='81996316701' 

chrome = webbrowser.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
chrome.open_new(url1)
time.sleep(1)
chrome.open_new_tab(url1+num)