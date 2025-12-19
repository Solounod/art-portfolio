import os
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.base import ContentFile

def optimize_image(image_field, max_width=1200):
    """
    Takes an image field, resizes it, and converts it to WebP.
    Args:
    image_field: The image field from the model (e.g., self.cover_image)
    max_width (int): The maximum allowed width. Default is 1200px (Full HD web).
    Returns:
    ContentFile: The processed file ready to save.
    """
    if not image_field or not hasattr(image_field, 'file'):
        return None
    
    img = Image.open(image_field)
    img = ImageOps.exif_transpose(img)

    if img.mode in ("P", "CMYK"):
        img = img.convert("RGB")

    if img.width > max_width:
        ratio = max_width / float(img.width)
        height = int((float(img.height) * float(ratio)))
        img = img.resize((max_width, height), Image.Resampling.LANCZOS)

    buffer = BytesIO()
    img.save(buffer, format="WEBP", quality=85, optimize=True)
    buffer.seek(0)

    filename = os.path.basename(image_field.name)
    name, _ = os.path.splitext(filename)
    new_filename = f"{name}.webp"

    return ContentFile(buffer.read(), name=new_filename)