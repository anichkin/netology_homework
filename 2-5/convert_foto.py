import os
import subprocess

source = 'Source'
current_dir = os.path.dirname(os.path.abspath(__file__))
process = subprocess.run('convert')
print(process.args)
if __name__ == '__main__':
    print(current_dir)
    images = os.listdir(os.path.join(current_dir, source))
    images_dir = os.path.join(current_dir, source)
    result = os.path.join(current_dir, 'Result')
    for convert_foto, image in enumerate(images):
        image_dir = os.path.join(images_dir, image)
        result_image_dir = os.path.join(result, image)
        print(image_dir)
        print(result_image_dir)
        process = subprocess.run('convert image_dir  -resize 200 result_image_dir')

