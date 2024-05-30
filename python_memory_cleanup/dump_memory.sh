#!/bin/bash

# input process name

# delimiter
IFS=$'\n'

# Run the ps command and grep for the desired process
read -a output <<< $(ps -ef | grep "$1")

# Extract the PID from the output
# syntax of '{ print $2}' is explained in man awk, 4. Records and fields.
# Simply put, it's an action defined in awk to print second splited string i.e. pid.
target_pid=$(echo "${output[0]}" | awk '{print $2}')

echo "pid is $target_pid"

# Check if the PID is not empty
if [[ -n $target_pid ]]; then
  # Run gcore with the extracted PID
  sudo gcore $target_pid
else
  echo "Process not found."
fi