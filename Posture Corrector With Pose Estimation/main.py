import tkinter as tk
from tkinter import ttk
import cv2
import mediapipe as mp
import numpy as np
import time
import array
import pygame
from datetime import datetime


pygame.mixer.init()

blink_Sound = pygame.mixer.Sound("interface-124464.wav")
wrong_posture = pygame.mixer.Sound("wrong-posture.wav")

arm_wrong = pygame.mixer.Sound("Arm_wrong.wav")
back_wrong = pygame.mixer.Sound("Back_wrong.wav")
leg_wrong = pygame.mixer.Sound("Leg_angle_wrong.wav")
body_arm_wrong = pygame.mixer.Sound("body_arm_wrong.wav")
upper_body_wrong = pygame.mixer.Sound("Upper_Body_wrong.wav")

numberOfExercise = 0

exercise_type = 1
numberOfSet = 0
numberOfTekrar = 0

exercises_str = ""

dosya_satir = 0

exercises = array.array('i',[])
set = array.array('i',[])
tekrar = array.array('i',[])
exerciseList = {1: 'Right Arm Dumbbell' ,2: 'Push Up' ,3: 'High Knee Twists',4:'Donkey Kicks',5:'Sit Up',6:'Squad'}

next_button = None
previous_button = None


global curretExercise
curretExercise = 1
global right_upper_body_angle
global right_upper_leg_angle
global left_upper_leg_angle
global left_arm_angle
global right_arm_angle
global left_leg_angle
global right_leg_angle
global right_body_arm_angle
global left_body_arm_angle
global left_back_angle
global right_back_angle
right_upper_body_angle = 0
right_upper_leg_angle = 0
left_upper_leg_angle = 0
left_arm_angle = 0
right_arm_angle = 0
left_leg_angle = 0
right_leg_angle = 0
right_body_arm_angle = 0
left_body_arm_angle = 0
left_back_angle = 0
right_back_angle = 0
right_lower_leg_angle = 0
currentSet = 1
currentTekrar = 0

state_label = None
current_Tekrar_label = None
current_Set = None


warning_label = None

gecmis_date_label = None
gecmis_dosex_label = None
gecmis_dosset_label = None
gecmis_dosrep_label = None

move_right_lower_leg_angle = None
move_right_knee_labely = None
move_left_elbow_labely = None
move_right_knee_label = None
move_left_elbow_label = None
move_left_knee_label = None
move_right_elbow_label = None
move_left_body_arm_angle_label = None
move_right_arm_angle_label = None
move_right_body_arm_angle_label = None
move_right_upper_body_angle_label = None
move_right_leg_angle_label = None
move_right_back_angle_label = None
move_left_leg_angle_label = None
move_left_upper_leg_label = None
move_right_upper_leg_label = None
move_right_arm_angle_label = None

move2_left_arm_angle_label = None
move2_left_knee_labely = None
move2_right_elbow_labely = None
move2_right_knee_label = None
move2_left_elbow_label = None
move2_left_knee_label = None
move2_right_elbow_label = None
move2_left_body_arm_angle_label = None
move2_right_arm_angle_label = None
move2_right_body_arm_angle_label = None
move2_right_upper_body_angle_label = None
move2_right_leg_angle_label = None
move2_right_back_angle_label = None
move2_left_leg_angle_label = None
move2_left_upper_leg_label = None
move2_right_upper_leg_label = None

stand_left_body_arm_angle_label = None
stand_right_arm_angle_label = None
stand_right_body_arm_angle_label = None
stand_right_upper_body_angle_label = None
stand_right_back_angle_label = None
stand_right_leg_angle_label = None
stand_left_leg_angle_label = None
stand_left_upper_leg_label = None
stand_right_upper_leg_label = None

def Right_Arm_Dumbbell():
    for widget in root.winfo_children():
        widget.destroy()
    global move_right_arm_angle_label
    global move_right_body_arm_angle_label
    global move_right_upper_body_angle_label

    global stand_right_arm_angle_label
    global stand_right_body_arm_angle_label
    global stand_right_upper_body_angle_label

    global current_Set
    global current_Tekrar_label
    global state_label


    root.geometry('600x600+900+240')


    stand_label = tk.Label(root, text="Put Camera on the Right Diagonal \n(Direction 2 o'clock)", font=("Arial", 20, "bold"), fg = "green")
    stand_label.place(x=60, y=5)


    current_Tekrar_label = tk.Label(root, text="Repeat: ",font=("Arial", 20, "bold"))
    current_Tekrar_label.place(x=20,y=100)
    current_Set = tk.Label(root, text="Set: ",font=("Arial", 20, "bold"))
    current_Set.place(x=230,y=100)
    state_label = tk.Label(root, text="State: ",font=("Arial", 20, "bold"))
    state_label.place(x=400, y=100)

    move_label = tk.Label(root, text="MOVE",font=("Arial", 24))
    move_label.place(x=70,y=150)

    stand_label = tk.Label(root, text="STAND",font=("Arial", 24))
    stand_label.place(x=340, y=150)


    #hareket
    move_right_arm_angle_label = tk.Label(root, text="Right Arm (<45): ",font=("Arial", 12))
    move_right_arm_angle_label.place(x=70,y=200)

    move_right_body_arm_angle_label = tk.Label(root,
                                          text="Right Body Arm (<30): ",font=("Arial", 12))
    move_right_body_arm_angle_label.place(x=70,y=225)

    move_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (>70): ",font=("Arial", 12))
    move_right_upper_body_angle_label.place(x=70,y=250)

    #duruş
    stand_right_arm_angle_label = tk.Label(root, text="Right Arm (>120): ",font=("Arial", 12))
    stand_right_arm_angle_label.place(x=340,y=200)

    stand_right_body_arm_angle_label = tk.Label(root,
                                          text="Right Body Arm (<30): ",font=("Arial", 12))
    stand_right_body_arm_angle_label.place(x=340,y=225)

    stand_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (>70): ",font=("Arial", 12))
    stand_right_upper_body_angle_label.place(x=340,y=250)

def Push_Up():
    for widget in root.winfo_children():
        widget.destroy()

    global move_right_leg_angle_label
    global move_right_arm_angle_label
    global move_right_upper_body_angle_label
    global move_right_back_angle_label

    global stand_right_leg_angle_label
    global stand_right_arm_angle_label
    global stand_right_upper_body_angle_label
    global stand_right_back_angle_label

    global current_Set
    global current_Tekrar_label
    global state_label

    root.geometry('600x600+900+240')

    stand_label = tk.Label(root, text="Put Camera on the Right Diagonal \n(Direction 2 o'clock)",
                           font=("Arial", 20, "bold"), fg="green")
    stand_label.place(x=60, y=5)

    current_Tekrar_label = tk.Label(root, text="Repeat: ", font=("Arial", 20, "bold"))
    current_Tekrar_label.place(x=20, y=100)
    current_Set = tk.Label(root, text="Set: ", font=("Arial", 20, "bold"))
    current_Set.place(x=230, y=100)
    state_label = tk.Label(root, text="State: ", font=("Arial", 20, "bold"))
    state_label.place(x=400, y=100)

    move_label = tk.Label(root, text="MOVE", font=("Arial", 24))
    move_label.place(x=70, y=150)

    stand_label = tk.Label(root, text="STAND", font=("Arial", 24))
    stand_label.place(x=340, y=150)

    #hareket
    move_right_arm_angle_label = tk.Label(root, text="Right Arm (<90): ",font=("Arial", 12))
    move_right_arm_angle_label.place(x=70,y=200)

    move_right_leg_angle_label = tk.Label(root, text="Right Leg (>150) : ",font=("Arial", 12))
    move_right_leg_angle_label.place(x=70,y=225)

    move_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (<40): ",font=("Arial", 12))
    move_right_upper_body_angle_label.place(x=70,y=250)

    move_right_back_angle_label = tk.Label(root, text="Right Back (>150): ".format(right_back_angle),font=("Arial", 12))
    move_right_back_angle_label.place(x=70,y=275)

    #duruş
    stand_right_arm_angle_label = tk.Label(root, text="Right Arm (>140): ",font=("Arial", 12))
    stand_right_arm_angle_label.place(x=340,y=200)

    stand_right_leg_angle_label = tk.Label(root, text="Right Leg (>150) : ",font=("Arial", 12))
    stand_right_leg_angle_label.place(x=340,y=225)

    stand_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (<40): ",font=("Arial", 12))
    stand_right_upper_body_angle_label.place(x=340,y=250)

    stand_right_back_angle_label = tk.Label(root, text="Right Back (>150): ".format(right_back_angle),font=("Arial", 12))
    stand_right_back_angle_label.place(x=340,y=275)

