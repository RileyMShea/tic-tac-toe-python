
    
'''    
  
'''                

    
    
def milestone():
    '''
    This is a project to creat a tic-tac-toe game within python
    -Two should be able to play the game (both sitting at the same computer)
    -The board should be printed out every time a player makes a move
    -You should be able to accept input of the player position and then place a symbol on the board
    '''
    from IPython.display import clear_output
    
    positions = {'topleft':' ','top':' ','topright':' ','left':' ','middle':' ','right':' ','bottomleft':' ','bottom':' ',
                'bottomright':' '}
    winner = 'tbd'
    def gameboard(pos,value):
        '''
        This will take the input of position on the the tic tac toe board and either an 'X' for player 1 or an 'O' for player 2
        and then update and print the board accordingly
        '''

        positions[pos] = value
        print positions['topleft'],'|',positions['top'],'|',positions['topright']
        print '--------'
        print positions['left'],'|',positions['middle'],'|',positions['right']
        print '--------'
        print positions['bottomleft'],'|',positions['bottom'],'|',positions['bottomright']
        print ''
        
    def testwinner(winner):
        
        #This will check the gameboard to see if there has been a winner or a tie
        
        totalsquares = 0
        #Top row win WORKING
        if (positions['topleft']==positions['top']==positions['topright']): #check if the top squares are the same
            if positions['topleft'] == ('X' or 'O'): #check if the top left position is X or O
                winner = positions['topleft'] # set the winner to the value of topleft, either X or O
        #Middle row win WORKING
        elif(positions['left']==positions['middle']==positions['right']):
            if positions['left'] == ('X' or 'O'):
                winner = positions['left']
        #Bottom row win DELAYED WORKING
        elif(positions['bottomleft']==positions['bottom']==positions['bottomright']):
            if positions['bottomleft'] == ('X' or 'O'):
                winner = positions['bottomleft']
        #Diagonal win 1
        elif(positions['topleft']==positions['middle']==positions['bottomright']):
            if positions['topleft'] == ('X' or 'O'):
                winner = positions['topleft']
        #Diagonal win 2
        elif(positions['bottomleft']==positions['middle']==positions['topright']):
            if positions['bottomleft'] == ('X' or 'O'):
                winner = positions['bottomleft']
        #Left Column win
        elif(positions['bottomleft']==positions['left']==positions['topleft']):
            if positions['bottomleft'] == ('X' or 'O'):
                winner = positions['bottomleft']            
        #Middle Column win
        elif(positions['top']==positions['middle']==positions['bottom']):
            if positions['top'] == ('X' or 'O'):
                winner = positions['top']
        #Right column win
        elif(positions['topright']==positions['right']==positions['bottomright']):
            if positions['topright'] == ('X' or 'O'):
                winner = positions['topright']
        #Full game board tie
        if winner == 'tbd':
            for key,value in positions.iteritems():
                if value == 'X' or value == 'O':
                    totalsquares += 1
            print totalsquares
            if totalsquares == 9:
                winner = 'tie'
                
        return winner
    
              
        
        
    print testwinner(winner)    
    square = ''
    player = 1
    gameboard('top',' ')        
    while(testwinner(winner) == 'tbd'):
        if player == 1:            
            square = raw_input('Player 1 (X) Choose a square to mark:')
            clear_output()
            gameboard(square,'X')
            testwinner(winner)
            player +=1 #set move to be player 2
        elif player == 2:
            square = raw_input('Player 2 (O) Choose a square to mark:')
            clear_output()
            gameboard(square,'O')
            testwinner(winner)
            player -= 1 # set move to be player 1

    if testwinner(winner) == ('X' or 'O'):
        print 'Congratulations player %s you have have won the game!' %testwinner(winner)
    else:
        print 'You have tied =/'
#    else:
#        break



milestone()
