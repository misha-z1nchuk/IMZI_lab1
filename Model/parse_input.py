from PIL import Image
from Model.persons_enum import EnumPerson
import os

list_ph = []


def parse(target):
    X = []
    Y = []

    dir_name = EnumPerson

    def rec_path(path):
        if os.path.basename(path) != "origin":
            global dir_name
            if os.path.isdir(path):
                lst_dir = os.listdir(path)
                if os.path.basename(path) == "barack_obama":
                    dir_name = EnumPerson.BARACK_OBAMA
                elif os.path.basename(path) == "elon_musk":
                    dir_name = EnumPerson.ELON_MUSK
                elif os.path.basename(path) == "jeff_bezos":
                    dir_name = EnumPerson.JEFF_BEZOS
                elif os.path.basename(path) == "mark_zuckerberg":
                    dir_name = EnumPerson.MARK_ZUCKERBERG
                elif os.path.basename(path) == "steve_jobs":
                    dir_name = EnumPerson.STEVE_JOBS
                elif os.path.basename(path) == "volodymyr_zelensky":
                    dir_name = EnumPerson.VOLODYMYR_ZELENSKY

                for elem in lst_dir:
                    rec_path(path + "/" + elem)
            else:
                im = Image.open(path)
                imageSizeW, imageSizeH = im.size
                pixel = []
                for i in range(0, imageSizeW):
                    for j in range(0, imageSizeH):
                        pixel.append(im.getpixel((i, j)))
                x_row = []

                for i in range(0, len(pixel)):
                    x_row.append(pixel[i][0] / 256.0)

                if len(x_row) == 10000:
                    global list_ph
                    X.append(x_row)
                    Y.append(dir_name.value)
                    list_ph.append(path)

    rec_path('../Base/' + target)

    return X, Y, list_ph
