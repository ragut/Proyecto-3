import os

class FileController():

    fileSystem = None

    def __init__(self):
        self.fileSystem = OwnMachine()

    def save_contest_banner(self, img, banner_file):
        self.fileSystem.save_contest_banner(img, banner_file)

    def save_original_video(self, video, video_name, original_file):
        self.fileSystem.save_original_video(video,video_name,original_file)

    def delete_video(self, video):
        self.fileSystem.delete_video(video)

    def save_converted_image(self, img, design):
        self.fileSystem.save_converted_image(img,design)

    def save_thumbnail_image(self, img, design):
        self.fileSystem.save_thumbnail_image(img,design)

    def get_original_url(self):
        return self.fileSystem.get_original_url()

    def get_converted_url(self):
        return self.fileSystem.get_converted_url()