import sys
import tempfile
from PIL import Image, ImageOps, ImageEnhance
from pdf2image import convert_from_path


def invert(pdf_path):
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path('pdf_path', output_folder=path)
        black_and_white_images = []
        for im in images_from_path:
            baw = im.convert('RGB').convert('L')
            im_invert = ImageOps.invert(baw)
            enhancer = ImageEnhance.Contrast(im_invert)
            final_image = enhancer.enhance(7.0)
            black_and_white_images.append(final_image)
    black_and_white_images[0].save("out.pdf", save_all=True, append_images=black_and_white_images[1:])

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    invert(pdf_path=pdf_path)
