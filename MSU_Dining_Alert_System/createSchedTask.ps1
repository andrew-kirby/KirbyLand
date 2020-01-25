# Find the path we are working from and the path to scan.bat
$path = $PSScriptRoot
$scriptPath = $path + "\Scripts"
$scanFile = $scriptPath + "\scan.bat"

# Define where the main python file is
$pyFile = $PSScriptRoot + '\Scripts\MSU_Dining_Alert_Controller.py'

# Define the command to execute
$scanCommand = 'python.exe ' + $pyFile

# Create the batch file called by the task scheduler
#Set-Content $scanFile "python.exe $pyFile"
Set-Content $scanFile $scanCommand

# Create the task in task scheduler
#$action = New-ScheduledTaskAction -Execute $scanCommand `
$action = New-ScheduledTaskAction -Execute $scanFile `
  -Argument '-NoProfile -WindowStyle Hidden' `
  -WorkingDirectory $scriptPath
$trigger =  New-ScheduledTaskTrigger -Daily -At 6am
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "MSU DINING ALERT SYSTEM" -Description "Scans MSU menus and alerts members"

pause