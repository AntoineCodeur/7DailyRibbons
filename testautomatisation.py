# -*- coding: utf-8 -*-
import time
import pyautogui
import pydirectinput
import pyperclip

WaitTime = 0.3
FilenameRead = None

def get_filename():
    with open('userdata.txt', 'r') as file:
        filename = file.read()
    return str(filename)

[FilenameRead, langage] = get_filename().split("\n")

def updown():
    time.sleep(3)
    for k in range(50):
        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')
        time.sleep(0.01)
        pydirectinput.keyDown('down')
        pydirectinput.keyUp('down')
        time.sleep(0.01)

def press(button):
    pydirectinput.keyDown(button)
    pydirectinput.keyUp(button)

def pressdouble(button1, button2):
    pydirectinput.keyDown(button1)
    pydirectinput.keyDown(button2)
    pydirectinput.keyUp(button1)
    pydirectinput.keyUp(button2)

def launch(FilenameRead, is_test=True):
    if is_test:
        time.sleep(3)
    else:
        time.sleep(1)
    filename = FilenameRead
    pyperclip.copy(filename)

    # Open the file
    pressdouble('ctrl', 'o')
    time.sleep(0.5)
    pressdouble('ctrl', 'v')
    time.sleep(0.5)
    press('enter')
    time.sleep(0.5)

    # Setup desmume in x4
    for _ in range(5):
        press('p')
    
    # Start the game 
    time.sleep(2)
    press('z')
    time.sleep(0.5)
    press('z') 
    time.sleep(1)   
    press('z')
    time.sleep(1)
    press('enter')
    time.sleep(1)

def get_ribbon_fr():
    pydirectinput.keyDown('x')
    time.sleep(WaitTime)

    for _ in range(4):
        press('z')
        time.sleep(WaitTime)

    for _ in range(3):
        press('z')
        time.sleep(WaitTime)
    time.sleep(WaitTime)
    press('down')
    time.sleep(WaitTime)

    for _ in range(2):
        press('z')
        time.sleep(WaitTime)
    pydirectinput.keyUp('x')
    pydirectinput.keyDown('x')
    time.sleep(WaitTime)
    press('down')
    time.sleep(WaitTime)

    for _ in range(2):
        press('z')
        time.sleep(WaitTime)
    press('up')
    for _ in range(3):
        press('z')
        time.sleep(WaitTime)
    press('down')
    time.sleep(WaitTime)
    for _ in range(2):
        press('z')
        time.sleep(WaitTime)

    for _ in range(8):
        press('x')
        time.sleep(WaitTime)




def get_ribbon_en():
    pydirectinput.keyDown('x')
    time.sleep(WaitTime)

    for _ in range(4):
        press('z')
        time.sleep(WaitTime)

    for _ in range(3):
        press('z')
        time.sleep(WaitTime)

    for _ in range(3):
        press('z')
        time.sleep(WaitTime)

    for _ in range(2):
        pydirectinput.keyUp('x')
        pydirectinput.keyDown('x')
        time.sleep(WaitTime)

    time.sleep(WaitTime)
    press('down')
    time.sleep(WaitTime)

    for _ in range(2):
        press('z')
        time.sleep(WaitTime)

    pydirectinput.keyUp('x')
    pydirectinput.keyDown('x')
    time.sleep(WaitTime)

    press('down')
    time.sleep(WaitTime)

    for _ in range(2):
        press('z')
        time.sleep(WaitTime)
    
    for _ in range(8):
        press('x')
        time.sleep(WaitTime)


def save():
    press('c')
    for _ in range(3):
        press('up')
    for _ in range(3):
        press('z')
        time.sleep(0.2)
    time.sleep(5)

def quit():
    pressdouble('alt', 'f4')

def ribbon(FilenameRead, langage, is_test=True):
    launch(FilenameRead, is_test)
    if langage=='FR':
        get_ribbon_fr()
    elif langage=='EN':
        get_ribbon_en()
    else:
        print("ERROR: LANGUAGE CAN ONLY BE 'EN' OR 'FR'")
    save()
    quit()

def changedate(first_time=False, is_test=True):
    time.sleep(2)
    if first_time:
        for _ in range(3):
            press('tab')
            time.sleep(0.05)
        press('right')

    else:
        for _ in range(9):
            press('tab')
            time.sleep(0.05)

    press('up')
    time.sleep(0.05)

    for _ in range(7):
        press('tab')
        time.sleep(0.05)
    press('enter')


# le keyboard interrupt marche pas, à revoir + revoir transition apres le premier run 
def run(print_time=False, langage=langage, FilenameRead=FilenameRead):
    if print_time:
        begin = time.time()
    print("Progress: -------")
    changedate(first_time=True, is_test=False)
    ribbon(FilenameRead, langage, is_test=False)
    print("          #------")
    for i in range(6):
        changedate()
        ribbon(FilenameRead, langage)
        StringProgress = "          " + '#' * (i + 2) + '-' * (5 - i)
        print(StringProgress)
    print("Run finished. ", end="")
    if print_time:
        end = time.time()
        runtime = end - begin
        print(f"It took {int(runtime // 60)} minutes and {int(runtime % 60)} seconds.")


    

# if __name__ == "__main__":
#     # run(print_time=True)
