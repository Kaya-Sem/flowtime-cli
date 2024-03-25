import csv
import datetime
import os

import click
import yaml


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


# change path back to .config
def create_history_file(filename="flowtime_history.csv", path=""):
    # Get the home directory
    home_dir = os.path.expanduser("~")

    # Construct the full path to the file
    file_path = os.path.join(home_dir, path, filename)

    # Define the header
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


def get_session_file():
    # If a session file exists, open it, else, create a new session
    if check_session_file_existance():
        pass
    else:
        # YYYY-MM-DD
        # HH:MM
        date = datetime.date.today().strftime("%Y-%m-%d")
        start_time = datetime.datetime.now().strftime("%H:%M")

        session_data = {
            "date: date": date,
            "start_time": start_time,
            "end_time": None,
            "focused_time": None,
            "break_time": None,
            "#focus_blocks": None,
            "#breaks": None,
        }

        with open("session.yaml", "w") as file:
            yaml.dump(session_data, file)


def start_timer():
    pass


# functions to be called from given argument
actions = {
    "start": start_timer(),
    "stop": hi(),
    "pause": hi(),
    "break": hi(),
    "session": hi(),
}


@click.command()
@click.argument(
    "action",
    type=click.Choice(
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

    click.echo(f"given action: {action}!")

    # call functionality based on given argument
    actions[action]


if __name__ == "__main__":
    flowtime()
