# nft-vision-hack

 * `generator.ipynb` script loads the background and other different trait features and layers them together uniquely and randomly to create a final planet image 
    with a plain background.
 * `nft-generator.py` script finally uses opencv to add a shadow to the planet using masking and alpha blending using the `overlay_shadow()` method. Currently it 
 puts the same shadow over the planets but there are much more possibilities here! The script then makes use of the `create_background_starfield()` method to create
 a random starfield in the background with a certain density and randomly placed and sized stars.
 
The `images` directory contains only some example images as we couldn't upload all the 1024 generated images.
