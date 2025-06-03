# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python

# pip install pillow

from PIL import Image

from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpg'

pil_image = Image.open(ORIGINAL)

width, height = pil_image.size
# exif = pil_image.info['exif']      # info da imagem


# REDIMENSIONAR COM O MESMO ASPEC RATIO (SEM DESCONFIGURAR)
# width    -   new_width
# height   -   ???
# -> regra de três

new_width = 400
new_height = round(height * new_width / width)

print(width, height)
print(new_width, new_height)

# REDIMENSIONANDO
new_image = pil_image.resize((new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    #exif=exif,
)
