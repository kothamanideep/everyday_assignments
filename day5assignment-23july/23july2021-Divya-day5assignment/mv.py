#from moviepy.editor import *
#clip = VideoFileClip("C:\Users\divya.km\Documents\virtual_class_video\d-1 ")
#clip = clip.subclip(0, 10)
c#lip.dispaly()


from moviepy.editor import *
 
# loading video dsa gfg intro video
clip = VideoFileClip("C:\Users\divya.km\Pictures\Camera Roll\VIRTUAL SESSION ON TECHNICAL AND CORE-20210722 0402-1")
 
# clipping of the video
# getting video for only starting 10 seconds
clip = clip.subclip(0, 10)
 
# rotatng video by 180 degree
clip = clip.rotate(180)
 
# Reduce the audio volume (volume x 0.5)
clip = clip.volumex(0.5)
 
# showing clip
clip.ipython_display(width = 280)