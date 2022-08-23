from email.message import EmailMessage
import datetime ,dadosbd, ssl, smtplib
import apiclimatempo as api

idemails = dadosbd.linhas
for i in idemails:
    tempo = api.description
    celcius = api.temperatura
    cityapi = api.nomecity
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
            Previsão do tempo da cidade de {cityapi} 
            >>>>{tempo} 
            temperatura de 
            >>>>{celcius}°C
            
            PS: perdoem os envios de email, tá em fase de teste
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
        
        