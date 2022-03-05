# Re-rendering pdf with inverted colors(black-and-white)
## to save your eyes at night 


before             |  after
:-------------------------:|:-------------------------:
<img src="images/Screen Shot 2022-03-05 at 2.18.38 PM.png" alt="before_image" width="250"/>  |  <img src="images/Screen Shot 2022-03-05 at 2.19.19 PM.png" alt="before_image" width="250"/>
<img src="images/Screen Shot 2022-03-05 at 2.20.46 PM.png" alt="before_image" width="250"/>  |  <img src="images/Screen Shot 2022-03-05 at 2.19.51 PM.png" alt="before_image" width="250"/>

---
# how to run

first ,clone this repository:
`git clone https://github.com/salva-imm/pinverter`

this application is using [`pdf2image`](https://github.com/Belval/pdf2image)

you need to install some dependencies on your system before going further : )

```
Windows

Windows users will have to build or download poppler for Windows. I recommend @oschwartz10612 version which is the most up-to-date. You will then have to add the bin/ folder to PATH or use poppler_path = r"C:\path\to\poppler-xx\bin" as an argument in convert_from_path.
Mac

Mac users will have to install [poppler for Mac](http://macappstore.org/poppler/).
Linux

Most distros ship with pdftoppm and pdftocairo. If they are not installed, refer to your package manager to install poppler-utils
Platform-independant (Using conda)

    Install poppler: conda install -c conda-forge poppler
    Install pdf2image: pip install pdf2image
```

then, simply run this:

`pip3 install -r requirements.txt`

now you can invert your pdf colors

`python3 main.py /Path-to-your-pdf/my-doc.pdf`

TODO:
    - reduce generated file's size (now its too big)