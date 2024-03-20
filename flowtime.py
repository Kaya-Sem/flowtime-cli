import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Manage flowtime timer")
    actions = parser.add_mutually_exclusive_group(required=True)

    actions.add_argument("start", help="start a new flowtime timer")
    actions.add_argument("stop", help="stop the flowtime timer")
    actions.add_argument("break", help="take a break")

    parser.add_argument(
        "-v",
        "--verbose",
        help="log info to the terminal",
        action="store_true",
    )
    args = parser.parse_args()

    if args.verbose:
        print(args)
        print("verbosity turned on")

    if args.start:
        print(" start called")
    elif args.stop:
        print("stop called")
