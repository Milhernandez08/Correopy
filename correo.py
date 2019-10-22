import smtplib
from decouple import config


class Correo():
    def __init__(self, correo):
        self.correo = correo
    
    def enviar(self):

        message = "Su cuenta ha sido ACTIVADA"
        subject = "ACTIVACION DE CUENTA"

        message = 'Subject: {}\n\n{}'.format(subject, message)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('aliveearth@ids.upchiapas.edu.mx', 'AliveMARH')

        server.sendmail('aliveearth@ids.upchiapas.edu.mx', self.correo, message)

        server.quit()

        return "Enviado"

