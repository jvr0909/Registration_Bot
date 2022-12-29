import email
from datetime import datetime

def most_recent_notif(messages):
    print("Getting Most Recent Notification")
    #Iterate through messages and extract data into the msgs list
    
    #Now we have all messages, but with a lot of details
    #Let us extract the right text and print on the screen

    #In a multipart e-mail, email.message.Message.get_payload() returns a 
    # list with one item for each part. The easiest way is to walk the message 
    # and get the payload on each part:
    # https://stackoverflow.com/questions/1463074/how-can-i-get-an-email-messages-text-content-using-python

    # NOTE that a Message object consists of headers and payloads.

    #create list storing course subject, number, and time of most recent notification
    

    most_recent_notification = []

    for response_part in messages[-1]:
        if type(response_part) is tuple:
            my_msg=email.message_from_bytes((response_part[1]))
            for part in my_msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=False)
                    #get day and time of email
                    time = my_msg['Date']
                    #find the word "Course" in the body
                    course_index = body.find("Course:") + 8
                    #get the course subject from course index to space
                    course_subject = body[course_index:].split()[0]
                    #get the course number from course index to space
                    course_number = body[course_index:].split()[1]
                    #convert time to datetime object
                    time = datetime.strptime(time, '%a, %d %b %Y %H:%M:%S %z')
                    most_recent_notification = (course_subject, course_number, time)
    return most_recent_notification