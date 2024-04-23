import os
import time
import ctypes
from colorama import init, Fore, Style

print('Initializing name...')
ctypes.windll.kernel32.SetConsoleTitleA(b"wingetkey")

print('Initializing color codes...')
init()
time.sleep(0.1)

hello_text = f'''
{Fore.RED}██╗       ██╗██╗███╗  ██╗{Fore.GREEN} ██████╗ ███████╗████████╗{Fore.BLUE}██╗  ██╗███████╗██╗   ██╗{Style.RESET_ALL}TM
{Fore.RED}██║  ██╗  ██║██║████╗ ██║{Fore.GREEN}██╔════╝ ██╔════╝╚══██╔══╝{Fore.BLUE}██║ ██╔╝██╔════╝╚██╗ ██╔╝{Style.RESET_ALL}
{Fore.RED}╚██╗████╗██╔╝██║██╔██╗██║{Fore.GREEN}██║  ██╗ █████╗     ██║   {Fore.BLUE}█████═╝ █████╗   ╚████╔╝ {Style.RESET_ALL}
{Fore.RED} ████╔═████║ ██║██║╚████║{Fore.GREEN}██║  ╚██╗██╔══╝     ██║   {Fore.BLUE}██╔═██╗ ██╔══╝    ╚██╔╝  {Style.RESET_ALL}
{Fore.RED} ╚██╔╝ ╚██╔╝ ██║██║ ╚███║{Fore.GREEN}╚██████╔╝███████╗   ██║   {Fore.BLUE}██║ ╚██╗███████╗   ██║   {Style.RESET_ALL}
{Fore.RED}  ╚═╝   ╚═╝  ╚═╝╚═╝  ╚══╝{Fore.GREEN} ╚═════╝ ╚══════╝   ╚═╝   {Fore.BLUE}╚═╝  ╚═╝╚══════╝   ╚═╝   {Style.RESET_ALL}
'''

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

print(Fore.YELLOW + 'Admin Verification...' + Style.RESET_ALL)
time.sleep(0.1)

if not is_admin():
    print(Fore.RED + '-e1002 Verification failed!' + Style.RESET_ALL)
    print(Fore.YELLOW + '-tip: Try running the program using the administrator name' + Style.RESET_ALL)
    time.sleep(0.2)
    os.system('pause')
    exit()

print(Fore.GREEN + 'Done!' + Style.RESET_ALL)
print('wait...')
time.sleep(0.5)

print('\033[H\033[J')
print(hello_text)

while True:
    ver = input('Введите версию продукта (10 | 11) $ ')
    if ver in ['10', '11']:
        break
    print(f'{Fore.RED}-e1001 Выбрана неверная версия продукта!{Style.RESET_ALL}')

key = input('Введите ключ активации (если нет, нажмите ENTER) $ ')

print(f'Запись ключа {Fore.CYAN}https://www.microsoft.com/{Style.RESET_ALL}')
print(f'{Fore.YELLOW}(slmgr /ipk {Fore.MAGENTA}WINDO-WSKEY-TOACT-IVATE{Fore.YELLOW}){Style.RESET_ALL}')
os.system(f'slmgr /ipk {"W269N-WFGWX-YVC9B-4J6C9-T83GX" if not key else key}')
print(f'Задано имя {Fore.CYAN}компьютера{Style.RESET_ALL} со службой управления {Fore.GREEN}ключами{Style.RESET_ALL}')
print(f'{Fore.YELLOW}(slmgr /skms kms.digiboy.ir){Style.RESET_ALL}')
os.system('slmgr /skms kms.digiboy.ir')
print(f'{Fore.GREEN}Активация Windows {ver}.{Style.RESET_ALL}')
os.system('slmgr /ato')

if input('Проверить активацию Windows? (да | нет - ENTER) $ ') == 'да':
    print(f'{Fore.GREEN}\n«Постоянная активация прошла успешно»{Style.RESET_ALL} - Продукт активирован')
    print(f'{Fore.RED}«Windows находится в режиме уведомления»{Style.RESET_ALL} - Продукт не активирован\n')
    os.system('slmgr /xpr')

print(f'Если активация прошла {Fore.RED}безуспешно{Style.RESET_ALL}, попробуйте ввести другой {Fore.GREEN}ключ активации.{Style.RESET_ALL}')
print(f'Спасибо за пользование программой активации wingetkey!')
os.system('pause')