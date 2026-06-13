import base64
import requests
import base64, httpx

def load_image_from_url(url: str, timeout: int = 10) :
    """
    Download an image from a URL and return it as a PIL Image.
    """
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()
    return base64.b64encode(httpx.get(url).content).decode("utf-8")

def load_image_from_path(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')