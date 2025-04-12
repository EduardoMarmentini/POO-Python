class Notion:
    def send(self, message: str):
        pass


class EmailNotion(Notion):
    def send(self, message: str):
        print(f"[EMAIL] {message}")


class SMSNotion(Notion):
    def send(self, message: str):
        print(f"[SMS] {message}")
