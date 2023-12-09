# Overview
This small script will help you farming the 7 daily ribbons on multiple pokemons without spending a ton of time doing it yourself. <br />
It uses direct inputs with a python script, so you can run it while you're doing something else, but you can't use your pc meanwhile. <br />
One run (7 ribbons) takes between 4 and 5 minutes.


# Softwares requirements
-Python (i can only guarantee it works in 3.11.6) <br />
-Python modules: time, pydirectinput, pyautogui, pyperclip <br />
-run_as_date <br />
-Desmume <br />
-An english or french rom of Platinum with your save in front of the ribbon girl (Note : didn't test with diamond and pearl but it should work, HGSS and other languages don't work but could work with updates) <br />

# Setup 
-Download the repository and extract it wherever you want <br />
-Open desmume, use ctrl + O to go to the folder of your rom, copy the text of its whole name (with the .nds at the end), open it <br />
-Save your game in front of the blonde girl who gives ribbons with the pokemon you want ribbons with in first position in your team (he must have 0 of these ribbons at the start) <br />
-Close desmume <br />
-Fill the userdata.txt document as follow: <br />
 &emsp; • In the first line : the name of your rom: paste what you copied just before <br />
 &emsp; • In the second line : the language of your rom: write 'EN' for an english rom, 'FR' for a french rom. Do not add spaces or line breaks <br />
 &emsp; • Save it and close it <br />


# How to use
-Launch run_as_date. It must be set to launch your desmume application and the next 7 days need to be from the same month (ex. if it's the 30 august, set it to 1 september). Make the changes if necessary, close it and rerun it <br />
-Run the file named 'exe.py'. You have 2 seconds to click back on run_as_date after that <br />
-That's it, the program will launch your game itself and proceed to get the 7 ribbons <br />



