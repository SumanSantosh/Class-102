import cv2
import dropbox
import time
import random

#Storing the starting time
start_time = time.time()

def take_snapshot():
    #Generating a random number to name the picture
    number = random.randint(0,100)
    #Initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        #Reading the frame and storing it under the variable frame
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        #Imwrite is used to save the image with the provided name
        cv2.imwrite(img_name,frame)
        result = False
    
    return(img_name)
    
    print("The Snapshot has been taken !!")

    #Releasing the camera
    videoCaptureObject.release()
    #Closing all the windows opened for the process
    cv2.destroyAllWindows()

def upload_File(img_name):
    access_token = "Iql5ai1OduoAAAAAAAAAASXl1E2Yr2gFVkFbIrW6G5fSQ4-LckioucP7qWmuZYj7"
    file = img_name
    file_from = file
    file_to = "/testfolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open (file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite) 
        print("File Uploaded")

def main():
    while(True):
        if ((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_File(name)

main()