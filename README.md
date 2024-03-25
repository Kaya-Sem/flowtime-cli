# flowtime-cli

python cli tool to efficiently implement flowmodoro

#### options

`session` start a new session and start the timer

`start`

`stop`

`pause`

`break`

#### How it works

flowtime-cli is IO based, which means all data is processed from and to files. Because of this, it does not block your terminal and it works between reboots. If you start a timer, restart your computer, and stop the timer, it will have kept track of the passed time, and your break will still be calculated correctly.

The script creates a history file, and keeps records of all past sessions in there. This can be used in other apps to be graphed and view statistics.
