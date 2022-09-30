import cv2

image = cv2.imread("/home/vest-tracker/Desktop/devRes/cv2_test_image")
dimensions = image.shape #image.shape gives the dimensions
print("pic dimensions: ", dimensions)

cv2.imshow('Preview',image)
cv2.waitKey(0) #waits for the spacebar to be pressed
cv2.destroyAllWindows()#destroys all windows when the spacebar is pressed

diffsize = input("resize to half size? (Y/N): ")
if diffsize.upper() == "Y":
    cv2.resize(image, (237,237))
    cv2.imwrite("/home/vest-tracker/Desktop/devRes/resized_test_image.png",image)
    
else:
    print("Thanks!")

(h,w,d) = dimensions