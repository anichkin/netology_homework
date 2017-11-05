import os
import subprocess

source = 'Source'
current_dir = os.path.dirname(os.path.abspath(__file__))
if __name__ == '__main__':
    images_dir = os.path.join(current_dir, source)
    images = os.listdir(images_dir)
    result_dir = os.path.join(current_dir, 'Result')
    if os.path.exists(result_dir) == False:
        os.mkdir(os.path.join(current_dir, 'Result'))
    for image in images:
        image_dir = (os.path.join(images_dir, image)).replace('\\','/')
        image_result_dir = (os.path.join(result_dir, image)).replace('\\','/')
        args_for_convert = ('convert ' + image_dir + ' -resize 200 ' + image_result_dir)
        process = subprocess.run(args_for_convert)
