#Task 1 question 3
 1.The function resposible for the name is the GetPlayerName() function.
 2.To make sure theat the user is repeatedly asked I will create a while loop which will only exit if the length of the name is more than 0.
 3.A variable which will be a boolean data type which will be for the while loop.

 FUNCTION in pseudo-code

 FUNCTION GetPlayerName
	OUTPUT''
	valid <- False
	WHILE not valid THEN
	INPUT PlayerName
	IF len(PlayerNaame) < 1 THEN
			Valid <- False
		ELSE THEN
			Valid <- True
		END IF
	END WHILE
	OUTPUT ''
	END FUNCTION

##Question 5
1.You must import datetime module
2.The update recent score function
Display recent score
Record for the recent score
importing the module
3.You must use %d/%m/%y which displays each component of the date.
##Additional Task - Variable roles
###Question 1
1.Fixed value is a variable which has a value which is never going to change.
2.A stepper value is a value which increases at a certain rate it could be used for populating a random list which would increase it at one per step.
3.Most recent holder is a variable which is used to store the most recent value from a sequence of values for example if you were adding up a total it would store the last value added.
4.Most wanted holder is a variable which stores the most relevant number at that time for example if you were looking through a list for the smallest number it would store the smallest encountered number so far as this type of variable.
5.Gatherer It keeps a running total of all of the values so far.  So if you were adding up a total it would hold the latest total from that point.
6.Transformation variables role is to get its new value from a fixed calculation for example it could be a conversion between pounds and kg it would hold the weight in kg.#
7.Followers role is to store the previous value of a variable for example if there was a value which needed to be kept for example in a bubble sort.
8.Temporary variables are for storing a value for a short period of time so you dont loose it this could be when you want to swap the value of two variables.
##Question 2
1.Fixed Value - Today in the update recent score function.
2.Stepper Value - Count in the update recent score function.
3.Most recent holder - score in class for leaderboards.
4.Most wanted holder - Current card in the play function.
5.Gatherer - Current score of the player in the play game function.
6.Follower - Date in the update recent score function.
7.Temporary - Today in the date function as it is simply their to be used to get the date.
##Question 1
If you pass by reference this means that you are using parameters and that the value you are using is avaliable to use across the whole program  whereas if you reference by value the variables within the function are only appropriate within the function.
##Question 2
1.GetRank by reference
2.GetSuit by reference
3.DisplayMenu by value
4.GetMenuChoice by value
5.LoadDeck by reference
6.ShuffledDeck by reference
7.DisplayCard by reference
8.GetCard by reference
9.GetPlayerName by value
10.GetChoiceFromUser by value
11.DisplayEndOfGameMessage by reference
12.DisplayCorrectGuessMessage by reference
13.ResetRecentScores by reference
14.DisplayRecentScores by reference 
15.UpdateRecentScores by reference
16.PlayGame by reference



