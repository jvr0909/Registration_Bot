import yaml
import imaplib


def most_recent_notif():
    print("Logging in to gmail")
    with open("credentials.yml") as f:
        content = f.read()
    
    # from credentials.yml import user name and password
    my_credentials = yaml.load(content, Loader=yaml.FullLoader)
    #Load the user name and passwd from yaml file
    user, password = my_credentials["gmail_user"], my_credentials["gmail_password"]
    #URL for IMAP connection
    imap_url = 'imap.gmail.com'
    # Connection with GMAIL using SSL
    my_mail = imaplib.IMAP4_SSL(imap_url)
    try:
        my_mail.login(user, password)
        print ("LOGIN SUCCESSFUL!!! ")
        # Select the Inbox to fetch messages
        my_mail.select('Inbox')
    except imaplib.IMAP4.error:
        print ("LOGIN FAILED!!! ")
        return

    
    #Define Key and Value for email search
    #For other keys (criteria): https://gist.github.com/martinrusev/6121028#file-imap-search
    print ("Getting All Emails From Course Explorer")
    key = 'FROM'
    value = my_credentials["illinois_email"]
    _, data = my_mail.search(None, key, value)  #Search for emails with specific key and value

    mail_id_list = data[0].split()  #IDs of all emails that we want to fetch 

    msgs = [] # empty list to capture all messages
    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)') #RFC822 returns whole message (BODY fetches just body)
        msgs.append(data)
    return msgs
