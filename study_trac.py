import json
from datetime import datetime

sessions =[]

def save_data():
    with open("sessions.json", "w") as file:
        json.dump(sessions, file, indent=4)

#------------------------------------------------------------------------------------------------------------------------

def load_data():
    global sessions
    try:
        with open("sessions.json", "r") as file:
            sessions = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        sessions = []
#------------------------------------------------------------------------------------------------------------------------
      
def calculate_time():
    total_time = 0
    college_time = {}
    skill_time = {}

    for s in sessions:
        total_time += s["time"]

        if s.get("type", "").lower() == "college":
            college_time[s["subject"]] = college_time.get(s["subject"], 0) + s["time"]
        else:
            skill_time[s["subject"]] = skill_time.get(s["subject"], 0) + s["time"]

    return total_time, college_time, skill_time

#------------------------------------------------------------------------------------------------------------------------

def most_studied():
    if not sessions:
        print("No data available!")
        return

    totals = {}

    for s in sessions:
        totals[s["subject"]] = totals.get(s["subject"], 0) + s["time"]

    top = max(totals, key=totals.get)  # Find the subject with the highest total study time

    print(f"\nMost Studied: {top} ({totals[top]} minutes)")

#------------------------------------------------------------------------------------------------------------------------
def show_summary():

    if not sessions:
        print("\nNo study data available!")
        return

    total, college, skills = calculate_time()

    total_hours = total // 60
    total_minutes = total % 60

    print("\n" + "=" * 40)
    print("STUDY SUMMARY".center(40))
    print("=" * 40)

    print(f"\nTotal Study Time: {total_hours}h {total_minutes}m")
    print(f"Total Sessions: {len(sessions)}")

    print("\nCollege Subjects:")
    if college:
        for sub, t in college.items():
            h = t // 60
            m = t % 60
            print(f"  - {sub:<15} : {h}h {m}m")
    else:
        print("  No data")

    print("\nExternal Skills:")
    if skills:
        for sub, t in skills.items():
            h = t // 60
            m = t % 60
            print(f"  - {sub:<15} : {h}h {m}m")
    else:
        print("  No data")

    print("\n" + "-" * 60)
    print("All Sessions".center(60))
    print("-" * 60)

    print(f"{'No.':<5}{'Subject':<15}{'Time':<12}{'Type':<10}{'Date'}")

    sorted_sessions = sorted(sessions, key=lambda x: x.get("date", ""))

    for idx, s in enumerate(sorted_sessions, 1):

        hours = s["time"] // 60
        minutes = s["time"] % 60

        if hours:
            time_str = f"{hours}h {minutes}m"
        else:
            time_str = f"{minutes}m"

        print(
            f"{idx:<5}"
            f"{s['subject']:<15}"
            f"{time_str:<12}"
            f"{s['type']:<10}"
            f"{s.get('date', 'N/A')}"
        )

    print("=" * 60)
#------------------------------------------------------------------------------------------------------------------------

def add_session():

    print("\nAdd Study Session")
    print("1. College")
    print("2. External Skill")

    choice = input("Choose type (1/2): ")

    if choice == "1":
        session_type = "college"
    elif choice == "2":
        session_type = "skill"
    else:
        print("Invalid choice!")
        return

    subject = input("Enter Subject Name: ").strip().title()

    try:
        time = int(input("Enter Time (minutes): "))
    except ValueError:
        print("Invalid Input!")
        return  

    if time <= 0:
        print("Time must be positive!")
        return

    session = {
        "type": session_type,
        "subject": subject,
        "time": time,
        "date":datetime.now().strftime("%Y-%m-%d")
        }

    sessions.append(session)
    save_data()

    print("Session added!")

#------------------------------------------------------------------------------------------------------------------------

def edit_session():
    if not sessions:
        print("No sessions to edit!")
        return

    print("\nEdit Study Session")
    for idx, s in enumerate(sessions, 1):
        print(f"{idx}. {s['type']} - {s['subject']} ({s['time']} mins) [{s.get('date','N/A')}]")

    try:
        choice = int(input("Enter session number to edit: "))

        if 1 <= choice <= len(sessions):
            session = sessions[choice - 1]

            print("\nLeave blank to keep current value")

            new_subject = input(f"Subject ({session['subject']}): ").strip()
            new_time = input(f"Time ({session['time']}): ").strip()
            new_type = input(f"Type ({session['type']}): ").strip()

            if new_subject:
                session["subject"] = new_subject.title()

            if new_time:
                try:
                    new_int_time = int(new_time)

                    if new_int_time <= 0:
                         print("Time must be positive!")
                         return
                    session["time"] = new_int_time
                    
                except ValueError:
                    print("Invalid time! Keeping old value.")

            if new_type:
                if new_type.lower() in ["college", "skill"]:
                    session["type"] = new_type.lower()
                else:
                    print("Invalid type!")
                    return

            save_data()

            print("Session updated!")

        else:
            print("Invalid session number!")

    except ValueError:
        print("Invalid input!")

#------------------------------------------------------------------------------------------------------------------------

def delete_session():
    if not sessions:
        print("No sessions to delete!")
        return
    
    print("\nDelete Study Session")
    for idx, s in enumerate(sessions, 1):
        print(f"{idx}. {s['type']} - {s['subject']} ({s['time']} mins) [{s.get('date','N/A')}]")
    try:
        choice = int(input("Enter session number to delete: "))

        if choice > 0 and choice <= len(sessions):
            removed = sessions.pop(choice - 1)
            print(f"Removed: {removed['type']} - {removed['subject']} ({removed['time']} mins)")
            save_data()
        else:
            print("Invalid session number!")
    except ValueError:
        print("Invalid input!")        

#------------------------------------------------------------------------------------------------------------------------
load_data()

def menu():
    while True:
        print("\n==== Smart Study Tracker ====")
        print("1. Add Session")
        print("2. Show Summary")
        print("3. Delete Session")
        print("4. Most Studied")
        print("5. Edit Session")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_session()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            delete_session()
        elif choice == "4":
            most_studied()
        elif choice == "5":
            edit_session()
        elif choice == "6":
            break    
        else:
            print("Invalid choice!")

menu()