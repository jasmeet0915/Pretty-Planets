import cv2
from random import randint, random
import numpy as np


def in_circle(sx, sy, cx, cy):
    dist = (sx - cx)**2 + (sy - cy)**2
    if dist < 300**2:
        return True
    else:
        return False

def overlay_shadow(orig_img, gray_img):
     # load shadow image with alpha channel
    shadow_img = cv2.imread("assets/shadow.png", -1)
    # extracting alpha channel from the image as a separate image for alpha mask
    shadow_alpha = shadow_img[:, :, 3]
    # converting the smile image back to BGR with only 3 channel without alpha channel
    shadow_img = shadow_img[:, :, 0:3]
    
    # create a black image for making mask
    mask_img = np.zeros(orig_img.shape[:2], dtype="uint8")

    # convert orig_img to 4 channel
    orig_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2BGRA)

    # detect circles(planet) in orig_img
    circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1.2, 100, maxRadius=300)
    print(circles)
        
    if circles is not None:
        circles = np.round (circles[0, :].astype("int"))

        for (x, y, r) in circles:
            # draw circle on mask img to create a mask for extracting shadow
            cv2.circle(mask_img, (x, y), r, (255, 255, 255), -1)
        
    # extract required shape of shadow image using above created mask but in 3 channel, no alpha
    shadow = cv2.bitwise_and(shadow_img, shadow_img, mask=mask_img)
    
    # create black-white shadow image that can be used as mask
    shadow_gray = cv2.cvtColor(shadow, cv2.COLOR_BGR2GRAY)
    (thresh, shadow_thresh) = cv2.threshold(shadow_gray, 10, 255, cv2.THRESH_BINARY)

    # extract alpha with shadow shape using shadow shape as mask
    shadow_alpha = cv2.bitwise_and(shadow_alpha, shadow_alpha, mask=shadow_thresh)
       
    # convert shadow back to 4 channel & add masked alpha as alpha channel
    shadow = cv2.cvtColor(shadow, cv2.COLOR_BGR2BGRA)
    shadow[:, :, 3] = shadow_alpha

    # overlay shadow on top of orig img
    final = cv2.add(shadow, orig_img)
    
    return final

def create_background_starfield(no_star_img, density):
    
    for star in range(0, density):
        # star properties [x, y, r]
        star_props = [randint(0, 1000), randint(0, 1000), randint(1, 3)]

        # check if star lies on planet then don't draw
        if in_circle(star_props[0], star_props[1], 500, 500):
            continue
        else:
            cv2.circle(no_star_img, (star_props[0], star_props[1]), star_props[2], (255, 255, 255), -1)

    return no_star_img 


def main():
    for i in range(0, 1024):
        base_img = cv2.imread("./images/{}.png".format(i))

        base_img_gray = cv2.cvtColor(base_img, cv2.COLOR_BGR2GRAY)

        shadow_img = overlay_shadow(base_img, base_img_gray)

        starred_img = create_background_starfield(shadow_img, density=500)

        cv2.imwrite("{}.png".format(i), starred_img)
        print("..............Written {}.png with Shadow & Starfield.............".format(i))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


