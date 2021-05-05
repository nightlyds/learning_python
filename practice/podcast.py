import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('PODCAST')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('podcast.log')
handler.setLevel(logging.WARNING)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

class Youtube:

    def __init__(self, name):
        logger.warning(f'NEW YOUTUBE: {name}')
        self.name = name

        self.__channels = []
        self.__viewers = []
        self.__podcasts = []

    def __str__(self):
        return 'Youtube'

    @property
    def Channels(self):
        return f'Channels: {self.__channels}'

    @Channels.setter
    def Channels(self, channel):
        logger.warning(f'NEW CHANNEL CREATED: {channel}')
        self.__channels.append(channel)

    @property
    def Viewers(self):
        return f'Viewers: {self.__viewers}'

    @Viewers.setter
    def Viewers(self, viewer):
        logger.info(f'NEW VIEWER ADDED: {viewer}')
        self.__viewers.append(viewer)

    @property
    def Podcasts(self):
        return f'Podcasts: {self.__podcasts}'

    @Podcasts.setter
    def Podcasts(self, podcast):
        logger.info(f'NEW PODCAST ADDED: {podcast}')
        self.__podcasts.append(podcast)

youtube = Youtube('Youtube')

print(f'CREATE NEW PLACE FOR VIDEOS: {youtube}')

youtube.Channels = 'Channel 1'
youtube.Channels = 'Channel 2'
youtube.Channels = 'Channel 3'

youtube.Viewers = 'Viewer 1'
youtube.Viewers = 'Viewer 2'
youtube.Viewers = 'Viewer 3'
youtube.Viewers = 'Viewer 4'
youtube.Viewers = 'Viewer 5'

youtube.Podcasts = 'Podcast 1'
youtube.Podcasts = 'Podcast 2'


print(f"""
    Channels: {youtube.Channels},
    Viewers: {youtube.Viewers},
    Podcasts: {youtube.Podcasts}
""")