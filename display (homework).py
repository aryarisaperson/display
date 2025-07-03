import cv2
image=cv2.imread("squidward.png")
print(image)


    


resize_input=int(input("Which resize do you want? Choose between 1-3:"))

if resize_input==1:
    size=(244, 228)
elif resize_input==2:
    size=(324, 244)
elif resize_input==3:
    size=(126, 244)


gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resize=cv2.resize(gray, size)
cv2.imshow("Loaded image.", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()





