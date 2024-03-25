import yaml
import click
import csv
import os
import datetime

# TODO
# create config in .config
# save in csv so they can graph it


@click.command()
@click.argument(
    "action",
    type=click.Choice(["start", "stop", "pause", "break", "session"]),
    metavar="ACTION",
    required=True,
)
def flowtime(action):
    """A minimal distraction, maximum utility flowmodoro timer"""

    click.echo(f"given action: {action}!")

    if action == "session":
        create_session_file()
    create_history_file()


def start_timer():
    pass


def create_history_file(filename="history.csv", path=".config"):
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


def create_session_file():
    # TODO import local time
    date = datetime.date.today().strftime("%Y-%m-%d")
    # Format the local time to display only HH:MM
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


if __name__ == "__main__":
    flowtime()
