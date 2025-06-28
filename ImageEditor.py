from PIL import Image,ImageEnhance, ImageFilter
import os
#importing the library to edit pictures
path = 'FilePath'
outputPath = 'FilePath'

for fn in os.listdir(path):
    try:
        img = Image.open(f"{path}/{fn}")
        clean_name = os.path.splitext(fn)[0]
        print(clean_name)
        contrast = ImageEnhance.Contrast(img).enhance(1.25)
        contrast.save(f"{outputPath}/{clean_name}_contrast.jpg")
        
        grayscale = img.convert('L')
        grayscale.save(f"{outputPath}/{clean_name}_grayscale.jpg")
    except Exception as e:
        print(f'Unexpected error occured: {e}')
        continue
    

