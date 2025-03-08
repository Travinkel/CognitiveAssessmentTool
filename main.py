import os
import json
from tests import stroop_test, response_mod, go_no_go  # Import test modules
from utils import results_viewer

def main():
    while True:
        print("\n==== Psychopathy Cognitive Assessment Tools ====")
        print("1. Stroop Test")
        print("2. Response Modulation Test")
        print("3. Go/No-Go Task")
        print("4. View Results")
        print("5. Exit")
        
        choice = input("Select a test: ")
        
        if choice == "1":
            stroop_test.run()
        elif choice == "2":
            response_mod.run()
        elif choice == "3":
            go_no_go.run()
        elif choice == "4":
            results_viewer.show_results()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
