def CreateBoard(r, c, b, n):

  for i in range(1,(r+1)):
    n.append(str(i))
  b.append(n)

  for i in range(c):
    b.append(['*']*(r))
  return(b)


def printBoard(b):
  for lst in b:
    print(" ".join(lst))
  return b


def check(board, n):
  n = []
  for i in range(1,len(board[1])+1):
    if board[1][i-1] == '*':
      n.append(i)
  print(n)

  user = (input('Enter column: '))

  if(user.isdigit() == True):
    user = int(user)
    if (user in n):
      return(user)
  print('Invalid input')
  return check(board, n)

def WinningCon(b, r, u, c):
  'row'
  loop1 = True
  rowCon = ""
  colCon = ""
  for i in range(0,len(b[1])):
    rowCon += b[r][i]
    if('X'*4 in rowCon) or('O'*4 in rowCon):
      return(True)
  for i in range(1,c+1):
    colCon += b[i][u-1]
    if('X'*4 in colCon) or('O'*4 in colCon):
      return(True)

def Diag2(u, r, b, row, column):
  utemp1 = u-1
  utemp2 = u-1
  rtemp1 = r
  rtemp2 = r
  end = ""
  beg = ""
  while(True):
    beg += b[rtemp1][utemp1]
    if(rtemp1 == 1):
      break
    elif(utemp1 == column):
      break
    rtemp1 -= 1
    utemp1 += 1
  while(True):
    if(rtemp2 == row-1):
      break
    elif(utemp2 == 0):
      break
    rtemp2 +=1
    utemp2 -=1
    end += b[rtemp2][utemp2]
  beg = beg[::-1]
  fullstring = beg+end
  if('X'*4 in fullstring) or('O'*4 in fullstring):
    return(True)

def Diag1(u, r, b, row, column):
  utemp1 = u-1
  utemp2 = u-1
  rtemp1 = r
  rtemp2 = r
  end = ""
  beg = ""
  while(True):
    beg += b[rtemp1][utemp1]
    if(rtemp1 == 1):
      break
    elif(utemp1 == 0):
      break
    rtemp1 -= 1
    utemp1 -= 1
  while(True):
    if(rtemp2 == row-1):
      break
    elif(utemp2 == column):
      break
    rtemp2 +=1
    utemp2 +=1
    end += b[rtemp2][utemp2]
  beg = beg[::-1]
  fullstring = beg+end
  if('X'*4 in fullstring) or('O'*4 in fullstring):
    return(True)

def ProcessInput(u, s, b, r):
  rowNum = r-1
  u = u-1
  while(not b[rowNum][u] == '*'):
    rowNum -= 1
  b[rowNum][u] = s
  return(rowNum)

def EndGame(g, b, p):
  printBoard(b)
  print("Congrats %s, you've won!" %p)
  replayGame = input('Would you like to play again? Yes or No?\n').lower()
  if replayGame == 'yes':
    MainGame()
  else:
    g = False
    return(g)

def MainGame():
  row = 7 #input('Enter number of rows')
  column = 6 #input('Enter number of columns')
  board = []
  nums = []
  board = CreateBoard(row, column, board, nums)
  player1 = 'K'#input('Enter name: ')
  player2 = 'A'#input('Enter name: ')
  turn = 1
  GameOn = True
  while(GameOn):
    board = printBoard(board)

    if(not turn%2 == 0):
      print("It's %s's turn" %player1)
      user = check(board, nums)
      rc = ProcessInput(user, "X", board, row)
      if(WinningCon(board, rc , user, column) == True):
        GameOn = EndGame(GameOn, board, player1)
      elif(Diag1(user, rc, board, row, column) == True):
        GameOn = EndGame(GameOn, board, player1)
      elif(Diag2(user, rc, board, row, column) == True):
        GameOn = EndGame(GameOn, board, player1)
    else:
      print("It's %s's turn" %player2)
      user = check(board, nums)
      rc = ProcessInput(user, "O", board, row)
      if(WinningCon(board, rc , user, column) == True):
        GameOn = EndGame(GameOn, board, player2)
      elif(Diag1(user, rc, board, row, column) == True):
        GameOn = EndGame(GameOn, board, player2)
      elif(Diag2(user, rc, board, row, column) == True):
        GameOn = EndGame(GameOn, board, player2)
    turn +=1



MainGame()
