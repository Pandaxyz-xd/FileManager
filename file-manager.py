import random, time, datetime, pyfiglet, os, colorama, requests
from datetime import datetime
red = colorama.Fore.RED
reset = colorama.Fore.RESET
green = colorama.Fore.GREEN
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
def banner():

    print(f"""
{red}
$$$$$$$$\ $$\ $$\                 $$\      $$\                                                             
$$  _____|\__|$$ |                $$$\    $$$ |                                                            
$$ |      $$\ $$ | $$$$$$\        $$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
$$$$$\    $$ |$$ |$$  __$$\       $$\$$\$$ $$ | \____$$\ $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  __|   $$ |$$ |$$$$$$$$ |      $$ \$$$  $$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$ |$$ |$$   ____|      $$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |      
$$ |      $$ |$$ |\$$$$$$$\       $$ | \_/ $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      
\__|      \__|\__| \_______|      \__|     \__| \_______|\__|  \__| \_______| \____$$ | \_______|\__|      
                                                                             $$\   $$ |                    
                                                                             \$$$$$$  |                    
                                                                              \______/                     
{green}New login: {reset}{current_time}
{green}Author: {reset}@Pandaxyz
""")


os.system("cls")
banner()
print("Hey! This is the menu")
select = None
while select != 0:
    select = int(input(f"[{red}1{reset}] Download image/s \n[{red}2{reset}] Delete file/s\n[{red}3{reset}] Download file/s\n[>>] "))

    if select == 1:
        os.system("cls")
        banner()
        image = input("Write the IMAGE url ends with png/jpg/jpeg etc...\n[>>] ")
        os.system("cls")
        banner()
        print("Image: ",image)
        name = input("Write the IMAGE name ex: myimage + .png/jpg etc...\n[>>] ")
        response = requests.get(image)
        open(name, "wb").write(response.content)
        print("Downloading file")
        time.sleep(1)
        os.system("cls")
        banner()
        print("File downloaded!")
    elif select == 2:
        os.system("cls")
        banner()
        route = input("Enter the file path\n[>>] ")
        os.remove(route)
        print("Removing file")
        time.sleep(1)
        os.system("cls")
        banner()
        print("File removed!")
    elif select == 3:
        os.system("cls")
        banner()
        files = input("Write the url DOCUMENT\n[>>] ")
        os.system("cls")
        banner()
        print("File: ",files)
        filename = input("Write the name DOCUMENT ex: mydocument + .txt/.json etc...\n[>>] ")
        response2 = requests.get(files)
        open(filename, "wb").write(response2.content)
        print("Downloading file")
        time.sleep(1)
        os.system("cls")
        banner()
        print("File downloaded!")
