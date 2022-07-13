import random

def file(filename):
    f = open(filename)
    imgs = f.read().splitlines()
    random.shuffle(imgs)
    return imgs