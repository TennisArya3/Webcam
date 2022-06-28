import cv2
import dropbox
import time
import random
startTime=time.time()
def takepic():
    number= random.randint(0,100)

    cam=cv2.VideoCapture(0)

    result=True
    while(result):
        ret,frame=cam.read()
        imageName="img"+str(number)+".png"
        
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=False 
    return imageName
    print("Picture Taken")
    cam.release()
    cv2.destroyAllWindows()
def uploadImg(img):
    token="sl.BKaaer8-unIsQEmLyh_2hLqMcyazo_CjXBHEJxt_btXiGGJN-SPhJAXFtoQ9AOcVKRnaDRV_gvAmhia3U1T-F3LgrKPIO1gMPeXvRhcTN00BHsLPCfTIozq4e8qQLsSgxX_47zWBqVE"
    file=img
    source=file
    destination="/new folder/"+img
    dbx=dropbox.Dropbox(token)
    with open(source,"rb")as x:
        dbx.files_upload(x.read(),destination,mode+dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
    
def main():
    while True:
        if((time.time()-startTime)>=5):
            img=takepic()
            uploadImg(img)
main()