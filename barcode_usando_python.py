!pip install python-barcode

import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, DisplayObject

barcode_format = barcode.get_barcode_class('ean13')

barcode_number = barcode_format('5901234123457', writer=ImageWriter())

barcode_image = barcode_number.save('barcode_filename')

display(Image(filename=barcode_image))
