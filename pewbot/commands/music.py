import soundcloud

from pewbot.base import PewbotCommand

class Command(PewbotCommand):
    help = "pewbot music me - post a random SoundCloud track from the provided genre"
    # client_id is tied to a SoundCloud app called "Pewbot"
    client = soundcloud.Client(client_id='b1bd1052f3afa0729bc9cdb745abe864')
    def handle(self, message, room_id):
        if message.startswith('pewbot music me'):
            try:
                response = []
                genre = message.split("pewbot music me")[1].strip()
                track = self.client.get('/tracks', q=genre)
                # Assumption: Campfire doesn't know what to do with an iframe,
                #  so let's do some ugly string manipulation
                iframe = self.client.get('/oembed', url=track[0].permalink_url).html
                iframe_tokens = iframe.split(" ")
                url = iframe_tokens[-1].split("\"")[1]
                response.append(url)
                return response
            except:
                return ["Error accessing the SoundCloud API"]