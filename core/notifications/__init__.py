class Notifier:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
        self.base_url = 'https://discordapp.com/api/webhooks'
