# urls_monitor

This script checks if a list of URLs is reachable usin **ping** command. If any URLs are down, it sends a notification to alert the user.

- **FEATURES**:
  
  - Reads URLs from a text file (urls.txt).
  - Uses ping to check if URLs are online.
  - Sends system notifications when a URL is down (Linux by default,    but supports Windows and macOS with minor modifications).
  - Runs continuously with a delay between notifications (5 seconds).

- **REQUIREMENTS**:

  - Python3
  - To adapt the script for Windows or macOS, update the           
    **send_notification** function accordingly.

- **SYSTEM COMPATIBILTY**:
  
  - ***Linux*** (default): Uses notify-send.
  - ***Windows***: Uses PowerShell message boxes
  - ***macOS***: Uses AppleScript
  
