from gmail_login import get_emails
from most_recent_notif import getMostRecentNotif
from check_last_10 import withinLast10Minutes
from registration import register
def main(event, context):
    messages = get_emails()
    most_recent_notification = getMostRecentNotif(messages)
    is_recent = withinLast10Minutes(most_recent_notification)
    register(is_recent, most_recent_notification)

print("Starting main")
main(None, None)
print("Finished main")
