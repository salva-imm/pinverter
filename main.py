import tempfile
import uuid
from PIL import Image, ImageOps, ImageEnhance
from pdf2image import convert_from_path

with tempfile.TemporaryDirectory() as path:
    pdf_path = ""
    images_from_path = convert_from_path('pdf_path', output_folder=path)
    black_and_white_images = []
    for im in images_from_path:
        baw = im.convert('RGB').convert('L')
        im_invert = ImageOps.invert(baw)
        enhancer = ImageEnhance.Contrast(im_invert)
        final_image = enhancer.enhance(7.0)
        black_and_white_images.append(final_image)
black_and_white_images[0].save("out.pdf", save_all=True, append_images=black_and_white_images[1:])