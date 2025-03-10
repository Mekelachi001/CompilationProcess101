import os
import time
import subprocess

def main():
    os.system('cls')
    os.system('color A')
    print("Enter Location of file Path ? ")
    print("[1] Current Location\n[2] Another Location")
    global path
    select = input("::> ")
    match(select):
        case '1':
            os.system('cls')
            path = os.getcwd()
        case '2':
            os.system('cls')
            path = input("Enter the Path to The file ? ")
        case _:
            raise IndexError ("Out Of Range or Invalis Input !!")
            exit()

    time.sleep(1)
    print("[*] Using Path : ",path)
    print("[*] Locating Folder Path ....")
    time.sleep(2)
    print("[*] Adding Path to file ..")
    os.system("PATH > file.txt")

    file = open("file.txt",'a')
    file.write(";")
    file.write(path)
    file.close()

    time.sleep(2)
    print("[*] File Modified")

    for x in range(20):
        print("[*] Completing ","#"*x)
        time.sleep(0.5)
        os.system('cls')
    time.sleep(2)
    os.system("cls")

    print("[*] Process Completed .. ")
    file = open("file.txt", 'r')
    text = file.read()
    file.close()
    print("[*] Pls Restart Your PC")

    os.system(f'PATH={text}')
    command = subprocess.run([f"PATH={text}"],capture_output=True,shell= True).stdout
    command1 = subprocess.run([f"PATH={text}; "],capture_output=True,shell= True).stdout
    # print(text)
    print(command1)
    time.sleep(10)
    os.system('color 7')
    os.system("cls")
    os.system("exit")



if __name__ == '__main__':
    main()