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

for s in sessions:
    print(f"{s['type']} | {s['subject']} | {s['time']} minutes")


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