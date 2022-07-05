# Chess-Player
This Python Program takes chess steps as input and plays chess from both sides following those steps. The inputed steps needs to follow the chess notation rules.

Currently, this program only works on [Lichess](https://lichess.org/) and that also at specific settings due to limitations of OpenCV and Pyautogui

# Disclaimer
I DO NOT promote any kind of cheating in any way. This project is completely for learning experience and is not meant to be misused for cheating on any online chess platforms.

# Technologies Used
### Programming Language
Python

### Python Modules
1. Pyautogui

2. OpenCV-Python

3. Numpy

# How to run it
1. Install Python 3
2. Install required python modules by entering below command in Terminal
```bash
pip install pyautogui opencv-python numpy
```
3. Create a new Workspace and open [Lichess](https://lichess.org/) on 2 different windows
4. Select the option to Play with Friend on Lichess and create a match and join the match from another window (as it is the only way you can control both sides of game)
5. The player with white pieces to play should set piece theme 'cburnett' on Lichess and the player with black pieces to play should set the piece theme to 'chess7' 
6. Your screen should look something like this

![image](https://user-images.githubusercontent.com/77500668/177385215-15024d4b-60c0-40a3-9c6a-d93d98f6d1e9.png)

7. Now, Take screenshot of your whole screen

  1. Crop the whole chess board of white player and save the image in graphics folder as "white_board.png". Your image should look something like this
  
      ![image](https://user-images.githubusercontent.com/77500668/177385908-3a3c3da6-8b5c-4f56-8615-657165449f1f.png)
  
  2. Do the same for black player chess board and save the image in graphics folder as "black_board.png". Your image should look like this
  
      ![image](https://user-images.githubusercontent.com/77500668/177390226-3c2a7db0-80af-4118-aeab-2252eb3b9175.png)

  
8. Finally, we are ready to run the program. Now, enter the chess steps (following chess notations) in "input.txt"

   Example Input:
   ```
   1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. d4 d5 6. Bd3 Bd6 7. 0-0 0-0 8. c4 c6 9. Re1 Bf5 10. Qb3 Qd7 11. Nc3 Nxc3 12. Bxf5 Qxf5 13. bxc3 b6 14. cxd5 cxd5 15. Qb5 Qd7 16. a4 Qxb5 17. axb5 a5 18. Nh4 (diagram) g6 19. g4 Nd7 20. Ng2 Rfc8 21. Bf4 Bxf4 22. Nxf4 Rxc3 23. Nxd5 Rd3 24. Re7 Nf8 25. Nf6+ Kg7 26. Ne8+ Kg8 27. d5 a4 28. Nf6+ Kg7 29. g5 a3 30. Ne8+ Kg8 31. Nf6+ Kg7 32. Ne8+ Kg8
   ```
   Kindly note that each step should be space seperated from each other and there should be space between the step counting and the steps.
   You can find such more input [here](https://en.wikipedia.org/wiki/World_Chess_Championship_2021#Game_11:_Nepomniachtchi%E2%80%93Carlsen,_0%E2%80%931)
   
9. Now go ahead and run the "play.py" file. There is a 5 second buffer time for you to minimize all other windows or switch to the workspace in which your chess windows are setuped.
10. Once the bot has moved all the steps in the input, it resigns the match

# Limitations & Bugs
1. Due to some limitations of OpenCV and Pyautogui, the chess pieces and the size of the chess board should exactly be the same as that of the ones stored in the 'graphics' folder.
2. The bot skips some steps sometimes which completely changes the course of the match

