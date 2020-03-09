import io
import base64
from PIL import Image

def generate(status):
  img = Image.new('RGB', (status, 1), color = 'red')
  data = io.BytesIO()
  img.save(data, "JPEG")
  return data.getvalue()