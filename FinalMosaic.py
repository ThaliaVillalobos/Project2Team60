"""
Andrew Martin
Terra Fenton
Thalia Villalobos

The main purpose of this program is to create a mosaic image. To make it easier for the user we created an image
scraper for the small image (tiles). We used the website www.istockphoto.com to obtain the images that the user
wished to search (example "cat", "dog", "cars", and so on). To build the mosaic, we installed pymos.core library,
however, we had to edit the library because it wasn’t detecting all the images. We learned that for some of the images
core was not coverting the image to “RBG.” To make it user-friendly we created graphical user interfaces (GUIs) using Tkinter. 
"""

from Tkinter import *
import Tkinter
import tkFont
import tkMessageBox
from PIL import Image, ImageTk
import tkFileDialog
import sys
import os
import os.path
from pymos.core import build_mosaic
import Search


MAX_WIDTH = 10000

#Keeping track of image
COUNTER = 1

#Creating a window for the menu
root = Tk()
root.title("Mosaic program")
root.geometry("800x600")

#___________________________________________________________________________________________
class ImagesButton:
    #Buttons
    def __init__(self, master):
        bottomFrame = Frame(master)
        bottomFrame.pack(side=BOTTOM)

        self.quitButton = Button(bottomFrame, text="Quit", command=close_window)
        self.quitButton.pack(side=BOTTOM)

        self.lowQualityButton = Button(bottomFrame, text="Low Quality Mosaic Image", fg="blue", command= self.lowQuality)
        self.lowQualityButton.pack(side=BOTTOM)

        self.mediumQualityButton = Button(bottomFrame, text="Medium Quality Mosaic Image", fg="blue", command= self.mediumQuality)
        self.mediumQualityButton.pack(side=BOTTOM)

        self.highQualityButton = Button(bottomFrame, text="High Quality Mosaic Image", fg="blue", command= self.highQuality)
        self.highQualityButton.pack(side=BOTTOM)

        imageTitle = Image.open("C:\Users\Thalia\Desktop\Project 2\Title.jpg")
        photo = ImageTk.PhotoImage(imageTitle)
        self.Title = Label(image=photo)
        self.Title.image = photo
        self.Title.pack()
        

    def highQuality(self):
        global COUNTER
        
        #Search scraper  
        Search.search()

        #Displaying a window massage, telling the user to select their background image
        displayBackgroundMessage()
        imagePath = getImagePath()
        tileFolder = "ImageTiles"
        image = Image.open(imagePath)
        width = image.size[0]
        size = getMuilt(width)

        build_mosaic(
            input_path = imagePath,
            output_path="mosaicImage"+str(COUNTER)+".png",
            collection_path= tileFolder,
            #Enlarge image
            zoom = size,
            #Tile size
            thumb_size = 20,
            fuzz=10,
            new_colormap=False
        )

        COUNTER +=1
        displayFinishMessage()
      
        
    def mediumQuality(self):
        global COUNTER
        Search.search()
        displayBackgroundMessage()    
        imagePath = getImagePath()
        tileFolder = "ImageTiles"
        image = Image.open(imagePath)
        width = image.size[0]
        size = getMuilt(width)

        build_mosaic(
            input_path = imagePath,
            output_path="mosaicImage"+str(COUNTER)+".png",
            collection_path= tileFolder,
            #Enlarge image
            zoom = size,
            #Tile size
            thumb_size = 40,
            fuzz=10,
            new_colormap=False
        )
        
        COUNTER +=1
        displayFinishMessage()



    def lowQuality(self):
        global COUNTER
        Search.search()
        displayBackgroundMessage()    
        imagePath = getImagePath()
        tileFolder = "ImageTiles"
        image = Image.open(imagePath)
        width = image.size[0]
        size = getMuilt(width)

        build_mosaic(
            input_path = imagePath,
            output_path="mosaicImage"+str(COUNTER)+".png",
            collection_path= tileFolder,
            #Enlarge image
            zoom = size,
            #Tile size
            thumb_size = 80,
            fuzz=10,
            new_colormap=False
        )
        
        COUNTER +=1
        displayFinishMessage()


def displayBackgroundMessage():
    tkMessageBox.showinfo("Message", "Please select your main background image")


def displayFinishMessage():
    tkMessageBox.showinfo("Message", "Your Mosaic Image is Done :) , you can find it in your folder")
    

def getImagePath():
    #Opens the file, so the user can select the main background image
    path = Tkinter.Tk()
    path.withdraw()
    filename = tkFileDialog.askopenfilename(parent=path, title="Select your main background image")

    return filename


def getMuilt(imageWidth):
    muilt = MAX_WIDTH/imageWidth

    return muilt


def close_window():
    root.destroy()



mainWindow = ImagesButton(root)
root.mainloop()



