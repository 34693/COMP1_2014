
# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

import random
import datetime
import pickle
import pdb

NO_OF_RECENT_SCORES = 10
SameCardRule = 'C'

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = ''

Deck = [None]
RecentScores = [None]
Choice = ''

def CreateDeck():
  card = TCard()
  Deck = []
  suit = 1
  
  for count in range(4):
    score = 1
    for count in range (13):
      card.Rank = score
      card.Suit = suit
      Deck.append(card)
      score = score + 1
    suit = suit + 1
  for count in range(len(Deck)):
      print(Deck[count].Suit,'suit')
      print(Deck[count].Rank,'rank')
  return Deck

def GetRank(RankNo, HighOrLow):

  if HighOrLow == 'l':
    Rank = ''
    if RankNo == 1:
      Rank = 'Ace'
    elif RankNo == 2:
      Rank = 'Two'
    elif RankNo == 3:
      Rank = 'Three'
    elif RankNo == 4:
      Rank = 'Four'
    elif RankNo == 5:
      Rank = 'Five'
    elif RankNo == 6:
      Rank = 'Six'
    elif RankNo == 7:
      Rank = 'Seven'
    elif RankNo == 8:
      Rank = 'Eight'
    elif RankNo == 9:
      Rank = 'Nine'
    elif RankNo == 10:
      Rank = 'Ten'
    elif RankNo == 11:
      Rank = 'Jack'
    elif RankNo == 12:
      Rank = 'Queen'
    elif RankNo == 13:
      Rank = 'King'

  elif HighOrLow == 'h':

    if RankNo == 1:
      Rank = 'Two'
    elif RankNo == 2:
      Rank = 'Three'
    elif RankNo == 3:
      Rank = 'Four'
    elif RankNo == 4:
      Rank = 'Five'
    elif RankNo == 5:
      Rank = 'Six'
    elif RankNo == 6:
      Rank = 'Seven'
    elif RankNo == 7:
      Rank = 'Eight'
    elif RankNo == 8:
      Rank = 'Nine'
    elif RankNo == 9:
      Rank = 'Ten'
    elif RankNo == 10:
      Rank = 'Jack'
    elif RankNo == 11:
      Rank = 'Queen'
    elif RankNo == 12:
      Rank = 'King'
    elif RankNo == 13:
      Rank = 'Ace'

  return Rank
    



    
    


def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print('6. Save to file')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  print()
  return Choice

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  Cards = []
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
    
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank, HighOrLow), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def SameCard(LastCard, NextCard):
  if NextCard.Rank == LastCard.Rank and SameCardRule == 'E':
    GameOver = True
  else:
    GameOver = False
  return GameOver

def GetPlayerName():
  print()
  name = False
  while not name:
    GiveName = input("Do you want to give your name for the leaderboard (y/n)")
    if GiveName in['y','yes','YES','Yes','Y']:
      valid = False
      name = True
    elif GiveName in['n','N','No','no']:
      valid = True
      name = True
      PlayerName = 'Anonymous'
    else:
      name = False
    
  print()
  while not valid:
    PlayerName = input('Please enter your name: ')
    if len(PlayerName) < 1:
      valid = False
    else:
      valid = True
  print()
  return PlayerName

def GetChoiceFromUser():
  valid = False
  while not valid:
    Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
    if Choice in['Y','YES','y','yes','Yes']:
      Choice = 'y'
      valid = True
    elif Choice in ['N', 'NO','n','No']:
      Choice = 'n'
      valid = True
    elif Choice == 's':
      valid = True
    else:
      valid = False
    
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("Name".ljust(10),'Date'.ljust(10),'Score')
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print(RecentScores[Count].Name.ljust(10),RecentScores[Count].Date.ljust(10),RecentScores[Count].Score)
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  PlayerName = GetPlayerName()
  today = datetime.date.today()
  Date = today.strftime('%d-%m-%y')
  FoundSpace = False
  Count = 1
  while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
    if RecentScores[Count].Name == '':
      FoundSpace = True
    else:
      Count = Count + 1
  if not FoundSpace:
    for Count in range(1, NO_OF_RECENT_SCORES):
      RecentScores[Count].Name = RecentScores[Count + 1].Name
      RecentScores[Count].Score = RecentScores[Count + 1].Score
    Count = NO_OF_RECENT_SCORES
  RecentScores[Count].Name = PlayerName
  RecentScores[Count].Score = Score
  RecentScores[Count].Date = Date


def DisplayOptions():
  print()
  print('1. Set ace to be HIGH or LOW')
  print('2. Card of same score ends game')
  print()
def GetOptionChoice():
  OptionChoice = int(input("Please enter your option choice."))
  return OptionChoice

