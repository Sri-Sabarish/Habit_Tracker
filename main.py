from datetime import datetime
import db
import streak

def show_menu():
    print("\n=== Habit Tracker ===")
    print("1. Add a new habit")
    print("2. Mark today's habit")
    print("3. View streak for one habit")
    print("4. View all habits and streak")
    print("5. Reset all data")
    print("6. Exit")

def add_new_habit():
    name=input("Enter a new habit :").strip()
    habits=db.get_all_habits()
    for habit_id,habit_name in habits:
        if name==habit_name:
            print("Habit already exists!")
    db.add_habit(name)
    print(f"Habit <{name}>  added!")

def pick_habit():
    habits=db.get_all_habits()
    if not habits:
        print("No habits yet. Add one first!")
    else:
        print("Your habits:")
        for habit_id,name in habits:
            print(f"{habit_id}) {name}")    
        choice=input("\nEnter habit number :").strip()
        for habit_id,name in habits:
            if str(habit_id)==choice:
                return habit_id,name  
        print("Invalid choice!")
        return None

def mark_today():
    picked=pick_habit()    
    if not picked:
        return
    id,name=picked
    status=input("Done or Missed? (Type-d/m) :")
    status="done" if status=="d" else "missed"
    today_str = datetime.today().strftime("%Y-%m-%d")
    db.log_status(id,today_str,status)
    print(f"Marked {name} as {status} for {today_str}")

def view_one_streak():
    picked=pick_habit()
    if not picked:
        return
    id,name=picked
    logs=db.get_logs(id)
    current=streak.calculate_current_streak(logs)
    best=streak.calculate_best_streak(logs)
    consistency=streak.calculate_consistency(logs)

    print(f"Habit : {name}")
    print(f"Current Streak : {current}")
    print(f"Best Streak : {best}")
    print(f"Consistency : {consistency}%")

def view_all_streaks():
    habits=db.get_all_habits()
    if not habits:
        print("No habits yet! Add one first") 
    print("\n===All Habits===\n")    
    for habit_id,name in habits:
        logs=db.get_logs(habit_id)
        current=streak.calculate_current_streak(logs)
        best=streak.calculate_best_streak(logs)
        consistency=streak.calculate_consistency(logs)
        print(f"Habit: {name} | Current Streak: {current} | Best Streak: {best} | Consistency: {consistency}%")
def reset_data():
    print("Note:This will delete all habits and logs")  
    confirm=input("Type 'yes' to reset data :").strip().lower()
    if confirm=="yes":
        db.reset_all_data()
        print("All data has been reset.")
    else:
        print("Reset cancelled.") 
def main():
    db.create_tables()
    while True:
        show_menu()
        choice=input("Choose an option :").strip()
        if choice=="1":
            add_new_habit()
        elif choice=="2":
            mark_today()
        elif choice=="3":
            view_one_streak()
        elif choice=="4":
            view_all_streaks()
        elif choice=="5":
            reset_data()
        elif choice=="6":
            print("Goodbye! keep growing.") 
            break
        else:
            print("Invalid option, try again.")
if __name__ == "__main__":
    main()





