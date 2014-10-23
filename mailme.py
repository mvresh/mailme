def send_email():
    import smtplib

    gmail_user = "user gmail ID"
    gmail_pwd = "password"
    FROM = 'gmail_uswr@gmail.com'
    TO = ['gmail_target@gmail.com'] #must be a list if more than one
    SUBJECT = "Working??"
    TEXT = "write whatever you want"

    #  actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        #server = smtplib.SMTP(SERVER) 
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 
        print "print 1"
        server.ehlo()
        print "print 2"
        server.starttls()
        print "print 3"
        server.ehlo()
        server.login(gmail_user, gmail_pwd)
        print "print 4"
        server.sendmail(FROM, TO, message)
        print "print 5"
        #server.quit()
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

send_email()
