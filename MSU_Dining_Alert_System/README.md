THE MSU MENU ALERT:
  Alerts users if special items appear on the Miller or Rendezvous Menu.

  REQUIRED MODULES:
  Use pip to install:
    -lxml
    -requests

  INITIAL SETUP:
  1. Populate Members
      - Add members in the Members folder according to the sample template.
  2. Include approprate email credentials
      - Enter appropriate email credentials into "emailcredentials-sample" and rename it to "emailcredentials". All alert emails will be sent from this email. You may need to enable some settings on your email account to allow the python service to automate an email from your account.
  3. Run "createSchedTask.ps1"
      - A scheduled task will be created which runs a menu scan daily at 6 am (provided you are logged into your computer)

  FUTURE ADDITIONS:
  - Make scheduled task work whenever the computer is on (not just when the user is logged in)
  - Add a log which records all email alerts sent out
