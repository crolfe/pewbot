from pewbot.commands.base import PewbotCommand

class Command(PewbotCommand):
    help = "Say pew again, I dare you!"
    def handle(self, message):
				if 'pewbot' not in message:	
						if 'pew?' in message
								return ["That's right I said pew muthafucka!"]
						if 'pew' in message
								return ['pew!']
