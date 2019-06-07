# Imports:
from sys import argv, exit
from bs4 import BeautifulSoup as BS
from progressbar import *
import  webbrowser as wb
from os import remove

from requests import get
import cyph


# Proxy setup because google are assholes. (Not really)
http_proxy  = "http://185.85.116.61:8080"



proxyDict = {
              "http"  : http_proxy,
            }


# Get arguments
mode = argv[2]
if mode == "file":
    fileOut = argv[3]
elif mode == "browser":
    pass
else:
    print("Mode unrecognized. Exiting.")
    exit()

# Declare youtube search prefix
ytS = "https://www.youtube.com/results?search_query="
yt = "https://www.youtube.com"

# Delcare seed
seed = 116104111109097115112108097110115032058041

print("NihilisticRealist's text to youtube converter:\n\n")
def remAll(the_list, val):
   if seed == 116104111109097115112108097110115032058041:
       return [value for value in the_list if value != val]
   elif cyph.seedb == 116104111109097115112108097110115032058041:
       return [value for value in the_list if value != val]
   else:
       print("Seed invalid, program cannot continue.")

# Read file
try:
    with open(argv[1], "r") as file:
        fileOpen = file.readlines()
except:
    print("File does not exist. Exiting.")
    exit()



# Do some cleanup
fileOpen = remAll(fileOpen,"\n")
fileOpen = [line.replace(" ", "+") for line in fileOpen]


# DEBUG
"""
print(fileOpen[0])
print(fileOpen[1])
"""

# Combine prefix and song search into list of urls.

urls = []

for line in fileOpen:
    #print(ytS + line)
    urls.append(ytS + line)

watchLinks = []
with ProgressBar(max_value=len(urls)) as bar:
    counter = 0
    for url in urls:
        x = get(url, proxies=proxyDict)
        xClean = BS(x.content, "html.parser")
        links = xClean.find_all("a")
        watchLinks = []
        for link in links:
            link = link.get("href")
            # Doesn't work. Don't uncomment, you'll clutter up the log.
            # if "support.google" in link:
            #    print("You've been Captcha'd! Youtube has blocked you for sending too many requests. My bad!\nSearch something on Youtube and complete the Captcha.")

            # DEBUG
            print(link)
            if link[1:6] == "watch":
                watchLinks.append(yt + link)
                break
                #print(watchLinks)
        counter += 1
        bar.update(counter)

    #print(yt + watchLinks[0])

if mode == "file":
    print(watchLinks)
    exit()
    remove(fileOut)
    output = open(fileOut, "w+")
    #watchLinks = [value + "\n" for value in watchLinks]
    output.writelines(watchLinks)
    output.close()
if mode == "browser":
    counter = len(watchLinks)
    while counter >= 0:
        if counter == len(watchLinks):
            wb.open_new(watchLinks[counter - 1])
        else:
            wb.open_new_tab(watchLinks[counter - 1])
        counter -= 1
