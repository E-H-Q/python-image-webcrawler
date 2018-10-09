import re
import requests
from bs4 import BeautifulSoup

url = "http://www.fiftythree.org/etherkiller/"

def main(url: str):
    image_regex = re.compile(".jpg$|.png$|.gif$")
    page_resp = requests.get(url)
    if not page_resp:
        return print(url, page_resp.status_code)

    html = BeautifulSoup(page_resp.text, "html5lib")
    images_found = html.find_all("a", {"href": image_regex})
    if images_found:
        print ("Found",len(images_found),"images")
        for image in images_found:
            save_image(image)

def save_image(image):
    image_resp = requests.get(f'{url}{image["href"]}')
    if not image_resp:
        print (image, image_resp.status_code)
    else:
        filename = f"images/{image['href'].split('/')[-1]}"
        print (f"Saving {filename}")
        with open(filename, "wb") as image_file:
            image_file.write(image_resp.content)

if __name__ == "__main__":
    main(url)