def High_Knee_Twists():
    for widget in root.winfo_children():
        widget.destroy()

    global move_right_knee_label
    global move_left_elbow_label
    global move_right_knee_labely
    global move_left_elbow_labely
    global move_left_body_arm_angle_label
    global move_right_leg_angle_label
    global move_right_body_arm_angle_label
    global move_left_leg_angle_label
    global move_right_arm_angle_label

    global move2_left_arm_angle_label
    global move2_left_knee_label
    global move2_right_elbow_label
    global move2_left_knee_labely
    global move2_right_elbow_labely
    global move2_left_body_arm_angle_label
    global move2_right_leg_angle_label
    global move2_right_body_arm_angle_label
    global move2_left_leg_angle_label

    global stand_left_body_arm_angle_label
    global stand_right_leg_angle_label
    global stand_right_body_arm_angle_label
    global stand_left_leg_angle_label

    global current_Set
    global current_Tekrar_label
    global state_label

    root.geometry('900x500+900+240')

    stand_label = tk.Label(root, text="Put Camera on the Right \n(Direction 3 o'clock)",
                           font=("Arial", 20, "bold"), fg="green")
    stand_label.place(x=250, y=5)

    current_Tekrar_label = tk.Label(root, text="Set: ", font=("Arial", 20, "bold"))
    current_Tekrar_label.place(x=120, y=100)
    current_Set = tk.Label(root, text="Repeat: ", font=("Arial", 20, "bold"))
    current_Set.place(x=320, y=100)
    state_label = tk.Label(root, text="State: ", font=("Arial", 20, "bold"))
    state_label.place(x=520, y=100)

    move_label = tk.Label(root, text="RIGHT LEG", font=("Arial", 24))
    move_label.place(x=70, y=150)

    stand_label = tk.Label(root, text="STAND", font=("Arial", 24))
    stand_label.place(x=340, y=150)

    move_label2 = tk.Label(root, text="LEFT LEG", font=("Arial", 24))
    move_label2.place(x=590, y=150)

    # right bacak
    move_right_knee_label = tk.Label(root, text="Right Knee x-axis ",font=("Arial", 12))
    move_right_knee_label.place(x=70, y=200)

    move_left_elbow_label = tk.Label(root, text="Left Elbow x-axis ",font=("Arial", 12))
    move_left_elbow_label.place(x=70, y=225)

    move_right_knee_labely = tk.Label(root, text="Right Knee y-axis ",font=("Arial", 12))
    move_right_knee_labely.place(x=70, y=250)

    move_left_elbow_labely = tk.Label(root, text="Left Elbow y-axis ",font=("Arial", 12))
    move_left_elbow_labely.place(x=70, y=275)

    move_left_body_arm_angle_label = tk.Label(root,
                                                 text="Left Body Arm (<70): ",font=("Arial", 12))
    move_left_body_arm_angle_label.place(x=70, y=300)

    move_right_body_arm_angle_label = tk.Label(root,
                                               text="Right Body Arm (>100): ",font=("Arial", 12))
    move_right_body_arm_angle_label.place(x=70, y=325)

    move_left_leg_angle_label = tk.Label(root, text="Left Leg (>150): ",font=("Arial", 12))
    move_left_leg_angle_label.place(x=70, y=350)

    move_right_leg_angle_label = tk.Label(root, text="Right Leg (<70): ",font=("Arial", 12))
    move_right_leg_angle_label.place(x=70, y=375)

    move_right_arm_angle_label = tk.Label(root, text="Right arm (<40): ",font=("Arial", 12))
    move_right_arm_angle_label.place(x=70, y=400)


    # left bacak
    move2_left_knee_label = tk.Label(root, text="Left Knee x-axis",font=("Arial", 12))
    move2_left_knee_label.place(x=590, y=200)

    move2_right_elbow_label = tk.Label(root, text="Right Elbow x-axis",font=("Arial", 12))
    move2_right_elbow_label.place(x=590, y=225)

    move2_left_knee_labely = tk.Label(root, text="Left Knee y-axis",font=("Arial", 12))
    move2_left_knee_labely.place(x=590, y=250)

    move2_right_elbow_labely = tk.Label(root, text="Right Elbow y-axis",font=("Arial", 12))
    move2_right_elbow_labely.place(x=590, y=275)

    move2_left_body_arm_angle_label = tk.Label(root,
                                              text="Left Body Arm (>100): ",font=("Arial", 12))
    move2_left_body_arm_angle_label.place(x=590, y=300)

    move2_right_body_arm_angle_label = tk.Label(root,
                                               text="Right Body Arm (<70): ",font=("Arial", 12))
    move2_right_body_arm_angle_label.place(x=590, y=325)

    move2_left_leg_angle_label = tk.Label(root, text="Left Leg (<70): ".format(right_back_angle),font=("Arial", 12))
    move2_left_leg_angle_label.place(x=590, y=350)

    move2_right_leg_angle_label = tk.Label(root, text="Right Leg (>150): ".format(right_back_angle),font=("Arial", 12))
    move2_right_leg_angle_label.place(x=590, y=375)

    move2_left_arm_angle_label = tk.Label(root, text="Left arm (<40): ", font=("Arial", 12))
    move2_left_arm_angle_label.place(x=590, y=400)

    # duruş
    stand_left_body_arm_angle_label = tk.Label(root,
                                               text="Left Body Arm (>100): ",font=("Arial", 12))
    stand_left_body_arm_angle_label.place(x=340, y=200)

    stand_right_body_arm_angle_label = tk.Label(root,
                                                text="Right Body Arm (>100): ",font=("Arial", 12))
    stand_right_body_arm_angle_label.place(x=340, y=225)

    stand_left_leg_angle_label = tk.Label(root, text="Left Leg (>150): ".format(right_back_angle),font=("Arial", 12))
    stand_left_leg_angle_label.place(x=340, y=250)

    stand_right_leg_angle_label = tk.Label(root, text="Right Leg (<40): ".format(right_back_angle),font=("Arial", 12))
    stand_right_leg_angle_label.place(x=340, y=275)

def Donkey_Kicks():

    for widget in root.winfo_children():
        widget.destroy()

    global move_right_body_arm_angle_label
    global move_right_leg_angle_label
    global move_right_arm_angle_label
    global move_right_upper_body_angle_label
    global move_right_back_angle_label
    global move_left_leg_angle_label
    global move_left_upper_leg_label
    global move_right_upper_leg_label
    global move_right_arm_angle_label

    global move2_right_body_arm_angle_label
    global move2_right_leg_angle_label
    global move2_right_arm_angle_label
    global move2_right_upper_body_angle_label
    global move2_right_back_angle_label
    global move2_left_leg_angle_label
    global move2_left_upper_leg_label
    global move2_right_upper_leg_label
    global move2_left_arm_angle_label

    global stand_right_body_arm_angle_label
    global stand_right_leg_angle_label
    global stand_right_arm_angle_label
    global stand_right_upper_body_angle_label
    global stand_right_back_angle_label
    global stand_left_leg_angle_label
    global stand_left_upper_leg_label
    global stand_right_upper_leg_label

    global current_Set
    global current_Tekrar_label
    global state_label

    root.geometry('850x600+900+240')

    stand_label = tk.Label(root, text="Put Camera on the Right \n(Direction 3 o'clock)",
                           font=("Arial", 20, "bold"), fg="green")
    stand_label.place(x=250, y=5)

    current_Tekrar_label = tk.Label(root, text="Set: ", font=("Arial", 20, "bold"))
    current_Tekrar_label.place(x=130, y=100)
    current_Set = tk.Label(root, text="Repeat: ", font=("Arial", 20, "bold"))
    current_Set.place(x=320, y=100)
    state_label = tk.Label(root, text="State: ", font=("Arial", 20, "bold"))
    state_label.place(x=520, y=100)

    move_label = tk.Label(root, text="LEFT LEG", font=("Arial", 24))
    move_label.place(x=70, y=150)

    stand_label = tk.Label(root, text="STAND", font=("Arial", 24))
    stand_label.place(x=340, y=150)

    move_label2 = tk.Label(root, text="RIGHT LEG", font=("Arial", 24))
    move_label2.place(x=590, y=150)


    #sol bacak
    move_right_arm_angle_label = tk.Label(root, text="Right Arm (>150): ",font=("Arial", 12))
    move_right_arm_angle_label.place(x=70, y=200)

    move_right_leg_angle_label = tk.Label(root, text="Right Leg (<110) : ",font=("Arial", 12))
    move_right_leg_angle_label.place(x=70, y=225)

    move_left_leg_angle_label = tk.Label(root, text="Left Leg (<110) : ".format(left_leg_angle),font=("Arial", 12))
    move_left_leg_angle_label.place(x=70, y=250)

    move_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (<40): ",font=("Arial", 12))
    move_right_upper_body_angle_label.place(x=70, y=275)

    move_right_body_arm_angle_label = tk.Label(root,
                                          text="Right Body Arm (60-120): ",font=("Arial", 12))
    move_right_body_arm_angle_label.place(x=70, y=300)

    move_right_back_angle_label = tk.Label(root, text="Right Back (>100): ".format(right_back_angle),font=("Arial", 12))
    move_right_back_angle_label.place(x=70, y=325)

    move_right_upper_leg_label = tk.Label(root,
                                     text="Right Upper Leg (>60): ".format(right_upper_leg_angle),font=("Arial", 12))
    move_right_upper_leg_label.place(x=70, y=350)

    move_left_upper_leg_label = tk.Label(root, text="Left Upper Leg (<20): ".format(left_upper_leg_angle),font=("Arial", 12))
    move_left_upper_leg_label.place(x=70, y=375)

    #sağ bacak
    move2_right_arm_angle_label = tk.Label(root, text="Right Arm (>150): ",font=("Arial", 12))
    move2_right_arm_angle_label.place(x=590, y=200)

    move2_right_leg_angle_label = tk.Label(root, text="Right Leg (<110) : ",font=("Arial", 12))
    move2_right_leg_angle_label.place(x=590, y=225)

    move2_left_leg_angle_label = tk.Label(root, text="Left Leg (<110) : ".format(left_leg_angle),font=("Arial", 12))
    move2_left_leg_angle_label.place(x=590, y=250)

    move2_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (<40): ",font=("Arial", 12))
    move2_right_upper_body_angle_label.place(x=590, y=275)

    move2_right_body_arm_angle_label = tk.Label(root,
                                          text="Right Body Arm (60-120): ",font=("Arial", 12))
    move2_right_body_arm_angle_label.place(x=590, y=300)

    move2_right_back_angle_label = tk.Label(root, text="Right Back (>100): ".format(right_back_angle),font=("Arial", 12))
    move2_right_back_angle_label.place(x=590, y=325)

    move2_right_upper_leg_label = tk.Label(root,
                                     text="Right Upper Leg (<20): ".format(right_upper_leg_angle),font=("Arial", 12))
    move2_right_upper_leg_label.place(x=590, y=350)

    move2_left_upper_leg_label = tk.Label(root, text="Left Upper Leg (>60): ".format(left_upper_leg_angle),font=("Arial", 12))
    move2_left_upper_leg_label.place(x=590, y=375)

    #duruş
    stand_right_arm_angle_label = tk.Label(root, text="Right Arm (>150): ",font=("Arial", 12))
    stand_right_arm_angle_label.place(x=340, y=200)

    stand_right_leg_angle_label = tk.Label(root, text="Right Leg (<110) : ",font=("Arial", 12))
    stand_right_leg_angle_label.place(x=340, y=225)

    stand_left_leg_angle_label = tk.Label(root, text="Left Leg (<110) : ".format(left_leg_angle),font=("Arial", 12))
    stand_left_leg_angle_label.place(x=340, y=250)

    stand_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (<40): ",font=("Arial", 12))
    stand_right_upper_body_angle_label.place(x=340, y=275)

    stand_right_body_arm_angle_label = tk.Label(root,
                                          text="Right Body Arm (60-120): ",font=("Arial", 12))
    stand_right_body_arm_angle_label.place(x=340, y=300)

    stand_right_back_angle_label = tk.Label(root, text="Right Back (>100): ".format(right_back_angle),font=("Arial", 12))
    stand_right_back_angle_label.place(x=340, y=325)

    stand_right_upper_leg_label = tk.Label(root,
                                     text="Right Upper Leg (>60): ".format(right_upper_leg_angle),font=("Arial", 12))
    stand_right_upper_leg_label.place(x=340, y=350)

    stand_left_upper_leg_label = tk.Label(root, text="Left Upper Leg (>60): ".format(left_upper_leg_angle),font=("Arial", 12))
    stand_left_upper_leg_label.place(x=340, y=375)

