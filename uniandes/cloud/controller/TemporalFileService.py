import os

class TemporalFileService:
    url_original = None
    url_banner = None
    url_converted = None

    def __init__(self):
        self.url_original = os.path.abspath(__file__ + "/../../tmp/original")+"/"
        self.url_banner = os.path.abspath(__file__ + "/../../tmp/banner")+"/"
        self.url_converted = os.path.abspath(__file__ + "/../../tmp/converted")+"/"