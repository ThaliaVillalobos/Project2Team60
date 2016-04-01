import requests
from bs4 import BeautifulSoup
import urllib
from Tkinter import *
import io
import os
import shutil
import time
from PIL import Image, ImageTk
import cStringIO


def search():
    app = Toplevel()
    app.geometry("1000x800")
    app.title("Tile Image")

    quitButton = Button(app, text="Quit",command=lambda:close_window(app), width = "10")
    quitButton.grid(row=0, column=2)
    
           
    tx1 = StringVar()
    tf = Entry(app, textvariable=tx1, width="100")
    b1 = Button(app, text="Search", command=lambda: searchPage(tx1,app), width="10")
    tf.grid(row=0, column=0)
    b1.grid(row=0, column=1)
    
    app.mainloop()
    

def searchPage(tx1,app):
    """
    if os.path.exists("\ImageTiles\.colormap.colormap"):
        os.remove("\ImageTiles\.colormap.colormap")
    """
    
    wordSearch = tx1.get()
    number = 0
    page = 1;
    
    #Crates a folder to hold the images
    if not os.path.exists("ImageTiles"):
        os.mkdir("ImageTiles")
    else:
        shutil.rmtree("ImageTiles")
        time.sleep(1)
        os.mkdir("ImageTiles")

    #Obtains images from istockphoto.com
    while page <= 1:
        url = "http://www.istockphoto.com/photos/%s?pageNumber':%s,'"%(wordSearch,page)
        sourceCode = requests.get(url)
        imageData = sourceCode.text
        soup = BeautifulSoup(imageData, "html.parser")

        for link in soup.findAll("img"):
            name = str(number)+ ".jpg"
            src = link.get('src')
            urllib.urlretrieve(src, "ImageTiles\\" + name)
            number += 1

            image = Image.open("ImageTiles\\" + name)
            photo = ImageTk.PhotoImage(image)
            tile = Label(app, image=photo)
            tile.image = photo
            tile.pack(side = "left") 
            
        page +=1   


def close_window(app):
    app.withdraw()
    app.quit()
    


#search()
