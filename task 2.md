#Task 2
##Question 6
###1.
The place where you would want to keep track of whether ace is high or low is in the GetRank fuunction.
###2.
The DisplayMenu function must be changed so that you can select option 5 for the options.
###3.
The function you must change for the ranking of the cards is GetRank.
##Pseuducode
FUNCTION DisplayMenu THEN
	OUTPUT'
	OUTPUT MAIN MENU
	OUTPUT 1. Play game (with shuffle)
	OUTPUT 2. Play game (without shuffle)
	OUTPUT 3. Display recent scores'
	OUTPUT 4. Reset recent scores
	OUTPUT 5. Options
	OUTPUT 6. Save to file
	OUTPUT 7. Load scores from file
	OUTPUT
	INPUT Select an option from the menu (or enter q to quit): 
END FUNTCTION

FUNCTION GetOptionChoice
	INPUT OptionChoice
RETURN OptionChoice
END FUNCTION

FUNCTION SetOption
	INPUT choice
RETURN choice
END FUNCTION

FUNCTION SetAceHighOrLow
	HighOrLow <- INPUT
Return HighOrLow
END FUNCTION
##Question 10
###1.It may already have scores which would then mean that there is a total over 10