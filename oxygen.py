from PIL import Image
import numpy as np

def image_to_array(image_path):
  """
  Loads JPEG image into 3D Numpy array of shape 
  (width, height, channels)
  """
  with Image.open(image_path) as image:         
    im_arr = np.fromstring(image.tobytes(), dtype=np.uint8)
    im_arr = im_arr.reshape((image.size[1], image.size[0], 4))                                   
  return im_arr


im = image_to_array("/Users/alexgalkin/Documents/competitive/BWINF1.py/oxygen.png")

# print(im)
# allnum = [i[0] for i in im[45]]
#allnum = list(map(lambda x:chr(x[0]),im[45]))
allnum = [105, 110, 116, 101, 103, 114, 105, 116, 121]
# allnum = list(map(lambda x:chr(x),allnum))
#print("".join([chr(a) for a in allnum]))
print(allnum[-1:1:-1])