def Sit_Up():

    for widget in root.winfo_children():
        widget.destroy()

    global move_right_leg_angle_label
    global move_right_upper_body_angle_label
    global move_right_back_angle_label

    global stand_right_leg_angle_label
    global stand_right_upper_body_angle_label
    global stand_right_back_angle_label

    global current_Set
    global current_Tekrar_label
    global state_label

    root.geometry('600x600+900+240')

    stand_label = tk.Label(root, text="Put Camera on the Right \n(Direction 3 o'clock)",
                           font=("Arial", 20, "bold"), fg="green")
    stand_label.place(x=60, y=5)

    current_Tekrar_label = tk.Label(root, text="Repeat: ", font=("Arial", 20, "bold"))
    current_Tekrar_label.place(x=20, y=100)
    current_Set = tk.Label(root, text="Set: ", font=("Arial", 20, "bold"))
    current_Set.place(x=230, y=100)
    state_label = tk.Label(root, text="State: ", font=("Arial", 20, "bold"))
    state_label.place(x=400, y=100)

    move_label = tk.Label(root, text="MOVE", font=("Arial", 24))
    move_label.place(x=70, y=150)

    stand_label = tk.Label(root, text="STAND", font=("Arial", 24))
    stand_label.place(x=340, y=150)


    move_right_leg_angle_label = tk.Label(root, text="Right Leg (<60): ",font=("Arial", 12))
    move_right_leg_angle_label.place(x=70,y=200)

    move_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (>60): ",font=("Arial", 12))
    move_right_upper_body_angle_label.place(x=70,y=225)

    move_right_back_angle_label = tk.Label(root, text="Right Back (<60): ",font=("Arial", 12))
    move_right_back_angle_label.place(x=70,y=250)


    stand_right_leg_angle_label = tk.Label(root, text="Right Leg (<60) : ",font=("Arial", 12))
    stand_right_leg_angle_label.place(x=340,y=200)

    stand_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (<15): ",font=("Arial", 12))
    stand_right_upper_body_angle_label.place(x=340,y=225)

    stand_right_back_angle_label = tk.Label(root, text="Right Back (>100): ",font=("Arial", 12))
    stand_right_back_angle_label.place(x=340,y=250)

def Squad():

    for widget in root.winfo_children():
        widget.destroy()

    global move_right_body_arm_angle_label
    global move_right_leg_angle_label
    global move_right_arm_angle_label
    global move_right_upper_body_angle_label
    global move_right_lower_leg_angle

    global stand_right_leg_angle_label
    global stand_right_arm_angle_label
    global stand_right_upper_body_angle_label

    global current_Set
    global current_Tekrar_label
    global state_label

    root.geometry('600x600+900+240')

    stand_label = tk.Label(root, text="Put Camera on the Right Diagonal \n(Direction 2 o'clock)",
                           font=("Arial", 20, "bold"), fg="green")
    stand_label.place(x=60, y=5)

    current_Tekrar_label = tk.Label(root, text="Repeat: ", font=("Arial", 20, "bold"))
    current_Tekrar_label.place(x=20, y=100)
    current_Set = tk.Label(root, text="Set: ", font=("Arial", 20, "bold"))
    current_Set.place(x=230, y=100)
    state_label = tk.Label(root, text="State: ", font=("Arial", 20, "bold"))
    state_label.place(x=400, y=100)

    move_label = tk.Label(root, text="MOVE", font=("Arial", 24))
    move_label.place(x=70, y=150)

    stand_label = tk.Label(root, text="STAND", font=("Arial", 24))
    stand_label.place(x=340, y=150)


    move_right_arm_angle_label = tk.Label(root, text="Right Arm (<45): ",font=("Arial", 12))
    move_right_arm_angle_label.place(x=70,y=200)

    move_right_leg_angle_label = tk.Label(root, text="Right Leg (<90) : ",font=("Arial", 12))
    move_right_leg_angle_label.place(x=70,y=225)

    move_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (>60): ",font=("Arial", 12))
    move_right_upper_body_angle_label.place(x=70,y=250)

    move_right_body_arm_angle_label = tk.Label(root,
                                    text="Right Body Arm (<=45): ",font=("Arial", 12))
    move_right_body_arm_angle_label.place(x=70,y=275)





    stand_right_arm_angle_label = tk.Label(root, text="Right Arm (>120): ",font=("Arial", 12))
    stand_right_arm_angle_label.place(x=350,y=200)

    stand_right_leg_angle_label = tk.Label(root, text="Right Leg (>140) : ",font=("Arial", 12))
    stand_right_leg_angle_label.place(x=350,y=225)

    stand_right_upper_body_angle_label = tk.Label(root,
                                            text="Right Upper Body (>70): ",font=("Arial", 12))
    stand_right_upper_body_angle_label.place(x=350,y=250)

