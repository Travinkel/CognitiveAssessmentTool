import os
import json
import sys

from stroop_tests.color_word_stroop import run_color_word_stroop
#from stroop_tests.picture_word_stroop import run_picture_word_stroop
#from stroop_tests.separated_cw_stroop import run_separated_cw_stroop

RESULTS_DIR = "results"

def main_menu():
    while True:
        print("\n=== Cognitive Assessment Tools ===")
        print("1. Run Standard Color-Word (CW) Stroop")
        print("2. Run Picture-Word (PW) Stroop")
        print("3. Run Spatially Separated CW Stroop")
        print("4. View Past Results")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ")

        if choice == "1":
            run_color_word_stroop()
            input("\nPress Enter to return to the main menu...")
        elif choice == "2":
            run_picture_word_stroop()
            input("\nPress Enter to return to the main menu...")
        elif choice == "3":
            run_separated_cw_stroop()
            input("\nPress Enter to return to the main menu...")
        elif choice == "4":
            view_results()
        elif choice == "5":
            print("Exiting program...")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")

def view_results():
    if not os.path.exists(RESULTS_DIR):
        print("\nNo results found.")
        return

    print("\n=== Test Results ===")
    files = os.listdir(RESULTS_DIR)
    if not files:
        print("No recorded test results found.")
        return

    for idx, filename in enumerate(files):
        print(f"{idx + 1}. {filename}")

    try:
        selection = int(input("\nSelect a result file to view (or 0 to return): "))
        if selection == 0:
            return

        file_path = os.path.join(RESULTS_DIR, files[selection - 1])
        with open(file_path, "r") as file:
            results = json.load(file)
            print(json.dumps(results, indent=4))

        input("\nPress Enter to return to the main menu...")

    except (ValueError, IndexError):
        print("Invalid selection.")

if __name__ == "__main__":
    main_menu()
