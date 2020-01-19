from google.cloud import vision
import requests
def detect_text(path):
    """Detects text in the file."""
    import io
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    number = 0
    isnumber = 1
    list = str.split(texts[0].description)
    print(list[0])
    url = 'http://169.233.251.177:4000/api/img-lookup'
    myobj = {'housenumber': list[0]}
    x = requests.post(url, data = myobj)

detect_text("secondimg.jpg")


