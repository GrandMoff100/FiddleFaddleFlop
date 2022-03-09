# FiddleFaddleFlop
The popular math game implemented in Python (Computer vs Human)

## Gameplay
The gameplay is pretty simple, and is very similar to the popular (as of Mar 8, 2022) New York Times daily Wordle game.

### Object
Much like, the object of the game is to guess something in the least amount of guesses.
In the case of Fiddle Faddle Flop, the object is to guess three-digit number with three unique digits between 1-9.

### Guessing
The guessing rules are as follows:
1. The guesser guesses any three digit number.
2. The secret-number keeper (a.k.a just the keeper) respondes with a sequence of fiddles, faddles, and flops that **DO NOT** correspond with the order of numbers in the guess.

| Guess Component | Meaning |
| :---            |    :----:   |
| Fiddle          | One of the numbers in the guess is correct and in the right spot |
| Faddle       | One of the numbers in the guess is correct but in the wrong spot |
| Flop | One of the numbers in the guess is wrong |

### Ending
The game ends when the guesser receives a response of Fiddle Fiddle Fiddle, or in other words, the number hass all the correct number in the correct spots.

## Real-World Example

Let us say that you are the guesser and I am the number keeper.
For the purpose of this example I am going to flat out tell you before hand that my number is `794` (but in a real game you would not know this).

### Guess One
Your first guess, say you guess `123`.
I respond with Flop Flop Flop.
Now you know that neither 1, 2, or 3 are in the number you are trying to guess.

### Guess Two
Now knowing that 1, 2, and 3 aren't in the number you guess a completely different number, `456`.
I respond with Flop Faddle Flop. (Recall that my response does not have to match to the order of numbers in your guess.)
You now know that either 4, 5, or 6, is in the number but in the wrong spot and the other two numbers are not in the number at all.

### Guess Three
In order to narrow down the search area you guess a number that three numbers that you have not guessed yet, `789`.
To this I respond with Faddle Fiddle Flop.
Now you know that one of 7, 8, and 9 is correct and in the right spot, one of them correct but in the wrong spot, and one is flat out wrong.

### Guess Four
Now comes the hard (or fun) part of the game.
(Depending on whether or not you enjoy problem-solving and critical thinking about math/logic.)
Here you can use logic like the following.
One of 7, 8, and 9 is a correct number in the correct spot.
Let's say it is 8.
Then if this true, then you know that 5 is not in second spot of our final number if at all, because it had the same position as 8 in our second guess.
We referencing your third guess, assuming 8 is a fiddle number, then either 7, or 9 is the faddle number (from your third guess).
Let's say it's 9.
Then because 8 is the correct spot, and 9 is the wrong spot (based on our assumption) then 9 is deduced to be the first spot because it cannot be in the second or third spots.
Next, because one of 4, 5, or 6 is a faddle number (from our second guess).
But because if 6 was faddle number that means it was not in the right spot meaning that it cannot go in the third spot of our number.
So therefore, only 4 or 5 could in the third spot.
Let's say we pick 5, then our fourth guess is `985`.

Then I respond with Flop Faddle Flop.

### Guess Five
Now we repeat our logic from your fourth guess.
One of 7, 8, and 9 is a correct number in the correct spot.
Let's say it is 7 instead, this time.
Then if this true, then you know that 4 is not in first spot of our final number if at all, because it had the same position as 7 in our second guess.
We looking at your third guess, assuming 7 is a fiddle number, then either 8, or 9 is the faddle number (from your third guess).
Let's go with 9, because it is likely that 8 is flop number being that it 2 in 3 chance (from our fourth guess).
Then because 7 is the correct spot, and 9 is the wrong spot (based on our assumption that it is a faddle number) then 9 is deduced to be the second spot because it cannot be in the first, or third spots.
Next, because one of 4, 5, or 6 is a faddle number (from our second guess).
But because if 6 was faddle number that means it was not in the right spot meaning that it cannot go in the third spot of our number, as it was in the third spot in your second guess).
So therefore, only 4 or 5 could in the third spot.
Let's say we pick 4, then our fourth guess is `794`.

Next I respond with Fiddle Fiddle Fiddle.
Congratulations!
You guessed the number!

### Conclusion
Because we picked numbers to fill in blank spots in our guess, there is an element of chance to the number guesses you'll use in your games.
But much of your strategy can be from logic and as your continue to play the game you can hone your existing logic, and work on new logic too.


## Implementation
Now back to this project.
This project mplements this game in Python, or more accurately creates a Computer-Human dynamic where it comes up with a number, and you have to guess the number.
Giving you an opportunity to practice!

In order to save you typing time, Fiddle Faddle and Flop are abbreviated to the `i`, `a`, and `o`.
(The second letters of the guess response component types.)

## Usage

...

## The Future

...

## Contributing

...

## License

This software is copyrighted by © Nathan Larsen, 2022 under the MIT License.
(See LICENSE file.)
