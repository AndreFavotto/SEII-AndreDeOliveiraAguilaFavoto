import os, time, concurrent.futures
from PIL import Image, ImageFilter


img_names = []
for file in os.listdir('../Thread/photos_thread06'):
    img_names.append(file)

t1 = time.perf_counter()

size = (1200, 1200)

#Without multiprocessing
""" for img_name in img_names:
    img = Image.open(f'../Thread/photos_thread06/{img_name}')

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'photos_multiprocessing06/{img_name}')
    print(f'{img_name} was processed...')
 """

#With multiprocessing
def process_image(img_name):
    img = Image.open(f'../Thread/photos_thread06/{img_name}')

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'photos_multiprocessing06/{img_name}')
    print(f'{img_name} was processed...')


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')