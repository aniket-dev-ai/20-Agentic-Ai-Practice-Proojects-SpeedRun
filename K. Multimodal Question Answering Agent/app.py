from langchain_core.messages import HumanMessage
from image_utils import load_image_from_url, load_image_from_path
from agent import model
from langchain_core.output_parsers import StrOutputParser

def main( url:str , path:bool , query):
    print("Loading image...")
    if path:
        print("Loading image from local path...")
        encoded_image = load_image_from_path(url)
    else:
        print("Loading image from URL...")
        encoded_image = load_image_from_url(url)
    
    prompt = HumanMessage(
        content=[
            {"type": "text", "text": query},
            {
                "type": "image",
                "base64": encoded_image, 
            "mime_type": "image/jpg"
            }
        ]
    )
    res = model.invoke([prompt])
    return res.content[0]['text']     #type: ignore