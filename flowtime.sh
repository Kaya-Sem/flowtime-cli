#!/bin/bash


if [[ "$1" == "" ]]; then
  echo "Syntax error: flowtime.sh [OPTION]" >&2
  exit 1
fi

FLOWTIME_FILE="$HOME/.flowtime"

# Display elapsed time since using flowtime start
displayElapsedTime()
{
  if [[ -f "$FLOWTIME_FILE" ]]; then
    start_time=$(cat "$FLOWTIME_FILE")
    current_time=$(date +%s)
    elapsed_time=$((current_time - start_time))

    echo "Elapsed time since start: $elapsed_time seconds"
  else
    echo "Error: Flowtime not started. Use 'flowtime start' first" 
  fi
}

# Stops the flowtime counter by simply removing tracker file.
stop_flowtime ()
{
  rm -f "$FLOWTIME_FILE"
  echo "Flowtime stopped. Recorded start time removed."
}

calculate_break_time() 
{
   if [[ -f "$FLOWTIME_FILE" ]]; then

     start_time=$(cat "$FLOWTIME_FILE")
     current_time=$(date +%s)
     elapsed_time=$((current_time - start_time))

     break_time=$((elapsed_time / 4))

     # Calculate break time in hours and minutes
     hours=$((break_time / 3600))
     minutes=$(((break_time % 3600) / 60)) 


    
     echo "Flowtime break: ${hours}h ${minutes}min"

     rm -f "$FLOWTIME_FILE"

     else
     echo "Error: Flowtime not started. Use 'flowtime start' first."
   fi
 
}

start_flowtime ()
{

  # check if the file already exists, since we don't want to overwrite it.
  if [[ -e "$FLOWTIME_FILE" ]]; then
    echo "Error: Flowtime is already running. Use 'flowtime stop' to stop the current session" >&2
    exit 1
  fi

  echo "$(date +%s)" > "$FLOWTIME_FILE"
  current_hour=$(date +"%H:%m:%S")
  echo "Flowtime started at ${current_hour}. Recording start time." 
}

# -------------

case "$1" in
  start)
    start_flowtime
  ;;
  break) 
    calculate_break_time
  ;;
time)
  displayElapsedTime
  ;;
  stop)
    stop_flowtime
  ;;
esac


