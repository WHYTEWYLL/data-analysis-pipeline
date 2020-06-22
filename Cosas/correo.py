import smtplib  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass
def correo():
    email1=input("Introduce tu correo:")
    email2=input("Introduce correo dest:")

    msg=MIMEMultipart()

    msg['From'] = email1 

    msg['To'] = email2 

    msg['Subject'] = "Netflix and Chill"

    body = "Opciones de peli a tu disposición, para pasar un buen rato"

    msg.attach(MIMEText(body, 'plain')) 

    filename = "Report.pdf"
    attachment = open("Output/Plot.png", "rb") 
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    loco=getpass("Contraseña:")
    s.login(email1, loco) 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(email1, email2, text) 
    
    # terminating the session 
    s.quit()
    return True