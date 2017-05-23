# GAN to generate handwritten and printed images
# Generate links, dates, times

import tensorflow as tf
import numpy as np
import os
import subprocess

def main():
    createImage()

def createImage(size, text, name, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

main()
