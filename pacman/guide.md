#Pac Man

_By Nok Hang Lo_

Welcome to Pacman!

The goal of this game is to eat all the food (represented by *) and special food ($) generated by the game without being eaten by the ghosts.

There are 15 pieces of food and 5 pieces of special food generated every time randomly.

Eating a special food stuns the ghosts and prevents them from moving for 20 moves, and allows the player to eat the ghosts.

Eating normal food gives +1 score, eating special food gives +2 score and eating ghosts give +5 score.

First try playing the original pacman at [this link](https://www.google.com/logos/2010/pacman10-i.html), then try the challenges below.

##Tasks

1. The player can currently walk through walls. Can you fix it so that the player can only move to squares that are empty?

2. The game currently does not check if the user entered a movement command (w/a/s/d). Can you fix it so the game prints an error message if the user does not input a movement command?

3. The player currently does not get +5 score for eating a ghost. Can you fix it so that this feature works?

4. When decrementing the stun duration, the game does not check if the stun duration is greater than 0, so the stun duration becomes negative. Can you fix this?

5. Currently when ghosts are stunned, they are not printed with a colour in the terminal. Can you use the print_coloured_text function to print the ghost with a green colour when they are stunned?

Hint for Challenge 5: Look at other instances of the print_coloured_text function in this code file and see how they are used. To see available colours, look at line 7 in the library file.

## Extension Challenges

1. The custom map is read in from the text file map.txt. Create a custom map of your own by changing the code to load the map instead from a multi-line string: make sure there is a P symbol for the player and at least 1 G symbol.
2. Uncomment lines 33 to 38 to change the symbols on the board to emojis. Go to this [emojis site](https://www.unicode.org/emoji/charts/full-emoji-list.html) (warning may take time to load) and find your own emojis to replace the default symbols
3. There are a lot of variables and functions in this code file all related to the game. Read about python classes on [W3Schools](https://www.w3schools.com/python/python_classes.asp) and try to make these variables and functions part of a class.
