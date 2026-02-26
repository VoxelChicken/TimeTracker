#!/bin/bash

x=1 # For looping purposes
program_to_check=$(cat program_to_check) # To know which program to look for
program_to_run=$(cat program_to_run) # To know what program to run via Flatpak

flatpak run $program_to_run

while [ $x -eq 1 ]; do
  sleep 1
  if [[ $(ps | grep $program_to_check) ]]; then # Continuously check if the program is running.
    continue
  else # If it can't be found (alias isn't running,)
    exit # Exit the shellscript (which continues on with the atexit.register() function in python.)
  fi
done
