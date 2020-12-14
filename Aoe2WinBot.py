# Colton W
# 5/4/2020
# Auto clicking Program.
import time
import pyautogui
from screen_search import *

Civs = ["Azt.png", "Ber.png", "Bri.png", "Bul.png", "Bur.png", "Byz.png", "Cel.png", "Chi.png", "Cum.png", "Eth.png",
        "Fra.png", "Got.png", "Hun.png", "Inc.png", "Ind.png", "Ita.png", "Jap.png", "Khm.png", "Kor.png", "Lit.png",
        "Mag.png", "Mal.png", "May.png", "Mon.png", "Per.png", "Sar.png", "Sla.png", "Tat.png", "Spa.png",
        "Vik.png", "Mali.png", "Tur.png", "Vie.png", "Por.png"]
for Civ in Civs:

    # Below is the Code to select the start shield
    startshield = Search("Start.png")  # Sets shield image
    pos = startshield.imagesearch()
    pyautogui.click(x=pos[0], y=pos[1], clicks=1, interval=.1, button='left')

    time.sleep(3)

    # Clicks on the team to run
    pyautogui.click(x=860, y=393, clicks=1, interval=.1, button='left')  # Clicks the team select
    CurrentCiv = Search(Civ)
    pos2 = CurrentCiv.imagesearch()
    pyautogui.click(x=pos2[0], y=pos2[1], clicks=2, interval=.1, button='left')
    time.sleep(.5)

    # This code clicks the Start Game button
    StartGame = Search("game.png")
    pos3 = StartGame.imagesearch()
    pyautogui.click(x=pos3[0], y=pos3[1], clicks=2, interval=.1, button='left')
    time.sleep(11)

    # This code clicks play and then leave game 100 times. TO furfill 100 wins.
    for x in range(150):
        Leave = Search("leave.png")
        pos4 = Leave.imagesearch()
        if pos4[0] != -1:
            pyautogui.click(x=pos4[0], y=pos4[1], clicks=2, interval=.1, button='left')
            print("Clicking Leave")
            time.sleep(3)
        else:
            print("Couldnt find Leave button, Waiting a few seconds and trying again.")
            time.sleep(7)
            Leave = Search("leave.png")
            pos4 = Leave.imagesearch()
            pyautogui.click(x=pos4[0], y=pos4[1], clicks=2, interval=.1, button='left')
            print("Clicking Leave")
            time.sleep(3)

        Play = Search("play.png")
        pos5 = Play.imagesearch()
        pyautogui.click(x=pos5[0], y=pos5[1], clicks=2, interval=.1, button='left')
        print("Clicking Play")
        time.sleep(9)

    # Clicks the leave outside of loop
    Leave = Search("leave.png")
    pos4 = Leave.imagesearch()
    if pos4[0] != -1:
        pyautogui.click(x=pos4[0], y=pos4[1], clicks=2, interval=.1, button='left')
        print("Clicking Leave")
        time.sleep(3)
    else:
        print("Couldnt find Leave button, Waiting a few seconds and trying again.")
        time.sleep(6)
        Leave = Search("leave.png")
        pos4 = Leave.imagesearch()
        pyautogui.click(x=pos4[0], y=pos4[1], clicks=2, interval=.1, button='left')
        print("Clicking Leave")
        time.sleep(3)

    time.sleep(2)

    # Clicks the return to menu button
    Return = Search("Return.png")
    pos6 = Return.imagesearch()
    pyautogui.click(x=pos6[0], y=pos6[1], clicks=2, interval=.1, button='left')
    time.sleep(1)

    print("Finished with Civ:" + Civ)
    time.sleep(2)
