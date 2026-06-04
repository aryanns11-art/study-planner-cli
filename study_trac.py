sessions = []
    
session1 = {
    "type": "college",
    "subject": "Maths",
    "time": 60
}

session2 = {
    "type": "skill",
    "subject": "Python",
    "time": 60
}

sessions.append(session1)
sessions.append(session2)


def calculate_time():
    total_time = 0
    college_time = {}
    skill_time = {}

    for s in sessions:
        total_time += s["time"]

        if s["type"] == "college":
            college_time[s["subject"]] = college_time.get(s["subject"], 0) + s["time"]
        else:
            skill_time[s["subject"]] = skill_time.get(s["subject"], 0) + s["time"]

    return total_time, college_time, skill_time

def show_summary():
    total, college, skills = calculate_time()

    print("\n-----Total Study Time-----:\n", total)

    print("\n-----College Subjects-----:")
    for sub, t in college.items():
        print(f"{sub}: {t}")

    print("\n-----External Skills------:")
    for sub, t in skills.items():
        print(f"{sub}: {t}")

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

    print("Session added!")

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
        else:
            print("Invalid session number!")
    except ValueError:
        print("Invalid input!")        

def menu():
    while True:
        print("\n==== Smart Study Tracker ====")
        print("1. Add Session")
        print("2. Show Summary")
        print("3. Delete Session")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_session()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            delete_session()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

menu()