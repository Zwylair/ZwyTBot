import io
import typing
from PIL import Image
import aiogram


def pil_to_bytesio(image: Image.Image, ft: typing.Literal['PNG', 'JPEG'] = 'JPEG'):
    img_buffer = io.BytesIO()
    image.save(img_buffer, format=ft)
    img_buffer.seek(0)
    return img_buffer


def media_to_tg_file(bytes_io_or_pil: io.BytesIO | Image.Image):
    if isinstance(bytes_io_or_pil, Image.Image):
        return aiogram.types.InputFile(pil_to_bytesio(bytes_io_or_pil))
    return aiogram.types.InputFile(bytes_io_or_pil)
