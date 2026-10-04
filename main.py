from tracker import mark_day, get_streak, load_data, get_quote
from quotes import quotes


def show_menu():
    print("\n===== StudyStreak =====")
    print("1. mark today as STUDIED")
    print("2. Mark today as MISSEd")
    print("3. View my streak")
    print("4. View this month")
    print("5. Exit")
    return input("Choose (1-5): ")

def main():
    while True:
        choice = show_menu()
        
        if choice == "1":
            situation = mark_day("studied")
            print("\n Marked as studied!")
            print(f"{get_quote(situation)}")
            
        elif choice == "2":
            situation = mark_day("missed")
            print("\n Marked as missed")
            print(f"{get_quote(situation)}")
            
            
        elif choice == "3":
            data = load_data()
            streak = get_streak(data)
            print(f"\n Current streak: {streak} day(s)")
            
        elif choice == "4":
            data = load_data()
            if not data:
                print("\nNO data yet. Start marking days!")
            else:
                print("\nYour records: ")
                for day, status in sorted(data.items()):
                    emoji = "☑️" if status == "studied" else "❌"
                    print(f"  {day}  {emoji}  {status}")
                    
        elif choice == "5":
            print("\nKeeep going. See you tomorrow!")
            break
        
        else:
            print("\n Pick 1-5 only.")
            
if __name__ == "__main__":
    main()
