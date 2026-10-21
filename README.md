# LimboVR (Name in progress)

This project is a work in progress, not a full working project.

Welcome to my project, LimboVR (name in progress). I am creating this project to make fullbody tracking in VR more accessible.

# IMPORTANT ANNOUNCEMENT 10/20/2026:

Hello, everybody (The one person who starred this project). I apologize for the extended hiatus on this project. I have both been working many hours and studying very heavily and also have switched over to Linux as of August (Hence the hiatus in July), which does not want to cooperate with my VR headset. So I can no longer test LimboVR. That being said, I will be installing a new drive with windows on my system soon, solely to work on this, and other VR related projects in the future. I am happy to announce that a large portion of my free time will go to working on my VR projects again. Also, I would like to eventually get a Linux compatible headset so that I can test my software on Linux as well before releasing a broken version to the public. It should have an up and running windows alpha release by Halloween and hopefully a full GUI and compatibility update shortly following. Thank you to anybody who may be following along this project, it means the world to me. Yours truly, BungleBun.

# What does this project do/plan to do?

LimboVR takes the user's webcam feed using opencv and uses mediapipe to map the user's body out with a skeletal rig. Using an advanced google machine learning model it uses pose estimation to smoothly translate the 2 dimensional camera movements into 3d fully tracked body movements. It then uses the tracked position of the mapped skeletal rig and maps it to your in-game virtual reality character.

Using the VRChat OSC it will translate your fullbody movements smoothly onto any avatar. There is also a plan to use OpenVR drivers to make this project compatible with any SteamVR game with FBT features as well.

Thus far I am only working on making it run on PCVR but I hope to eventually find ways to make it run smoothly on any setup, whether that be PCVR and webcam, standalone and mobile camera, PCVR and mobile camera, or standalone and webcam. 

# Fancy tech lingo:

Languages:
    -Python

Libraries:
    -OpenCV
    -Mediapipe
    -Numpy
    -Time
    -Python-OSC
    -TBD

Frameworks:
    -TBD

# How to run:

This project is a work in progress. It currently runs, but is still in alpha and has none of the compatibility features I would like.  

# Update log:

* 10/20/2026: Renamed project to a better sounding name and important progress update announcement.

* 7/29/2026: Attempted to find settings that match the scale of the players body, the tracking points, and the players avatar. So far... very unsuccessful. 

* 7/8/2026: Reversed Mediapipe's outputted coordinates to accurately calibrate and track the user's body to their in game avatar. Removed broken code.

* 7/6/2026: Using X, Y, and Z tracking coordinates and arctan2 was able to dynamically solve for tracker rotation angles. Officially tested on my VR headset and although some minor scale and rotation bugs need to be repaired before it is useable, it reads, translates, and sends data, and VRChat receives it (almost) perfectly. 

* 7/3/2026: Added a local OSC client that speaks to VRChat's OSC server over port UDP/9000. Translates Mediapipe's coordinate data into something that VRChat can read as tracker position. Potential plans for a full-body tracking solution for desktop and even possibly mobile users.

* 7/2/2026: Added Google's ML model and Mediapipe to track the coordinates of 33 different points on the user's body. Currently prints the coordinates, with plans to instead feed them into a game's OSC/Driver. Also added better documentation inside of the code.

* 7/1/2026: This is my first real git contribution so I am just trying to get it out there with hopes of updating in the future.

