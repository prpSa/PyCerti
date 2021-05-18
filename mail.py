import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "uthakemarunga@gmail.com"  # Enter your address
receiver_email = "rajans2206@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")  #Oggy123@
message = """\
Subject: Kya Hila Dala na!!**!!
Kya bola tha mujhe maro..
Aa raha hu tuze marne ruk... """

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)