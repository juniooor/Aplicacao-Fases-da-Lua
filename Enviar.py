from email.message import EmailMessage
import datetime ,dadosbd, ssl, smtplib
import apiclimatempo as app

idemails = dadosbd.linhas
for i in idemails:
    
    tempo = app.api(i[3])
    email_sender = 'testesdevjremail@gmail.com'
    email_password = "rjolvirgaakyizrf"
    email_receiver = i[2]
    # password = 'yqwbxnpeompbzwvh'

    data = datetime.date.today()
    data = data.strftime('%d-%b-%Y')
    subject = 'Previsão do tempo '
    corpo_email = f"""
        Olá {i[1]}.
             
            Previsão do tempo em
                >{i[3]}< 
            {data}
            >{tempo[0]} 
            temperatura de 
            >{tempo[1]}°C
            
             Obrigado por participar do teste <3
            
            Link para descadastrar: https://forms.gle/mju8PNZR1ucXJW3LA 
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
        print('enviado')
        
        