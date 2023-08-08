# command-line Rock-Paper-Scissors game where a player can play against the computer.


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-guideline)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

**Note: Delete this note and update the table of contents based on what sections you keep.**

## Overview
  Build a command-line Rock-Paper-Scissors game where a player can play against the computer.


### The guideline

**Step 1: User Input for Player's Choice**
1. Print a welcome message to explain the rules of the game.
2. Prompt the player to input their choice: rock, paper, or scissors.

**Step 2: Generate Computer's Choice**
1. Use the `random` module to randomly select the computer's choice among rock, paper, and scissors.

**Step 3: Determine the Winner**
1. Create a function that takes both the player's and computer's choices as arguments.
2. Implement the game's logic to determine the winner based on the choices. Define the rules: rock beats scissors, scissors beats paper, and paper beats rock. Handle ties as well.

**Step 4: Display Results**
1. Display the player's and computer's choices.
2. Display the result of the game: whether the player won, lost, or it's a tie.

**Step 5: Play Again**
1. After displaying the result, ask the player if they want to play again.
2. If the player wants to play again, loop back to Step 1. If not, exit the game with a thank-you message.


### Screenshot

![](./Screenshot.jpg)

### Links

- Solution URL: https://github.com/Don-Wealth/Rock-Paper_Scissors-game

## My process

I created a function -get_choice()- to get the choice of the player using input function.
I created a tuple and stored it in a variable called option. I used the tuple to create the computer's choice and i used the -random.choice- function to make it select randomly. I then created a dictionary using player and computer as key and player_choice and computer_choice as the value respectively, then stored it in a variable called choices and returned choices.

I created another function named -check_win_ to check the winner and i added "player" and "computer" as an arguments. I used "if" and "elif" conditional statement to state the conditions that must be true to win.

I then created -main- function to calculate and print the result. I used the wile loop to set if the user wants to replay or quit.

and i finally called the main function

### Built with

- python
- random module

### What I learned

I learnt how to create and call functions. I also learnt how to use the while loop, how to break from the loop or return.


## Author

-Linkedin - [@Chika Modozie](https://www.linkedin.com/in/chika-modozie-7a220424a/)
- Twitter - [@DonWealth0001](https://twitter.com/DonWealth0001)


## Acknowledgments

i appreciate Sir kadibia for helping me start out on my Journey and guiding me towards the right resources to use.

