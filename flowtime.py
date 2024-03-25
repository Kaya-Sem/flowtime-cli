import csv
import datetime
import os
import sys

import click
import yaml

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".config")
SESSION_FILE_PATH = os.path.join(CONFIG_DIR, "session.yaml")

NEG_RESPONSES = ["no", "n", "N", "nah", "Nah", "Naw", "na"]
POS_RESPONSES = ["Y", "y", "Yes", "yes", "sure", "yeah", "Yeah"]


def delete_session_file():
    if os.path.exists(SESSION_FILE_PATH):
        os.remove(SESSION_FILE_PATH)
        sys.stderr.write("Session file deleted succesfully\n")
    else:
        sys.stderr.write("Session file does not exist\n")


def check_session_file_existance():
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(home_dir, ".config")
    session_file_path = os.path.join(config_dir, "session.yaml")

    if os.path.exists(session_file_path):
        return open(session_file_path, "w")

    # is no session file is found
    return None


def hi():
    pass


def create_history_file(filename="flowtime_history.csv", path=".config"):
    # Construct the full path to the file
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, path, filename)

    # Define CSV header
    fieldnames = [
        "date",
        "start_time",
        "end_time",
        "focused_time",
        "break_time",
        "#focusblocks",
        "#breaks",
    ]

    # Write an empty CSV file with header
    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


def create_session_file():
    # YYYY-MM-DD
    # HH:MM
    date = datetime.date.today().strftime("%Y-%m-%d")
    start_time = datetime.datetime.now().strftime("%H:%M")

    session_data = {
        # session data
        "date: date": date,
        "session_start_time": start_time,
        "session_end_time": None,
        "total_focused_time": None,
        "total_break_time": None,
        "count_focus_blocks": None,
        "count_breaks": None,
        # current timer
        "current_timer_start": None,
        "current_break_start": None,
    }

    os.makedirs(CONFIG_DIR, exist_ok=True)

    with open(SESSION_FILE_PATH, "w") as file:
        yaml.dump(session_data, file)


def start_timer():
    pass


def session():
    if check_session_file_existance():
        response = str(input("Found ongoing session. Start new a one? (Y/n): "))

        if response in POS_RESPONSES:
            delete_session_file()

        elif response in NEG_RESPONSES:
            pass

    else:
        create_session_file()


# functions to be called from given argument
actions = {
    "start": start_timer(),
    "stop": hi(),
    "pause": hi(),
    "break": hi(),
    "session": session(),
}


@click.command()
@click.argument(
    "action",
    type=click.Choice(  # all possible arguments
        [
            "start",
            "stop",
            "pause",
            "break",
            "session",
        ]
    ),
    metavar="ACTION",
    required=True,
)
def flowtime(action):
    """A minimal distraction, maximum utility flowmodoro timer"""

    # call functionality based on given argument
    actions[action]


if __name__ == "__main__":
    flowtime()
