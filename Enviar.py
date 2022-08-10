from ast import Break
from multiprocessing import context
import smtplib
from email.message import EmailMessage
import ssl
import datetime
import dadosbd
import apiclimatempo as api

idemails = dadosbd.linhas

tempo = api.description
celcius = api.temperatura
for i in idemails:
    email_sender = 'emaildetestedevjr@gmail.com'
    email_password = 'yqwbxnpeompbzwvh'
    email_receiver = i[2]
    # password = 'yqwbxnpeompbzwvh'

    data = datetime.date.today()
    data = data.strftime('%d-%b-%Y')
    subject = 'Previsão do tempo '
    corpo_email = f"""
        Olá {i[1]}.
             
            >>{data}<< 
            Previsão do tempo da cidade de Recife hoje é {tempo} temperatura de {celcius}°C
            confirmando seu email: {i[2]}
        """

    msg = EmailMessage()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    msg.set_content(corpo_email)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context ) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())
    break