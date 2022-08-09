from multiprocessing import context
import smtplib
from email.message import EmailMessage
import ssl
import datetime

emails = ['laylagomess@outlook.com','vini_nascimentosilva@hotmail.com', 'juniormodern@hotmail.com']
for i in emails:
    email_sender = 'emaildetestedevjr@gmail.com'
    email_password = 'yqwbxnpeompbzwvh'
    email_receiver = i
    # password = 'yqwbxnpeompbzwvh'

    data = datetime.date.today()
    data = data.strftime('%d-%b-%Y')
    subject = 'Previsão do tempo '
    corpo_email = f"""
        Email teste.
            PREPARA QUE LÁ VEM SPAM INFINITO 
            >>{data}<< 
            Previsão do tempo hoje é {tempo} temperatura de {celcius}°C
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


