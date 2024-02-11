import os

def main():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@                              @")
    print("@Welcome in encoder            @")
    print("@Created by: Danb1551          @")
    print("@Instagram: @danik_12sniper    @")
    print("@Web: termux.wz.cz             @")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Select:")
    print("{1.} Encode")
    print("{2.} Dekódování")
    choice = input("Write down the selected number: ")

    if choice == '1':
        os.system('python3 encoder.py')
    elif choice == '2':
        os.system('python3 decoder.py')
    else:
        print("Error")

if __name__ == "__main__":
    main()
