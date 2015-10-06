import os

#runnning the script to retrieve the shutterspeed settings from the camera and store in variable tree
tree = os.popen("gphoto2 --get-config shutterspeed").read()

#save variable tree as a ext file for processing
with open("Shutterspeed.txt", "w") as text_file:
    text_file.write(format(tree))

#Lets read the file and retrieve the line with the current shutterspeed
f=open('Shutterspeed.txt')
shutterspeed_line=f.readlines()
shutter_speed =  shutterspeed_line[2]
shutter_speed = shutter_speed[9:]
print shutter_speed


