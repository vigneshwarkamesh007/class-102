from os import access
import time 
import random
from tracemalloc import start
import dropbox
import cv2

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    #initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any stroage device
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("sanpshop taken")    

    #release the camera 
    videoCaptureObject.release()
    #closes all the window that might be opned during process
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token=""
    file=img_name
    file_from=file
    file_to="/newfolder1/"+(img_name)
    dbx=dropbox.dropBox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


      
def main():
     while(True):
          if ((time.time() - start_time) >= 5):
              name = take_snapshot()
              upload_file(name)


main()
 

              
               

