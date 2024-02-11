import os

def main():
    print("Vítejte v aplikaci pro kódování a dekódování.")
    print("Zvolte možnost:")
    print("1. Kódování")
    print("2. Dekódování")
    choice = input("Zadejte číslo možnosti: ")

    if choice == '1':
        os.system('python3 encoder.py')
    elif choice == '2':
        os.system('python3 decoder.py')
    else:
        print("Neplatná volba.")

if __name__ == "__main__":
    main()