def open_camera():
    global move_right_knee_label
    global move_left_elbow_label
    global move_left_body_arm_angle_label
    global move_right_body_arm_angle_label
    global move_right_leg_angle_label
    global move_right_arm_angle_label
    global move_right_upper_body_angle_label
    global move_right_back_angle_label
    global move_left_leg_angle_label
    global move_left_upper_leg_label
    global move_right_upper_leg_label
    global move_right_lower_leg_angle

    global move2_left_knee_label
    global move2_right_elbow_label
    global move2_left_body_arm_angle_label
    global move2_right_body_arm_angle_label
    global move2_right_leg_angle_label
    global move2_right_arm_angle_label
    global move2_right_upper_body_angle_label
    global move2_right_back_angle_label
    global move2_left_leg_angle_label
    global move2_left_upper_leg_label
    global move2_right_upper_leg_label

    global stand_left_body_arm_angle_label
    global stand_right_body_arm_angle_label
    global stand_right_leg_angle_label
    global stand_right_arm_angle_label
    global stand_right_upper_body_angle_label
    global stand_right_back_angle_label
    global stand_left_leg_angle_label
    global stand_left_upper_leg_label
    global stand_right_upper_leg_label

    global numberOfExercise
    global current_Set
    global current_Tekrar_label
    global state_label
    global exercises_str
    global dosya_dizi
    global dosya_satir
    global date
    global dosya
    if len(exercises_str) < 5:
        warning_label.config(text="Warning: You did not add any exercises.",fg="red")
        return
    dosya_satir=0
    date = date +"*"+ exercises_str

    dosya_dizi.append(date)

    with open(dosya, "r") as dosya_ici:
        satirlar = dosya_ici.readlines()
        for satir in satirlar:
            dosya_dizi.append(satir.strip())
            dosya_satir = dosya_satir + 1
            if dosya_satir == 9:
                pass


    with open(dosya, "w") as dosya_ici:
        for eleman in dosya_dizi:
            dosya_ici.write(eleman + "\n")


    color_changer = 'black'

    count = 0
    curretExercise = 1
    #deneme_label.config(text="Counter: {}")  # 1 saniye (1000 ms) sonra güncelleme işlemini tekrarla

    hareketBaslangic = 0
    currentSet = 1

    currentTekrar = 0
    starting_time = time.time()
    voice_replay = 0

    exercises.append(0)
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    cap = cv2.VideoCapture(0)

    # Gif dosyasının yüklenmesi
    gif_path = "C:\\Users\\emirh\\OneDrive\\Masaüstü\\Posture Corrector With Pose Estimation\\Wow-gif.gif"
    gif = cv2.VideoCapture(gif_path)
    # Gif'in fps değeri
    gif_fps = int(gif.get(cv2.CAP_PROP_FPS))
    gifBelirleme = 0

    start_time = time.time()  # Başlangıç zamanını kaydet
    counter = 0


    def calculate_angle(a, b, c):
        a = np.array(a)  # First
        b = np.array(b)  # Mid
        c = np.array(c)  # End

        radians = np.arctan2(480 * (c[1] - b[1]), 640 * (c[0] - b[0])) - np.arctan2(480 * (a[1] - b[1]),
                                                                                    640 * (a[0] - b[0]))
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle


    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while True:



            if int(hareketBaslangic) == 0 and exerciseList[exercises[curretExercise - 1]] == 'Right Arm Dumbbell':
                gif_path = "C:\\Users\\emirh\\OneDrive\\Masaüstü\\Posture Corrector With Pose Estimation\\bicep-curls.gif"
                gif = cv2.VideoCapture(gif_path)
                # Gif'in fps değeri
                gif_fps = int(gif.get(cv2.CAP_PROP_FPS))
                hareketBaslangic = hareketBaslangic + 1
                gifx = 490
                gifscale = 0.2
                Right_Arm_Dumbbell()

            elif int(hareketBaslangic) == 0 and exerciseList[exercises[curretExercise - 1]] == 'Push Up':
                gif_path = "C:\\Users\\emirh\\OneDrive\\Masaüstü\\Posture Corrector With Pose Estimation\\Push-Up.gif"
                gif = cv2.VideoCapture(gif_path)
                # Gif'in fps değeri
                gif_fps = int(gif.get(cv2.CAP_PROP_FPS))
                hareketBaslangic = hareketBaslangic + 1
                gifx = 470
                gifscale = 0.4
                Push_Up()

            elif int(hareketBaslangic) == 0 and exerciseList[exercises[curretExercise - 1]] == 'High Knee Twists':
                gif_path = "C:\\Users\\emirh\\OneDrive\\Masaüstü\\Posture Corrector With Pose Estimation\\high-knee.gif"
                gif = cv2.VideoCapture(gif_path)
                # Gif'in fps değeri
                gif_fps = int(gif.get(cv2.CAP_PROP_FPS))
                hareketBaslangic = hareketBaslangic + 1
                gifx = 510
                gifscale = 0.3
                High_Knee_Twists()

            elif int(hareketBaslangic) == 0 and exerciseList[exercises[curretExercise - 1]] == 'Donkey Kicks':
                gif_path = "C:\\Users\\emirh\\OneDrive\\Masaüstü\\Posture Corrector With Pose Estimation\\donkey-kick.gif"
                gif = cv2.VideoCapture(gif_path)
                # Gif'in fps değeri
                gif_fps = int(gif.get(cv2.CAP_PROP_FPS))
                hareketBaslangic = hareketBaslangic + 1
                gifx = 440
                gifscale = 0.3
                Donkey_Kicks()

            elif int(hareketBaslangic) == 0 and exerciseList[exercises[curretExercise - 1]] == 'Sit Up':
                gif_path = "C:\\Users\\emirh\\OneDrive\\Masaüstü\\Posture Corrector With Pose Estimation\\Sit-Up.gif"
                gif = cv2.VideoCapture(gif_path)
                # Gif'in fps değeri
                gif_fps = int(gif.get(cv2.CAP_PROP_FPS))
                hareketBaslangic = hareketBaslangic + 1
                gifx = 490
                gifscale = 0.3
                Sit_Up()

            elif int(hareketBaslangic) == 0 and exerciseList[exercises[curretExercise - 1]] == 'Squad':
                gif_path = "C:\\Users\\emirh\\OneDrive\\Masaüstü\\Posture Corrector With Pose Estimation\\squad.gif"
                gif = cv2.VideoCapture(gif_path)
                # Gif'in fps değeri
                gif_fps = int(gif.get(cv2.CAP_PROP_FPS))
                hareketBaslangic = hareketBaslangic + 1
                gifx = 495
                gifscale = 0.3
                Squad()

            ret, frame = cap.read()
            current_time = time.time() - starting_time
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates

                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]

                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]

                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

                left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

                right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]



                vertical_shoulder_angle = 180 * np.arctan2((480 * abs(left_shoulder[1] - right_shoulder[1])),
                                                           (640 * abs(left_shoulder[0] - right_shoulder[0]))) / np.pi
                right_upper_body_angle = 180 * np.arctan2((480 * abs(right_shoulder[1] - right_hip[1])),
                                                          (640 * abs(right_shoulder[0] - right_hip[0]))) / np.pi
                right_upper_leg_angle = 180 * np.arctan2((480 * abs(right_knee[1] - right_hip[1])),
                                                         (640 * abs(right_knee[0] - right_hip[0]))) / np.pi
                left_upper_leg_angle = 180 * np.arctan2((480 * abs(left_knee[1] - left_hip[1])),
                                                        (640 * abs(left_knee[0] - left_hip[0]))) / np.pi

                right_lower_leg_angle = 180 * np.arctan2((480 * abs(right_knee[1] - right_ankle[1])),
                                                        (640 * abs(right_knee[0] - right_ankle[0]))) / np.pi

                left_arm_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
                right_arm_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)

                left_leg_angle = calculate_angle(left_hip, left_knee, left_ankle)
                right_leg_angle = calculate_angle(right_hip, right_knee, right_ankle)

                right_body_arm_angle = calculate_angle(right_hip, right_shoulder, right_elbow)
                left_body_arm_angle = calculate_angle(left_hip, left_shoulder, left_elbow)

                left_back_angle = calculate_angle(left_shoulder, left_hip, left_knee)
                right_back_angle = calculate_angle(right_shoulder, right_hip, right_knee)

                if exerciseList[exercises[curretExercise - 1]] == 'Right Arm Dumbbell':

                    state = "MOVE" if count == 0 else "STATE"

                    # hareket
                    if count == 0:
                        state = "MOVE"

                        color_changer = 'green' if int(right_arm_angle) < 45 else 'red'
                        move_right_arm_angle_label.config(text="Right Arm (<45): " + str(int(right_arm_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if int(right_body_arm_angle) < 30 else 'red'
                        move_right_body_arm_angle_label.config(
                            text="Right Body Arm (<30): " + str(int(right_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_upper_body_angle) > 70 else 'red'
                        move_right_upper_body_angle_label.config(
                            text="Right Upper Body (>70): " + str(int(right_upper_body_angle)), fg=color_changer)

                    # duruş
                    if count == 1:
                        state = "STAND"

                        color_changer = 'green' if int(right_arm_angle) > 120 else 'red'
                        stand_right_arm_angle_label.config(text="Right Arm (>120): " + str(int(right_arm_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if int(right_body_arm_angle) < 30 else 'red'
                        stand_right_body_arm_angle_label.config(
                            text="Right Body Arm (<30): " + str(int(right_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_upper_body_angle) > 70 else 'red'
                        stand_right_upper_body_angle_label.config(
                            text="Right Upper Body (>70): " + str(int(right_upper_body_angle)), fg=color_changer)

                    current_Set.config(text="Set: " + str(currentSet) + " / " + str(set[curretExercise - 1]))
                    current_Tekrar_label.config(
                        text="Repeat: " + str(currentTekrar) + " / " + str(tekrar[curretExercise - 1]))
                    state_label.config(text="State: " + str(state))

                    root.update()
                    if int(right_body_arm_angle) > 30 or int(right_upper_body_angle) < 70:
                        if int(right_upper_body_angle) < 70:
                            image = cv2.line(image,
                                             (int(640 * float(right_shoulder[0])), int(480 * float(right_shoulder[1]))),
                                             (int(640 * float(right_hip[0])), int(480 * float(right_hip[1]))),
                                             (242, 237, 11), 7)
                        if int(right_body_arm_angle) > 30:
                            image = cv2.line(image,
                                             (int(640 * float(right_shoulder[0])), int(480 * float(right_shoulder[1]))),
                                             (int(640 * float(right_elbow[0])), int(480 * float(right_elbow[1]))),
                                             (242, 237, 11), 7)

                        image = cv2.line(image,
                                         (int(640 * float(right_shoulder[0])), int(480 * float(right_shoulder[1]))),
                                         (int(640 * float(right_hip[0])), int(480 * float(right_hip[1]))),
                                         (242, 237, 11), 7)

                        if int(right_upper_body_angle) < 70 and int(current_time) % 5 == 0 and voice_replay == 0:
                            upper_body_wrong.play()
                            voice_replay = 1
                        elif int(right_body_arm_angle) > 30 and int(current_time) % 5 == 0 and voice_replay == 0:
                            body_arm_wrong.play()
                            voice_replay = 1

                    if int(right_body_arm_angle) < 30 and int(current_time) % 5 == 3:
                        voice_replay = 0

                    if count == 0 and int(right_arm_angle) < 45 and int(right_body_arm_angle) < 30 and int(
                            right_upper_body_angle) > 70:
                        blink_Sound.play()
                        count = 1
                        currentTekrar = currentTekrar + 1

                    if int(right_arm_angle) > 120 and int(right_upper_body_angle) > 70 and int(
                            right_body_arm_angle) <= 30 and count == 1:
                        count = 0

                if exerciseList[exercises[curretExercise - 1]] == 'Push Up':

                    # hareket
                    if count == 0:
                        state = "MOVE"

                        color_changer = 'green' if int(right_arm_angle) < 90 else 'red'
                        move_right_arm_angle_label.config(text="Right Arm (<90): " + str(int(right_arm_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if int(right_leg_angle) > 150 else 'red'
                        move_right_leg_angle_label.config(text="Right Leg (>150) : " + str(int(right_leg_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if int(right_upper_body_angle) < 40 else 'red'
                        move_right_upper_body_angle_label.config(
                            text="Right Upper Body (<40): " + str(int(right_upper_body_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_back_angle) > 150 else 'red'
                        move_right_back_angle_label.config(text="Right Back (>150): " + str(int(right_back_angle)),
                                                           fg=color_changer)
                    # duruş
                    if count == 1:
                        state = "STAND"
                        color_changer = 'green' if int(right_arm_angle) > 140 else 'red'
                        stand_right_arm_angle_label.config(text="Right Arm (>140): " + str(int(right_arm_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if int(right_leg_angle) > 150 else 'red'
                        stand_right_leg_angle_label.config(text="Right Leg (>150) : " + str(int(right_leg_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if int(right_upper_body_angle) < 40 else 'red'
                        stand_right_upper_body_angle_label.config(
                            text="Right Upper Body (<40): " + str(int(right_upper_body_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_back_angle) > 150 else 'red'
                        stand_right_back_angle_label.config(text="Right Back (>150): " + str(int(right_back_angle)),
                                                            fg=color_changer)

                    current_Set.config(text="Set: " + str(currentSet) + " / " + str(set[curretExercise - 1]))
                    current_Tekrar_label.config(
                        text="Repeat: " + str(currentTekrar) + " / " + str(tekrar[curretExercise - 1]))
                    state_label.config(text="State: " + str(state))

                    root.update()
                    if int(right_leg_angle) < 150 or int(right_back_angle) < 150:
                        if int(right_back_angle) < 150:
                            image = cv2.line(image, (int(640 * float(right_hip[0])), int(480 * float(right_hip[1]))),
                                             (int(640 * float(right_shoulder[0])), int(480 * float(right_shoulder[1]))),
                                             (242, 237, 11), 7)
                            image = cv2.line(image, (int(640 * float(right_hip[0])), int(480 * float(right_hip[1]))),
                                             (int(640 * float(right_knee[0])), int(480 * float(right_knee[1]))),
                                             (242, 237, 11), 7)

                        if int(right_leg_angle) < 150:
                            image = cv2.line(image, (int(640 * float(right_knee[0])), int(480 * float(right_knee[1]))),
                                             (int(640 * float(right_ankle[0])), int(480 * float(right_ankle[1]))),
                                             (242, 237, 11), 7)
                            image = cv2.line(image, (int(640 * float(right_hip[0])), int(480 * float(right_hip[1]))),
                                             (int(640 * float(right_knee[0])), int(480 * float(right_knee[1]))),
                                             (242, 237, 11), 7)

                        if int(right_leg_angle) < 150 and int(current_time) % 5 == 0 and voice_replay == 0:
                            leg_wrong.play()
                            voice_replay = 1
                        elif int(right_back_angle) < 150 and int(current_time) % 5 == 0 and voice_replay == 0:
                            back_wrong.play()
                            voice_replay = 1

                    if int(right_upper_body_angle) < 40 and int(right_arm_angle) > 75 and int(
                            right_arm_angle) < 105 and int(current_time) % 5 == 3:
                        voice_replay = 0

                    if int(right_arm_angle) < 90 and int(right_leg_angle) > 150 and int(right_back_angle) > 150 and int(
                            right_upper_body_angle) < 40 and count == 0:
                        blink_Sound.play()
                        count = 1
                        currentTekrar = currentTekrar + 1

                    if int(right_arm_angle) > 140 and int(right_leg_angle) > 150 and int(
                            right_back_angle) > 150 and int(right_upper_body_angle) < 40 and count == 1:
                        count = 0

                if exerciseList[exercises[curretExercise - 1]] == 'High Knee Twists':

                    # right bacak
                    if count == 0:
                        state = "RIGHT LEG"
                        color_changer = 'green' if right_knee[0] < left_shoulder[0] and right_knee[0] > right_shoulder[
                            0] else 'red'
                        move_right_knee_label.config(text="Right Knee x-axis (" + str(int(1000 * right_shoulder[0])) +
                                                          "-" + str(int(1000 * left_shoulder[0])) + ") :" + str(
                            int(1000 * right_knee[0])), fg=color_changer)

                        color_changer = 'green' if left_elbow[0] < left_shoulder[0] and left_elbow[0] > right_shoulder[
                            0] else 'red'
                        move_left_elbow_label.config(text="Left Elbow x-axis (" + str(int(1000 * right_shoulder[0])) +
                                                          "-" + str(int(1000 * left_shoulder[0])) + ") :" + str(
                            int(1000 * left_elbow[0])), fg=color_changer)

                        color_changer = 'green' if right_knee[1] > left_shoulder[1] and right_knee[1] < left_hip[
                            1] else 'red'
                        move_right_knee_labely.config(text="Right Knee y-axis (" + str(int(1000 * left_shoulder[1])) +
                                                           "-" + str(int(1000 * left_hip[1])) + ") :" + str(
                            int(1000 * right_knee[1])), fg=color_changer)

                        color_changer = 'green' if left_elbow[1] > left_shoulder[1] and left_elbow[1] < left_hip[
                            1] else 'red'
                        move_left_elbow_labely.config(text="Left Elbow y-axis (" + str(int(1000 * left_shoulder[1])) +
                                                           "-" + str(int(1000 * left_hip[1])) + ") :" + str(
                            int(1000 * left_elbow[1])), fg=color_changer)

                        color_changer = 'green' if left_body_arm_angle < 70 else 'red'
                        move_left_body_arm_angle_label.config(
                            text="Left Body Arm (<70): " + str(int(left_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if right_body_arm_angle < 70 else 'red'
                        move_right_body_arm_angle_label.config(
                            text="Right Body Arm (<70): " + str(int(right_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if left_leg_angle > 150 else 'red'
                        move_left_leg_angle_label.config(text="Left Leg (>150): " + str(int(left_leg_angle)),
                                                         fg=color_changer)

                        color_changer = 'green' if right_leg_angle < 70 else 'red'
                        move_right_leg_angle_label.config(text="Right Leg (<70): " + str(int(right_leg_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if right_arm_angle < 40 else 'red'
                        move_right_arm_angle_label.config(text="Right Arm (<40): " + str(int(right_arm_angle)),
                                                          fg=color_changer)

                    # left bacak
                    elif count == 2:
                        state = "LEFT LEG"

                        color_changer = 'green' if left_knee[0] < left_shoulder[0] and left_knee[0] > right_shoulder[
                            0] else 'red'
                        move2_left_knee_label.config(text="Left Knee x-axis (" + str(int(1000 * right_shoulder[0])) +
                                                          "-" + str(int(1000 * left_shoulder[0])) + ") :" + str(
                            int(1000 * left_knee[0])), fg=color_changer)

                        color_changer = 'green' if right_elbow[0] < left_shoulder[0] and right_elbow[0] > \
                                                   right_shoulder[0] else 'red'
                        move2_right_elbow_label.config(
                            text="Right Elbow x-axis (" + str(int(1000 * right_shoulder[0])) +
                                 "-" + str(int(1000 * left_shoulder[0])) + ") :" + str(
                                int(1000 * right_elbow[0])), fg=color_changer)

                        color_changer = 'green' if left_knee[1] > left_shoulder[1] and left_knee[1] < left_hip[
                            1] else 'red'
                        move2_left_knee_labely.config(text="Left Knee y-axis (" + str(int(1000 * left_shoulder[1])) +
                                                           "-" + str(int(1000 * left_hip[1])) + ") :" + str(
                            int(1000 * left_knee[1])), fg=color_changer)

                        color_changer = 'green' if right_elbow[1] > left_shoulder[1] and right_elbow[1] < left_hip[
                            1] else 'red'
                        move2_right_elbow_labely.config(
                            text="Right Elbow y-axis (" + str(int(1000 * left_shoulder[1])) +
                                 "-" + str(int(1000 * left_hip[1])) + ") :" + str(
                                int(1000 * right_elbow[1])), fg=color_changer)

                        color_changer = 'green' if left_body_arm_angle < 70 else 'red'
                        move2_left_body_arm_angle_label.config(
                            text="Left Body Arm (<70): " + str(int(left_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if right_body_arm_angle < 70 else 'red'
                        move2_right_body_arm_angle_label.config(
                            text="Right Body Arm (<70): " + str(int(right_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if left_leg_angle < 70 else 'red'
                        move2_left_leg_angle_label.config(text="Left Leg (<70): " + str(int(left_leg_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if right_leg_angle > 150 else 'red'
                        move2_right_leg_angle_label.config(text="Right Leg (>150): " + str(int(right_leg_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if left_arm_angle < 40 else 'red'
                        move2_left_arm_angle_label.config(text="Left Arm (<40): " + str(int(left_arm_angle)),
                                                          fg=color_changer)

                    # duruş
                    else:
                        state = "STAND"
                        color_changer = 'green' if left_body_arm_angle > 100 else 'red'
                        stand_left_body_arm_angle_label.config(
                            text="Left Body Arm (>100): " + str(int(left_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if right_body_arm_angle > 100 else 'red'
                        stand_right_body_arm_angle_label.config(
                            text="Right Body Arm (>100): " + str(int(right_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if left_leg_angle > 150 else 'red'
                        stand_left_leg_angle_label.config(text="Left Leg (>150): " + str(int(left_leg_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if right_leg_angle > 150 else 'red'
                        stand_right_leg_angle_label.config(text="Right Leg (>150): " + str(int(right_leg_angle)),
                                                           fg=color_changer)

                    current_Set.config(text="Set: " + str(currentSet) + " / " + str(set[curretExercise - 1]))
                    current_Tekrar_label.config(
                        text="Repeat: " + str(currentTekrar) + " / " + str(tekrar[curretExercise - 1]))
                    state_label.config(text="State: " + str(state))

                    root.update()

                    if (left_elbow[0] < left_shoulder[0]
                            and left_elbow[0] > right_shoulder[0]
                            and left_elbow[1] > left_shoulder[1]
                            and left_elbow[1] < left_hip[1]

                            and right_knee[0] < left_shoulder[0]
                            and right_knee[0] > right_shoulder[0]
                            and right_knee[1] > left_shoulder[1]
                            and right_knee[1] < left_hip[1]

                            and int(left_leg_angle) > 150
                            and int(right_leg_angle) < 70
                            and int(right_body_arm_angle) < 70
                            and int(left_body_arm_angle) < 70
                            and int(right_arm_angle) < 40

                            and count == 0):
                        blink_Sound.play()
                        count = 1
                        currentTekrar = currentTekrar + 1

                    if (right_elbow[0] < left_shoulder[0]
                            and right_elbow[0] > right_shoulder[0]
                            and right_elbow[1] > left_shoulder[1]
                            and right_elbow[1] < left_hip[1]

                            and left_knee[0] < left_shoulder[0]
                            and left_knee[0] > right_shoulder[0]
                            and left_knee[1] > left_shoulder[1]
                            and left_knee[1] < left_hip[1]

                            and int(left_leg_angle) < 70
                            and int(right_leg_angle) > 150
                            and int(right_body_arm_angle) < 70
                            and int(left_body_arm_angle) < 70
                            and int(left_arm_angle) < 40

                            and count == 2):
                        blink_Sound.play()
                        count = 3
                        currentTekrar = currentTekrar + 1

                    if int(left_leg_angle) > 150 and int(right_leg_angle) > 150 and int(
                            right_body_arm_angle) > 100 and int(left_body_arm_angle) > 100 and count == 3:
                        count = 0

                    if int(left_leg_angle) > 150 and int(right_leg_angle) > 150 and int(
                            right_body_arm_angle) > 100 and int(left_body_arm_angle) > 100 and count == 1:
                        count = 2

                if exerciseList[exercises[curretExercise - 1]] == 'Donkey Kicks':

                    if count == 0:
                        state = "LEFT LEG"

                        color_changer = 'green' if int(right_arm_angle) > 150 else 'red'
                        move_right_arm_angle_label.config(text="Right Arm (>150): " + str(int(right_arm_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if int(right_leg_angle) < 110 else 'red'
                        move_right_leg_angle_label.config(text="Right Leg (<110) : " + str(int(right_leg_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if int(left_leg_angle) < 110 else 'red'
                        move_left_leg_angle_label.config(text="Left Leg (<110) : " + str(int(left_leg_angle)),
                                                         fg=color_changer)

                        color_changer = 'green' if int(right_upper_body_angle) < 40 else 'red'
                        move_right_upper_body_angle_label.config(text="Right Upper Body (<40): " + str(int(
                            right_upper_body_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_body_arm_angle) < 120 and int(
                            right_body_arm_angle) > 60 else 'red'
                        move_right_body_arm_angle_label.config(text="Right Body Arm (60-120): " + str(int(
                            right_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_back_angle) > 100 else 'red'
                        move_right_back_angle_label.config(text="Right Back (>100): " + str(int(right_back_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if int(right_upper_leg_angle) > 60 else 'red'
                        move_right_upper_leg_label.config(
                            text="Right Upper Leg (>60): " + str(int(right_upper_leg_angle)), fg=color_changer)

                        color_changer = 'green' if int(left_upper_leg_angle) < 20 else 'red'
                        move_left_upper_leg_label.config(text="Left Upper Leg (<20): " + str(int(left_upper_leg_angle)),
                                                         fg=color_changer)
                    # sağ bacak
                    elif count == 2:
                        state = "RIGHT LEG"

                        color_changer = 'green' if int(right_arm_angle) > 150 else 'red'
                        move2_right_arm_angle_label.config(text="Right Arm (>150): " + str(int(right_arm_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if int(right_leg_angle) < 110 else 'red'
                        move2_right_leg_angle_label.config(text="Right Leg (<110) : " + str(int(right_leg_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if int(left_leg_angle) < 110 else 'red'
                        move2_left_leg_angle_label.config(text="Left Leg (<110) : " + str(int(left_leg_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if int(right_upper_body_angle) < 40 else 'red'
                        move2_right_upper_body_angle_label.config(text="Right Upper Body (<40): " + str(int(
                            right_upper_body_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_body_arm_angle) > 60 and int(
                            right_body_arm_angle) < 120 else 'red'
                        move2_right_body_arm_angle_label.config(text="Right Body Arm (60-120): " + str(int(
                            right_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_back_angle) > 100 else 'red'
                        move2_right_back_angle_label.config(text="Right Back (>100): " + str(int(right_back_angle)),
                                                            fg=color_changer)

                        color_changer = 'green' if int(right_upper_leg_angle) < 20 else 'red'
                        move2_right_upper_leg_label.config(
                            text="Right Upper Leg (<20): " + str(int(right_upper_leg_angle)), fg=color_changer)

                        color_changer = 'green' if int(left_upper_leg_angle) > 60 else 'red'
                        move2_left_upper_leg_label.config(
                            text="Left Upper Leg (>60): " + str(int(left_upper_leg_angle)), fg=color_changer)

                    # duruş
                    else:
                        state = "STAND"

                        color_changer = 'green' if right_arm_angle > 150 else 'red'
                        stand_right_arm_angle_label.config(text="Right Arm (>150): " + str(int(right_arm_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if right_leg_angle < 110 else 'red'
                        stand_right_leg_angle_label.config(text="Right Leg (<110) : " + str(int(right_leg_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if left_leg_angle < 110 else 'red'
                        stand_left_leg_angle_label.config(text="Left Leg (<110) : " + str(int(left_leg_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if right_upper_body_angle < 40 else 'red'
                        stand_right_upper_body_angle_label.config(text="Right Upper Body (<40): " + str(int(
                            right_upper_body_angle)), fg=color_changer)

                        color_changer = 'green' if right_body_arm_angle > 60 and right_body_arm_angle < 120 else 'red'
                        stand_right_body_arm_angle_label.config(text="Right Body Arm (60-120): " + str(int(
                            right_body_arm_angle)), fg=color_changer)

                        color_changer = 'green' if right_back_angle > 100 else 'red'
                        stand_right_back_angle_label.config(text="Right Back (>100): " + str(int(right_back_angle)),
                                                            fg=color_changer)

                        color_changer = 'green' if right_upper_leg_angle > 60 else 'red'
                        stand_right_upper_leg_label.config(
                            text="Right Upper Leg (>60): " + str(int(right_upper_leg_angle)), fg=color_changer)

                        color_changer = 'green' if left_upper_leg_angle > 60 else 'red'
                        stand_left_upper_leg_label.config(
                            text="Left Upper Leg (>60): " + str(int(left_upper_leg_angle)), fg=color_changer)

                    current_Set.config(text="Set: " + str(currentSet) + " / " + str(set[curretExercise - 1]))
                    current_Tekrar_label.config(
                        text="Repeat: " + str(currentTekrar) + " / " + str(tekrar[curretExercise - 1]))
                    state_label.config(text="State: " + str(state))

                    root.update()

                    if int(right_upper_body_angle) > 40 or int(right_arm_angle) < 150:
                        if int(right_arm_angle) < 150:
                            image = cv2.line(image,
                                             (int(640 * float(right_elbow[0])), int(480 * float(right_elbow[1]))),
                                             (int(640 * float(right_shoulder[0])), int(480 * float(right_shoulder[1]))),
                                             (242, 237, 11), 7)
                            image = cv2.line(image,
                                             (int(640 * float(right_wrist[0])), int(480 * float(right_wrist[1]))),
                                             (int(640 * float(right_elbow[0])), int(480 * float(right_elbow[1]))),
                                             (242, 237, 11), 7)

                        if int(right_upper_body_angle) > 40:
                            image = cv2.line(image, (int(640 * float(right_hip[0])), int(480 * float(right_hip[1]))),
                                             (int(640 * float(right_shoulder[0])), int(480 * float(right_shoulder[1]))),
                                             (242, 237, 11), 7)

                        if int(right_arm_angle) < 150 and int(current_time) % 5 == 0 and voice_replay == 0:
                            arm_wrong.play()
                            voice_replay = 1
                        elif int(right_upper_body_angle) > 40 and int(current_time) % 5 == 0 and voice_replay == 0:
                            upper_body_wrong.play()
                            voice_replay = 1

                    if int(right_upper_body_angle) < 40 and int(right_arm_angle) > 150 and int(current_time) % 5 == 3:
                        voice_replay = 0

                    if count == 0 and int(right_arm_angle) > 150 and int(right_upper_body_angle) < 40 and int(
                            left_leg_angle) < 110 and int(right_leg_angle) < 110 and int(
                        right_body_arm_angle) > 60 and int(right_body_arm_angle) < 120 and int(
                        left_upper_leg_angle) < 20 and int(right_upper_leg_angle) > 60 and int(right_back_angle) > 100:
                        blink_Sound.play()
                        count = 1
                        currentTekrar = currentTekrar + 1

                    if count == 2 and int(right_arm_angle) > 150 and int(right_upper_body_angle) < 40 and int(
                            left_leg_angle) < 110 and int(right_leg_angle) < 110 and int(
                        right_body_arm_angle) > 60 and int(right_body_arm_angle) < 120 and int(
                        right_upper_leg_angle) < 20 and int(left_upper_leg_angle) > 60 and int(right_back_angle) > 100:
                        blink_Sound.play()
                        count = 3
                        currentTekrar = currentTekrar + 1

                    if int(right_arm_angle) > 150 and int(right_upper_body_angle) < 40 and int(
                            left_leg_angle) < 110 and int(right_leg_angle) < 110 and count == 1 and int(
                        right_body_arm_angle) > 60 and int(
                        right_body_arm_angle) < 120 and int(left_upper_leg_angle) > 60 and int(
                        right_upper_leg_angle) > 60 and int(right_back_angle) > 100:
                        count = 2

                    if int(right_arm_angle) > 150 and int(right_upper_body_angle) < 40 and int(
                            left_leg_angle) < 110 and int(right_leg_angle) < 110 and count == 3 and int(
                        right_body_arm_angle) > 60 and int(
                        right_body_arm_angle) < 120 and int(left_upper_leg_angle) > 60 and int(
                        right_upper_leg_angle) > 60 and int(right_back_angle) > 100:
                        count = 0

                if exerciseList[exercises[curretExercise - 1]] == 'Sit Up':

                    if count == 0:
                        state = "MOVE"

                        color_changer = 'green' if int(right_leg_angle) < 60 else 'red'
                        move_right_leg_angle_label.config(text="Right Leg (<60): " + str(int(right_arm_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if int(right_upper_body_angle) > 60 else 'red'
                        move_right_upper_body_angle_label.config(
                            text="Right Upper Body (>60): " + str(int(right_upper_body_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_back_angle) < 60 else 'red'
                        move_right_back_angle_label.config(text="Right Back (<60): " + str(int(right_back_angle)),
                                                           fg=color_changer)

                    if count == 1:
                        state = "STAND"

                        color_changer = 'green' if int(right_leg_angle) < 60 else 'red'
                        stand_right_leg_angle_label.config(text="Right Leg (<60) : " + str(int(right_leg_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if int(right_upper_body_angle) < 15 else 'red'
                        stand_right_upper_body_angle_label.config(
                            text="Right Upper Body (<15): " + str(int(right_upper_body_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_back_angle) > 100 else 'red'
                        stand_right_back_angle_label.config(text="Right Back (>100): " + str(int(right_back_angle)),
                                                            fg=color_changer)

                    current_Set.config(text="Set: " + str(currentSet) + " / " + str(set[curretExercise - 1]))
                    current_Tekrar_label.config(
                        text="Repeat: " + str(currentTekrar) + " / " + str(tekrar[curretExercise - 1]))
                    state_label.config(text="State: " + str(state))

                    root.update()

                    if int(right_leg_angle) > 60:

                        image = cv2.line(image, (int(640 * float(right_knee[0])), int(480 * float(right_knee[1]))),
                                         (int(640 * float(right_hip[0])), int(480 * float(right_hip[1]))),
                                         (242, 237, 11), 7)
                        image = cv2.line(image, (int(640 * float(right_knee[0])), int(480 * float(right_knee[1]))),
                                         (int(640 * float(right_ankle[0])), int(480 * float(right_ankle[1]))),
                                         (242, 237, 11), 7)

                        if int(right_leg_angle) > 60 and int(current_time) % 5 == 0 and voice_replay == 0:
                            leg_wrong.play()
                            voice_replay = 1

                    if int(right_leg_angle) < 60 and int(current_time) % 5 == 3:
                        voice_replay = 0

                    if int(right_leg_angle) < 60 and int(right_back_angle) < 60 and int(
                            right_upper_body_angle) > 60 and count == 0:
                        blink_Sound.play()
                        count = 1
                        currentTekrar = currentTekrar + 1

                    if int(right_leg_angle) < 60 and int(right_back_angle) > 100 and int(
                            right_upper_body_angle) < 15 and count == 1:
                        count = 0

                if exerciseList[exercises[curretExercise - 1]] == 'Squad':

                    state = "MOVE" if count == 0 else "STAND"
                    if count == 0:
                        color_changer = 'green' if int(right_arm_angle) < 45 else 'red'
                        move_right_arm_angle_label.config(text="Right Arm (<45): " + str(int(right_arm_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if int(right_leg_angle) < 90 else 'red'
                        move_right_leg_angle_label.config(text="Right Leg (<90) : " + str(int(right_leg_angle)),
                                                          fg=color_changer)

                        color_changer = 'green' if int(right_upper_body_angle) > 60 else 'red'
                        move_right_upper_body_angle_label.config(text="Right Upper Body (>60): " + str(int(
                            right_upper_body_angle)), fg=color_changer)

                        color_changer = 'green' if int(right_body_arm_angle) <= 45 else 'red'
                        move_right_body_arm_angle_label.config(
                            text="Right Body Arm (<=45): " + str(int(right_body_arm_angle)), fg=color_changer)

                    if count == 1:
                        color_changer = 'green' if int(right_arm_angle) > 120 else 'red'
                        stand_right_arm_angle_label.config(text="Right Arm (>120): " + str(int(right_arm_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if int(right_leg_angle) > 140 else 'red'
                        stand_right_leg_angle_label.config(text="Right Leg (>140) : " + str(int(right_leg_angle)),
                                                           fg=color_changer)

                        color_changer = 'green' if int(right_upper_body_angle) > 60 else 'red'
                        stand_right_upper_body_angle_label.config(text="Right Upper Body (>60): " + str(int(
                            right_upper_body_angle)), fg=color_changer)

                    current_Set.config(text="Set: " + str(currentSet) + " / " + str(set[curretExercise - 1]))
                    current_Tekrar_label.config(
                        text="Repeat: " + str(currentTekrar) + " / " + str(tekrar[curretExercise - 1]))
                    state_label.config(text="State: " + str(state))

                    root.update()

                    if int(right_upper_body_angle) < 60:
                        image = cv2.line(image,
                                         (int(640 * float(right_shoulder[0])), int(480 * float(right_shoulder[1]))),
                                         (int(640 * float(right_hip[0])), int(480 * float(right_hip[1]))),
                                         (242, 237, 11), 7)
                        if int(current_time) % 5 == 0 and voice_replay == 0:
                            upper_body_wrong.play()
                            voice_replay = 1

                    if int(right_upper_body_angle) > 60 and int(current_time) % 5 == 3:
                        voice_replay = 0

                    if count == 0 and int(right_leg_angle) < 90 and int(right_arm_angle) < 45 and int(
                            right_body_arm_angle) <= 45 and int(right_upper_body_angle) > 60:
                        blink_Sound.play()
                        count = 1
                        currentTekrar = currentTekrar + 1

                    if int(right_arm_angle) > 120 and count == 1 and int(right_upper_body_angle) > 60 and int(
                            right_leg_angle) > 140:
                        count = 0

                if curretExercise == numberOfExercise and int(set[curretExercise - 1]) == int(currentSet) and int(
                        tekrar[curretExercise - 1]) == int(
                    currentTekrar):
                    for widget in root.winfo_children():
                        widget.destroy()
                    root.geometry('400x300+900+240')
                    end_label = tk.Label(root, text="Exercise Ended",
                                         font=("Arial", 24, "bold"))
                    end_label.place(x=75, y=100)
                    root.update()
                    break

                if int(set[curretExercise - 1]) == int(currentSet) and int(tekrar[curretExercise - 1]) == int(
                        currentTekrar):
                    hareketBaslangic = 0
                    currentTekrar = 0
                    currentSet = 1
                    curretExercise = curretExercise + 1
                    count = 0

                elif int(tekrar[curretExercise - 1]) == int(currentTekrar):
                    currentSet = currentSet + 1
                    currentTekrar = 0

            except:
                pass

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                      )

            # Gif dosyasından bir kare okunması
            ret, gif_frame = gif.read()

            if not ret:
                gif.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            # Gif karesinin boyutlarının alınması
            gif_height, gif_width, _ = gif_frame.shape

            # Gif'in boyutlarının kamera görüntüsü boyutlarına göre ayarlanması
            scale_factor = float(gifscale)
            gif_width = int(gif_width * scale_factor)
            gif_height = int(gif_height * scale_factor)
            gif_frame = cv2.resize(gif_frame, (gif_width, gif_height))

            # Gif'in alpha kanalının ayarlanması
            if gif_frame.shape[2] == 4:
                alpha_s = gif_frame[:, :, 3] / 255.0
                alpha_s = 1 - alpha_s  # alpha değerlerini tersine çevir
            else:
                alpha_s = np.ones_like(gif_frame[:, :, 0])

            # Gif'in konumunun ayarlanması
            y1, y2 = 0, 0 + gif_frame.shape[0]
            x1, x2 = int(gifx), int(gifx) + gif_frame.shape[1]

            # Gif'in alpha kanalının ayarlanması
            if gif_frame.shape[2] == 4:
                alpha_s = gif_frame[:, :, 2] / 255.0
                alpha_s = 1 - alpha_s  # alpha değerlerini tersine çevir
            else:
                alpha_s = np.ones_like(gif_frame[:, :, 0])

            # Görüntüye opaklık uygula
            for c in range(0, 3):
                image[y1:y2, x1:x2, c] = (alpha_s * gif_frame[:, :, c] + (1 - alpha_s) * image[y1:y2, x1:x2, c])

            gif_frame = cv2.cvtColor(gif_frame, cv2.COLOR_BGR2LAB)
            gif_frame[:, :, 0] = cv2.equalizeHist(gif_frame[:, :, 0])
            gif_frame = cv2.cvtColor(gif_frame, cv2.COLOR_LAB2BGR)

            # Gif'in kamera görüntüsüne eklenmesi
            frame_roi = image[y1:y2, x1:x2]
            gif_roi = gif_frame[:, :, :3]

            if frame_roi.shape == gif_roi.shape:
                image[y1:y2, x1:x2] = cv2.add(frame_roi, gif_roi)
            else:
                gif_roi_resized = cv2.resize(gif_roi, (frame_roi.shape[1], frame_roi.shape[0]))
                image[y1:y2, x1:x2] = cv2.add(frame_roi, gif_roi_resized)

            # update_counter()
            cv2.imshow("Camera", image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()
    gif.release()

def right_arm_dumbbell_add():
    global numberOfExercise
    global  exercises_str
    global warning_label
    if len(set_entry.get()) == 0 or len(tekrar_entry.get()) == 0:
        warning_label.config(text="Warning: Please enter Set and Repeat.", fg="red")
        return
    numberOfExercise = numberOfExercise + 1
    warning_label.config(text="", fg="red")
    exercises.append(1)
    set.append(int(set_entry.get()))
    tekrar.append(int(tekrar_entry.get()))
    exercises_str = ""

    set_entry.delete(0, tk.END)
    tekrar_entry.delete(0, tk.END)

    for i in range(len(exercises)):
        exercises_str = str(exercises_str) + str(exerciseList[exercises[i]]) +"("+str(set[i]) + "-" + str(tekrar[i]) +"), "
    execises_label.config(text="Exercises\n "+ str(exercises_str.replace(",","\n")))
    root.update()

def push_up_add():
    global numberOfExercise
    global exercises_str
    global warning_label
    if len(set_entry.get()) == 0 or len(tekrar_entry.get())== 0:
        warning_label.config(text="Warning: Please enter Set and Repeat.", fg="red")
        return
    numberOfExercise = numberOfExercise + 1
    warning_label.config(text="", fg="red")
    exercises.append(2)
    set.append(int(set_entry.get()))
    tekrar.append(int(tekrar_entry.get()))

    set_entry.delete(0, tk.END)
    tekrar_entry.delete(0, tk.END)

    exercises_str = ""
    for i in range(len(exercises)):
        exercises_str = str(exercises_str) + str(exerciseList[exercises[i]]) +"("+str(set[i]) + "-" + str(tekrar[i]) +"), "
    execises_label.config(text="Exercises\n"+ str(exercises_str.replace(",","\n")))
    root.update()

def high_knee_add():
    global numberOfExercise
    global exercises_str
    global warning_label

    if len(set_entry.get()) == 0 or len(tekrar_entry.get())== 0:
        warning_label.config(text="Warning: Please enter Set and Repeat.", fg="red")
        return

    numberOfExercise = numberOfExercise + 1
    warning_label.config(text="", fg="red")
    exercises.append(3)
    set.append(int(set_entry.get()))
    tekrar.append(int(tekrar_entry.get()))

    set_entry.delete(0, tk.END)
    tekrar_entry.delete(0, tk.END)

    exercises_str = ""
    for i in range(len(exercises)):
        exercises_str = str(exercises_str) + str(exerciseList[exercises[i]]) +"("+str(set[i]) + "-" + str(tekrar[i]) +"), "
    execises_label.config(text="Exercises\n"+ str(exercises_str.replace(",","\n")))
    root.update()

def donkey_add():
    global numberOfExercise
    global exercises_str


    global warning_label
    if len(set_entry.get()) == 0 or len(tekrar_entry.get())== 0:
        warning_label.config(text="Warning: Please enter Set and Repeat.", fg="red")
        return

    numberOfExercise = numberOfExercise + 1
    warning_label.config(text="", fg="red")
    exercises.append(4)
    set.append(int(set_entry.get()))
    tekrar.append(int(tekrar_entry.get()))

    set_entry.delete(0, tk.END)
    tekrar_entry.delete(0, tk.END)

    exercises_str = ""
    for i in range(len(exercises)):
        exercises_str = str(exercises_str) + str(exerciseList[exercises[i]]) +"("+str(set[i]) + "-" + str(tekrar[i]) +"), "
    execises_label.config(text="Exercises\n" + str(exercises_str.replace(",","\n")))
    root.update()

def sit_up_add():
    global numberOfExercise
    global exercises_str

    global warning_label
    if len(set_entry.get()) == 0 or len(tekrar_entry.get())== 0:
        warning_label.config(text="Warning: Please enter Set and Repeat.", fg="red")
        return

    numberOfExercise = numberOfExercise + 1
    warning_label.config(text="", fg="red")
    exercises.append(5)
    set.append(int(set_entry.get()))
    tekrar.append(int(tekrar_entry.get()))

    set_entry.delete(0, tk.END)
    tekrar_entry.delete(0, tk.END)

    exercises_str = ""
    for i in range(len(exercises)):
        exercises_str = str(exercises_str) + str(exerciseList[exercises[i]]) +"("+str(set[i]) + "-" + str(tekrar[i]) +"), "
    execises_label.config(text="Exercises\n" + str(exercises_str.replace(",","\n")))
    root.update()

def squad_add():
    global numberOfExercise
    global exercises_str

    global warning_label
    if len(set_entry.get()) == 0 or len(tekrar_entry.get())== 0:
        warning_label.config(text="Warning: Please enter Set and Repeat.", fg="red")
        return

    numberOfExercise = numberOfExercise + 1
    warning_label.config(text="", fg="red")
    exercises.append(6)
    set.append(int(set_entry.get()))
    tekrar.append(int(tekrar_entry.get()))

    set_entry.delete(0, tk.END)
    tekrar_entry.delete(0, tk.END)

    exercises_str = ""
    for i in range(len(exercises)):
        exercises_str = str(exercises_str) + str(exerciseList[exercises[i]]) +"("+str(set[i]) + "-" + str(tekrar[i]) +"), "
    execises_label.config(text="Exercises\n"+ str(exercises_str.replace(",","\n")))
    root.update()

def import_set():
    set.append(set_entry.get())
    set_label.config(text="Counter: {}".format(set))
    root.update()

def import_tekrar():
    tekrar.append(tekrar_entry.get())
    Tekrar_label.config(text="Counter: {}".format(tekrar))
    root.update()

def gecmis():
    global next_button
    global previous_button
    global dosya_satir

    global gecmis_date_label
    global gecmis_dosex_label
    global gecmis_dosset_label
    global gecmis_dosrep_label
    global dosya_saat
    global dosya_tarih
    global dosya_set
    global dosya_tekrar
    global dosya_exercises
    global dosya_count
    dosya_count = 1

    def previous_gecmis():

        global next_button
        global previous_button
        global gecmis_date_label
        global gecmis_dosex_label
        global gecmis_dosset_label
        global gecmis_dosrep_label
        global dosya_count
        global dosya_satir
        dosya_count = dosya_count - 1
        if int(dosya_count)==1:
            previous_button.destroy()

        if int(dosya_count) == int(dosya_satir-1):
            next_button = ttk.Button(gecmis_pencere, text="Next", command=next_gecmis)
            next_button.place(x=300, y=20)


        gecmis_date_label.config(text=str(dosya_saat[dosya_count - 1])+ "  " + str(dosya_tarih[dosya_count - 1]))
        gecmis_dosex_label.config(text=dosya_exercises[dosya_count - 1])
        gecmis_dosset_label.config(text=dosya_set[dosya_count - 1])
        gecmis_dosrep_label.config(text=dosya_tekrar[dosya_count - 1])
        gecmis_pencere.update()

    def next_gecmis():

        global previous_button
        global next_button
        global gecmis_date_label
        global gecmis_dosex_label
        global gecmis_dosset_label
        global gecmis_dosrep_label
        global dosya_count
        global dosya_satir
        dosya_count = dosya_count + 1

        if int(dosya_count) == 2:
            previous_button = ttk.Button(gecmis_pencere, text="Perivous", command=previous_gecmis)
            previous_button.place(x=50, y=20)

        if int(dosya_count) == int(dosya_satir):
            next_button.destroy()

        gecmis_date_label.config(text=str(dosya_saat[dosya_count - 1])+ "  " + str(dosya_tarih[dosya_count - 1]))
        gecmis_dosex_label.config(text=dosya_exercises[dosya_count - 1])
        gecmis_dosset_label.config(text=dosya_set[dosya_count - 1])
        gecmis_dosrep_label.config(text=dosya_tekrar[dosya_count - 1])
        gecmis_pencere.update()


    gecmis_pencere = tk.Tk()
    gecmis_pencere.geometry('400x450+900+240')
    gecmis_pencere.title("History")

    gecmis_date_label = tk.Label(gecmis_pencere, text= dosya_saat[dosya_count - 1] + "  "+dosya_tarih[dosya_count - 1])
    gecmis_date_label.place(x=150,y=50)

    gecmis_execises_label = tk.Label(gecmis_pencere, text="Exercises",font=("Arial", 12, "bold"))
    gecmis_execises_label.place(x=45,y=80)

    gecmis_set_label = tk.Label(gecmis_pencere, text="Set",font=("Arial", 12, "bold"))
    gecmis_set_label.place(x=200, y=80)

    gecmis_tekrar_label = tk.Label(gecmis_pencere, text="Repeat",font=("Arial", 12, "bold"))
    gecmis_tekrar_label.place(x=280, y=80)

    gecmis_dosex_label = tk.Label(gecmis_pencere, text= dosya_exercises[dosya_count - 1])
    gecmis_dosex_label.place(x=25,y=110)

    gecmis_dosset_label = tk.Label(gecmis_pencere, text=dosya_set[dosya_count - 1])
    gecmis_dosset_label.place(x=205, y=110)

    gecmis_dosrep_label = tk.Label(gecmis_pencere, text=dosya_tekrar[dosya_count - 1])
    gecmis_dosrep_label.place(x=285, y=110)

    next_button = ttk.Button(gecmis_pencere, text="Next", command=next_gecmis)
    next_button.place(x=300, y=20)

    gecmis_pencere.mainloop()

root = tk.Tk()
root.geometry('580x400+900+240')
root.resizable(False,True)
root.title('sporty')
logo_yolu = "logo.ico"
root.iconbitmap(logo_yolu)

dosya_dizi = []
now = datetime.now()
tarih = now.strftime("%d/%m/%Y")
zaman = now.strftime("%H:%M:%S")
date = str(tarih) + "*"+ str(zaman)

dosya = "deneme.txt"
dosya_saat_str = ""
dosya_tarih_str = ""
dosya_saat = []
dosya_tarih = []
dosya_set = []
dosya_set_str = ""
dosya_tekrar = []
dosya_tekrar_str=""
dosya_exercises = []
dosya_exercises_str = ""
dosya_kelime = ""
dosya_count = 0

with open(dosya, "r") as dosya_ici:
    satirlar = dosya_ici.readlines()
    for satir in satirlar:
        satir = satir.strip()
        dosya_count = 0
        for harf in satir:
            if harf != "*" and harf != "(" and  harf != ")" and harf != "-" and harf != ",":
                if dosya_count == 2 and harf == "/":
                    pass
                else:
                    dosya_kelime = dosya_kelime + harf

            if harf == "*" and dosya_count == 0:
                dosya_count = 1
                dosya_tarih_str = dosya_kelime
                dosya_kelime = ""

            elif harf == "*" and dosya_count == 1:
                dosya_saat_str = dosya_kelime
                dosya_kelime = ""
                dosya_count = 2
            elif harf == "(":
                dosya_exercises_str = dosya_exercises_str + dosya_kelime + "-"
                dosya_kelime = ""
            elif harf == "-" and dosya_count == 2:
                dosya_set_str = dosya_set_str + dosya_kelime + "-"
                dosya_kelime = ""
            elif harf == ")":
                dosya_tekrar_str = dosya_tekrar_str + dosya_kelime + "-"
                dosya_kelime = ""

        dosya_exercises_str = dosya_exercises_str.replace("-","\n\n")
        dosya_tekrar_str =dosya_tekrar_str.replace("-","\n\n")
        dosya_set_str = dosya_set_str.replace("-","\n\n")
        dosya_exercises.append(dosya_exercises_str)
        dosya_tekrar.append(dosya_tekrar_str)
        dosya_set.append(dosya_set_str)
        dosya_tarih.append(dosya_tarih_str)
        dosya_saat.append(dosya_saat_str)
        dosya_tarih_str = ""
        dosya_saat_str = ""
        dosya_exercises_str = ""
        dosya_tekrar_str = ""
        dosya_set_str = ""


with open(dosya, "r") as dosya_ici:
    dosya_satir = sum(1 for _ in dosya_ici)


style = ttk.Style()
style.theme_use('clam')

right_arm_dumbbell_button = ttk.Button(root, text="Add Right Arm Dumbbell", command=right_arm_dumbbell_add, width=23)
right_arm_dumbbell_button.place(x=50,y=20)

push_up_button = ttk.Button(root, text="Add Push Up", command=push_up_add, width=23)
push_up_button.place(x=215,y=20)

high_knee_button = ttk.Button(root, text="Add High Knee Twists", command=high_knee_add, width=23)
high_knee_button.place(x=380,y=20)

donkey_button = ttk.Button(root, text="Add Donkey Kiks", command=donkey_add, width=23)
donkey_button.place(x=50,y=70)

sit_up_button = ttk.Button(root, text="Add Sit Up", command=sit_up_add, width=23)
sit_up_button.place(x=215,y=70)

squad_add_button = ttk.Button(root, text="Add Squad", command=squad_add, width=23)
squad_add_button.place(x=380,y=70)

camera_button = ttk.Button(root, text="Start Exercising", command=open_camera, width=23)
camera_button.place(x=215,y=160)

hata_button = ttk.Button(root, text="History", command=gecmis)
hata_button.place(x=50, y=245)

warning_label = tk.Label(root, text="",font=("Arial", 10, "bold"))
warning_label.place(x=160,y=200)

set_label = tk.Label(root, text="Set: ")
set_label.place(x=130,y=120)

Tekrar_label = tk.Label(root, text="Repeat: ")
Tekrar_label.place(x=280,y=120)

execises_label = tk.Label(root, text="Exercises ")
execises_label.place(x=245,y=250)

set_entry=ttk.Entry(root, width=15)
set_entry.place(x=160,y=120)

tekrar_entry=ttk.Entry(root, width=15)
tekrar_entry.place(x=330,y=120)


root.mainloop()