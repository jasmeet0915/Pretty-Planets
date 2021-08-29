import cv2
from random import randint

def main():
    base_img_index = randint(1, 12) 

    base_img = cv2.imread("assets/planets/{}.png".format(base_img_index))
    shadow_img = cv2.imread("assets/shadow.png")
    cv2.imshow("Image", shadow_img)
    cv2.imshow("base Image", base_img)


    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


