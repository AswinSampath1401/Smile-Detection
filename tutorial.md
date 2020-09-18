# Welcome to the Tutorial

## Steps Followed

1) Load the Haar cascade classifiers for face and smile <br>
(Link to the cascade are found <a href='https://github.com/opencv/opencv/tree/master/data/haarcascades'>here</a>)

2) Enter the path of your image in the main.py file

3) The image is sent to 
``` getmodel(img) ``` function to predict maximum number of faces possible

4) Every face is then scanned to predict whether the person is smiling or not and a rectangle is drawn around their smile

5) Region of smile predicted are sorted by their width size and displayed

```
    smile =sorted(smile,key=lambda x: x[2],reverse=True)
```

6) See the comments for explanation for each command


# Real Time Smile detection 

<p> Process is similar to reading a picture</p>

## Refer comments in the file 
<a href='realtime_smile_detect.py'>Realtime</a> for line by line understanding

# Outputs

<img src='Images\Screenshots\real_o1.PNG' style="width:300px;height:300px;">
<span><img src='Images\Screenshots\real_o2.PNG' style="width:300px;height:300px;">

