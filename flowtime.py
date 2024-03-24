import click
import csv
import os

# TODO
# create config in .config
# save in csv so they can graph it


@click.command()
@click.argument(
    "action",
    type=click.Choice(["start", "stop"]),
    metavar="ACTION",
    required=True,
)
def flowmodoro(action):
    """A minimal distraction, maximum utility flowmodoro timer

    actions: start, stop"""
    click.echo(f"given action: {action}!")
    create_history_file()


def start_timer():
    pass


def create_history_file(filename="flowmodoro_history.csv", path=""):
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


if __name__ == "__main__":
    flowmodoro()
