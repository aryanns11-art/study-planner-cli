import json

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

        if s["type"].lower() == "college":
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

    top = max(totals, key=totals.get)

    print(f"\nMost Studied: {top} ({totals[top]} minutes)")

#------------------------------------------------------------------------------------------------------------------------

def show_summary():

    if not sessions:
        print("No study data available!")
        return

    total, college, skills = calculate_time()

    print(f"\nTotal Study Time: {total} minutes")

    print("\n-----College Subjects-----:")
    for sub, t in college.items():
        print(f"{sub}: {t}")

    print("\n-----External Skills------:")
    for sub, t in skills.items():
        print(f"{sub}: {t}")

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
        "time": time
    }

    sessions.append(session)
    save_data()

    print("Session added!")

#------------------------------------------------------------------------------------------------------------------------

def delete_session():
    if not sessions:
        print("No sessions to delete!")
        return
    
    print("\nDelete Study Session")
    for idx, s in enumerate(sessions, 1):
        print(f"{idx}. {s['type']} - {s['subject']} ({s['time']} mins)")
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
        print("5. Exit")

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
            break
        else:
            print("Invalid choice!")

menu()