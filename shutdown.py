import os
check = input("Want to shutdown your computer ? (y/n): ")
if check == 'n':
    exit()
else:
    os.system("shutdown /s /t 1")       #   /r instead of /s will restart the system