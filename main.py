import os
import time

def main_menu():
    while True:
        print("\nCognitive Assessment Tools")
        print("1. Stroop Test")
        print("2. Response Modulation Test")
        print("3. Attention Bottleneck Test")
        print("4. Exit")
        
        choice = input("Select a test (1-4): ")

        if choice == "1":
            os.system("python tests/stroop_test.py")
        elif choice == "2":
            os.system("python tests/response_modulation_test.py")
        elif choice == "3":
            os.system("python tests/attention_bottleneck_test.py")
        elif choice == "4":
            print("Exiting...")
            time.sleep(1)
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
