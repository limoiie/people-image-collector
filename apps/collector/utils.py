import numpy
import face_recognition
from PIL import Image
import uuid
import os
import matplotlib.pyplot as plt


def convert_pillow_image_to_numpy_array(image: Image.Image):
    image_pixels = numpy.array(image.getdata(), dtype='uint8')
    image_pixels.reshape((image.size[0], image.size[1], 3))
    return image_pixels.transpose()


def load_images_from_file_paths(file_paths: list):
    return [face_recognition.load_image_file(file_path) for file_path in file_paths]


def crop_image(image: numpy.array, row_range, col_range):
    return image[row_range[0]:row_range[1], col_range[0]:col_range[1]]


def generate_an_random_string(string_len: int):
    return uuid.uuid4().hex[:string_len]


def generate_an_non_exist_file_path(folder, file_template):
    while True:
        uuid_string = uuid.uuid4().hex
        file_name = file_template % uuid_string[:16]
        file_path = os.path.join(folder, file_name)
        if not os.path.exists(file_path):
            return file_path
    pass


def show_image(image, title):
    plt.figure('IMAGE')
    plt.imshow(image)
    plt.title(title)
    plt.show()
