# study_protocol.py — yes, code it: a tiny program storing {concept: last_reviewed_date} in a 
# JSON file that prints which concepts are due today per the spacing schedule (1d, 3d, 7d, 14d). 
# It will serve you for the rest of the curriculum — real tool, real learning.

# topics - date learned them
# missed sessions - based on date
# completed sessions
# future sessions
# sessions for today

from datetime import date
from datetime import timedelta

import json

from tabulate import tabulate

import copy

DEFAULT_VALUE = {
    "topics": {

    },
    "completed_sessions": {

    }
}

path = "protocol.json"

# tomorrow

# Default value structure for the json file.
def write_default_value(path="protocol.json"):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_VALUE, f, indent=2)
    except PermissionError:
        print("You do not have permission to write in this file.")
    except json.JSONDecodeError:
        print("File corrupted.")

# Reads the file and stores its content.
def load_json(path="protocol.json"):
    """Returns the data inside the file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = json.load(f)
    except FileNotFoundError:
        print("File does not exist.")
        print("Creating file with default values...")
        write_default_value()   
        return DEFAULT_VALUE
    except PermissionError:
        print("Permission denied.")
        write_default_value()
        return DEFAULT_VALUE
    except json.JSONDecodeError:
        print("Json file is corrupted.")
        print("Creating file with default values...")
        write_default_value()
        return DEFAULT_VALUE
    else:
        return content

def add_topic(topic: str, date_reviewed: date, path="protocol.json"):
    data = {
        "review_date": date_reviewed.isoformat(),
        "day 1": (date_reviewed + timedelta(days=1)).isoformat(),
        "day 3": (date_reviewed + timedelta(days=3)).isoformat(),
        "day 7": (date_reviewed + timedelta(days=7)).isoformat(),
        "day 14": (date_reviewed + timedelta(days=14)).isoformat(),
        "day 30": (date_reviewed + timedelta(days=30)).isoformat()
    }

    content = load_json(path)

    content["topics"][topic] = data

    save_data(content)

def save_data(data, path: str = "protocol.json"):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except FileNotFoundError:
        print("File does not exist.")
    except PermissionError:
        print("You do not have permission to write in this file.")
    except json.JSONDecodeError:
        print("File is corrupted.")

def today_session(today):
    content = load_json()

    today_lesson = []

    for topic, session in content["topics"].items():
        for s, dates in session.items():
            if dates == today.isoformat() and s != "review_date":
                today_lesson.append([topic, dates, s])

    return today_lesson

def missed_sessions(today):
    content = load_json()
    
    missed = []
    
    for topic, session in content["topics"].items():
        for s, dates in session.items():
            if date.fromisoformat(dates) < today and s != "review_date":
                missed.append([topic, dates, s])

    return missed

def view_completed():
    completed = get_completed()

    compl = []

    for topic, session in completed.items():
        for s, dates in session.items():
            compl.append([topic, dates, s])

    return compl

def complete(index_complete):
    choices = today_session(date.today())

    session = choices[index_complete]

    content = load_json()

    content_copy = copy.deepcopy(content)

    completed = get_completed()

    for topics, values in content["topics"].items():
        for s, dates in values.items():
            if session[0] == topics and session[1] == dates and session[2] == s:
                if topics not in completed:
                    completed[topics] = {}
                    completed[topics][s] = dates
                del content_copy["topics"][topics][s]

    content = content_copy

    content["completed_sessions"] = completed

    save_data(content)

def get_completed(path="protocol.json"):
    try:
        with open(path, "r") as f:
            content = json.load(f)
    except FileNotFoundError:
        print("File doesn't exist.")
    except PermissionError:
        print("Permission denied")
    except json.JSONDecodeError:
        print("File corrupted.")
    else:
        return content["completed_sessions"]

def main():
    today = date.today()
    print("Welcome to Study Protocol!")
    while True:
        print("\n1. Insert new topic" \
            "\n2. View topics to recall today" \
            "\n3. View missed recalls" \
            "\n4. View completed recalls" \
            "\n5. Mark as complete a topic" \
            "\n6. Exit")

        try:
            choice = int(input("\nEnter choice: "))
        except ValueError:
            print("Please enter a valid choice.")
        else:
            if choice == 1:
                topic = input("Enter topic: ")
                add_topic(topic, today)
            elif choice == 2:
                headers = ["Concept", "Date", "Session No."]
                to_recall = today_session(today)
                print(tabulate(to_recall, headers=headers, tablefmt="grid"))
            elif choice == 3:
                headers = ["Concept", "Date", "Session No."]
                missed = missed_sessions(today)
                print(tabulate(missed, headers=headers, tablefmt="grid"))
            elif choice == 4:
                headers = ["No.", "Concept", "Date", "Session No."]
                compl = view_completed()
                print(tabulate(compl, headers=headers, tablefmt="grid", showindex=range(1, len(compl) + 1)))
            elif choice == 5:
                headers = ["No.", "Concept", "Date", "Session No."]
                to_recall = today_session(today)
                print(tabulate(to_recall, headers=headers, tablefmt="grid", showindex=range(1, len(to_recall) + 1)))
                try:
                    index_complete = int(input("Enter the number you want to mark as complete: ")) - 1 
                    if index_complete > len(to_recall) - 1 or index_complete < 0:
                        raise ValueError
                except ValueError:
                    print("Please enter a valid integer.")
                else:
                    complete(index_complete)
            elif choice == 6:
                break
            else:
                print("Please choose number from 1-6.")

if __name__ == "__main__":
    main()