def ValidateOption():
  DisplayOptions
  valid = False
  while not valid:
    OptionChoice = GetOptionChoice()
    if OptionChoice == 1:
      valid = True
    elif OptionChoice == 2:
      valid = True
    else:
      valid = False
  return OptionChoice

def SetSameCardRule():
  SameCardRule = input("Please etner whetther you want the same card to (C)ontinue the game or (E)nd the game")
  return SameCardRule

def SetAceHighOrLow():
  HighOrLow = input("Please enter if you want ace (h)igh or (l)ow")
  return HighOrLow

def SetOption():
  choice = ValidateOption()
  return choice


def SaveToFile(RecentScores):
  with open("save_scores.txt", encoding="utf-8",mode="w") as my_file:
    for record in range(1,NO_OF_RECENT_SCORES +1):
      my_file.write(str(RecentScores[record].Score)+"\n")
      my_file.write(str(RecentScores[record].Date)+"\n")
      my_file.write(str(RecentScores[record].Name) +"\n")

        

def load_scores():
  RecentScores = [""]
  with open("save_scores.txt", mode="r", encoding = "utf-8") as Scores:
    for count in range(1,NO_OF_RECENT_SCORES + 1):
      ScoreRecord = TRecentScore()
      ScoreRecord.Score = Scores.readline().rstrip("\n")
      ScoreRecord.Date = Scores.readline().rstrip("\n")
      ScoreRecord.Name = Scores.readline().rstrip("\n")
      RecentScores.append(ScoreRecord)
    for count in range(1, NO_OF_RECENT_SCORES + 1):
      try:
        int(RecentScores[count].Score)
      except ValueError:
        RecentScores[count].score = None
    print()
    print("Load completed!")
  return RecentScores
  

def PlayGame(Deck, RecentScores):
  Save = False
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n') and (Choice != 's'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    if LastCard.Rank == NextCard.Rank and SameCardRule == 'C':
      NoOfCardsTurnedover = NoOfCardsTurnedOver
    elif Choice == 's':
      Score = NoOfCardsTurnedOver
      SaveGameProgess(NextCard,LastCard,Deck,NoOfCardsTurnedOver,Score)
    else:
      NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if LastCard.Rank == NextCard.Rank and SameCardRule == 'E':
      GameOver = True
    elif (LastCard.Rank == NextCard.Rank and SameCardRule == 'C') or (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

def BubbleSortScores(RecentScores):
    swapped = True
    list_length = len(RecentScores)
    while swapped:
        list_length = list_length - 1
        swapped = False
        print(RecentScores[1].Score)

        for count in range(1,list_length):
            if RecentScores[count].Score < RecentScores[count+1].Score:
                tempScore = RecentScores[count].Score
                tempDate = RecentScores[count].Date
                tempName = RecentScores[count].Name
                
                RecentScores[count].Score = RecentScores[count+1].Score
                RecentScores[count].Date = RecentScores[count+1].Date
                RecentScores[count].Name = RecentScores[count+1].Name
                RecentScores[count+1].Score = tempScore
                RecentScores[count+1].Date = tempDate
                RecentScores[count+1].Name = tempName                
                swapped = True

    return RecentScores

def Save_Progress(NoOfCardsTurnedOver):
    with open("progressSave.txt", mode='w',encoding='utf-8')as GameSave:
        temp= NoOfCardsTurnedOver
        GameSave.write(str(temp))
    with open("deck.txt",mode='w',encoding='utf-8')as deck:
        for each in deck:
          deck.write(str(each)+"\n")

def SaveGameProgess(NextCard,LastCard,Deck,NoOfCardsTurnedOver,Score):
  GameData = [NextCard,LastCard,NoOfCardsTurnedOver,Score]
  with open("gameprogress.dat", mode="wb") as SaveData:
    pickle.dump(GameData,SaveData)
  SaveDeck(Deck)

def SaveDeck(Deck):
  with open('deck.txt',mode="w",encoding="utf-8") as DeckCards:
    for Card in Deck:
      if Card != None:
        DeckCards.write(str(Card.Suit)+"\n")
        DeckCards.write(str(Card.Rank)+"\n")

if __name__ == '__main__':
##  for Count in range(1, 53):
##    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Deck = CreateDeck()
  for each in Deck:
    print(Deck[each].Suit)
    print(Deck[each].Rank)
  Choice = ''
  HighOrLow = 'l'
  try:
    RecentScores = load_scores()
  except:
    IOError
    ValueError
    SaveToFile(RecentScores)
  while Choice not in['q','quit','QUIT','Q','Quit']:
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      load_scores()
      RecentScores = BubbleSortScores(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
      choice = SetOption()
      if choice == 1:
        HighOrLow = SetAceHighOrLow()
      elif choice == 2:
        SameCardRule = SetSameCardRule()
    elif Choice == '6':
      SaveToFile(RecentScores)



      
      



  
      

