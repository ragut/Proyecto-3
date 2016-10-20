import os

class Filesystem():

    url_ori = None
    url_converted = None
    ulr_banner = None

    def __init__(self):
        self.url_ori = os.path.abspath(__file__ + "/../../tmp/original")+"/"
        self.url_converted = os.path.abspath(__file__ + "/../../tmp/converted")+"/"
        self.ulr_banner = os.path.abspath(__file__ + "/../../tmp/banner")+"/"

    def save_contest_banner(self, img, banner_file):
        img.save(self.ulr_banner+banner_file,"png")
        img.close()

    def save_original_video(self, video, file_name, original_file_extension):
        path = os.path.join(self.url_ori,file_name+"."+original_file_extension)
        fileObj = open(path, 'wb')
        fileObj.write(video)
        fileObj.close()

    def get_converted_url(self):
        return self.url_converted

    def get_original_url(self):
        return self.url_ori


