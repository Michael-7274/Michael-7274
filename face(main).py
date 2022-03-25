import time

import cv2
import cv2 as t
import sys
import keyboard
import os
import time as y1
print("To exit hold Q")
# def check():
#     i=0
#     j=0
#     image = cv2.imread('D:\FD\Suspect.png')
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cascPath = "haarcascade_mcs_mouth.xml"
#     mouthCascade = cv2.CascadeClassifier(cascPath)
#     mouth = mouthCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.2,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )
#     for (x, y, w, h) in mouth:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         i=i+1
#     cascPath = "haarcascade_mcs_nose.xml"
#     noseCascade = cv2.CascadeClassifier(cascPath)
#     nose = noseCascade.detectMultiScale(
#             gray,
#             scaleFactor=1.2,
#             minNeighbors=5,
#             minSize=(30, 30),
#             flags=cv2.CASCADE_SCALE_IMAGE
#         )
#     for (x, y, w, h) in nose:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         j = j + 1
#     if i==1 & j==1 :
#         cv2.imwrite('D:\FD\confirmed\confirmed.png',image)
# def k():
#     os.system('python face(check).py')
#     time.sleep(2)
def v():

    c = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cascPath = "haarcascade_frontalface_default.xml"

    while(True):
        t1 = 0
        global a
        a='s'
        if keyboard.is_pressed('q'):
            a = 'q'
            break
        ret, frame = c.read()
        # Create the haar cascade
        t.imwrite("me.png", frame)
        faceCascade = cv2.CascadeClassifier(cascPath)
        # Read the image
        image = cv2.imread('me.png')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('test', gray)
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        print(len(faces))
        # print(type(faces))
        # cv2.imshow("f",faces)
        # print("Found {0} faces!".format(len(faces)))

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            t1=t1+1
        cv2.imshow("Faces found", image)
        # print(type(faces))
        cv2.waitKey(1) & 0xFF
        if t1!=0:
            cv2.imwrite('D:\FD\Suspect.png',image)
            # check()
            i=0
            j=0
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cascPath = "haarcascade_mcs_mouth.xml"
            mouthCascade = cv2.CascadeClassifier(cascPath)
            mouth = mouthCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            for (x, y, w, h) in mouth:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                i = i + 1
            cascPath = "haarcascade_mcs_nose.xml"
            noseCascade = cv2.CascadeClassifier(cascPath)
            nose = noseCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            s=y1.strftime("%H_%M_%S")
            for (x, y, w, h) in nose:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                j = j + 1
            if i == j:
                cv2.imwrite(f'D:\FD\confirmed\confirmed{s}.png', image)

            # # os.system('python check.py')
            # k()
            # os.system('python face(check).py')
            #
            break
        else:
            continue
            # cv2.waitKey(0)
        #
        cv2.waitKey(1) & 0xFF

    c.release()
    t.destroyAllWindows()

# with open('D:\FD\_1.txt', 'w') as file:
#     file.write("Iteration 1")
# with open('D:\FD\confirmed\_2.txt', 'w') as file:
#     file.write("Iteration 1")
# print(os.system('mkdir D:\FD'))
# print(os.system("mkdir D:\FD\confirmed"))
os.system('file_creator.py')
time.sleep(5)
# print("File created")
# except:
#s=0

while True:
    v()

    if keyboard.is_pressed('q') :
        print("pressed")
        break
    if a=='q':
        break
    #s=s+1
    # if a=='q':
    #     break
    # a=str(input())
    # if(a=='q'):
    #     break

# def check():
#
#     image = cv2.imread('D:\Suspect.png')
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cascPath = "haarcascade_mcs_mouth.xml"
#     mouthCascade = cv2.CascadeClassifier(cascPath)
#     mouth = mouthCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.2,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )
#     for (x, y, w, h) in mouth:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.imwrite('D:\Confirmed.png',image)


#_______________________________________________________________________________________________________________________
# def v():
#     l=0
#     c=t.VideoCapture(0)
#     i=1
#     while(True):
#         l=l+1
#     #read is going to return true if the frame is available, ret saves the true or false value
#         ret,frame=c.read()
#     # ret,frame = t.VideoCapture(0).read();
#
#     #To save an image from the video
#     # if t.waitKey(1) ==ord('c'):
#     #     t.imwrite("me.png",frame)
#     #     if cv2.waitKey(1) & 0xFF==ord('s'):
#         t.imshow("video",frame)
#
#
#         if l ==30:
#             i+=1
#             cv2.imwrite(f"D:\copy{i}.png",frame)
#         if keyboard.is_pressed('q'):
#             break
#         # if cv2.waitKey(1) & 0xFF ==ord('Q'):
#         #     break
#         cv2.waitKey(1) & 0xFF
#     c.release()
#     t.destroyAllWindows()