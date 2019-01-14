
import sys

def main(argv):
    pixels = []
    image = argv[0]
    transformed = []

    FOCAL_LENGTH = 1000
    SENSOR_X = 2000
    SENSOR_Y = 1000
    CAMERA_X = SENSOR_X/2
    CAMERA_Y = SENSOR_Y/2
    with open(image) as file:
        for p in file:
                p = p.strip()
                p = p.split(" ")
                x = float(p[0])/float(p[2])
                y = float(p[1])/float(p[2])

                u = FOCAL_LENGTH * x + CAMERA_X
                v = FOCAL_LENGTH * y + CAMERA_Y


                if (u > 0 and u < 2000) and (v > 0 and v < 1000):
                    pixels.append([u,v])


    print(pixels)

if __name__=='__main__':
  main(sys.argv[1:])
