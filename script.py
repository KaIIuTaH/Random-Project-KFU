import smtplib
import getpass

print("Welcome to SMTP-client^^\nAuthorize") #внес небольшую правку
#для уменьшения длины кода

login = input("Input your login: ")
password = input("Input your password: ") #что дальше? =)

server = smtplib.SMTP(host='smtp.gmail.com', port = 587)
server.starttls()
server.login(login,password)
while True: #что оно вообще делает??
    slogin = input("Input your recipien's login: ")
    text = input("Input your message: ")
    server.sendmail(login,slogin,text)
