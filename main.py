import gmail_login
import most_recent_notif
import check_last_10

def main():
    messages = gmail_login.most_recent_notif()
    most_recent_notification = most_recent_notif.most_recent_notif(messages)
    is_recent = check_last_10.check_last_10(most_recent_notification)
    print(is_recent)



if __name__ == "__main__":
    main()