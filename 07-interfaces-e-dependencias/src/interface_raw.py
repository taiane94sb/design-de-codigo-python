from abc import ABC, abstractmethod

# Definir as regras de construção


class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None: pass


class EmailNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f'Email message - {message}')


class SMSNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f'SMS message - {message}')


class Notificator():
    def __init__(self, notificator_sender: NotificationSender) -> None:
        self.__notificator_sender = notificator_sender

    def send(self, message: str) -> None:
        # Validação de dados
        self.__notificator_sender.send_notification(message)

# obj = NotificationSender()
# obj.send_notification('Olá, Mundo!')


obj1 = EmailNotificationSender()
obj1.send_notification('Olá, Mundo!')  # Email message - Olá, Mundo!

obj2 = SMSNotificationSender()
obj2.send_notification('Olá, Mundo!')  # SMS message - Olá, Mundo!

obj3 = Notificator(EmailNotificationSender())
obj3.send('Olá, Mundo!')  # Email message - Olá, Mundo!

obj4 = Notificator(SMSNotificationSender())
obj4.send('Olá, Mundo!')  # SMS message - Olá, Mundo!
