from libraries import *

#black = '#000000'
#yellow = '#FFFF00'
#red = '#FF0000'
#green = '#00FF00'

#orange = '#FFA500'
#dark_green = '#006400'

def DNA_chip(switches, title):
 
    window = tk.Tk()
    window.title(title)
    
    N = 4
  	
    lights = [[None for _ in range(N)] for _ in range(N)]

    for row in range(N):
      for col in range(N):
        switch_button = tk.Label(window, width=10, height=5, bg='#000000')
        switch_button.grid(row=row, column=col, padx=5, pady=5)
        
        if switches[row][col] == None:
           lights[row][col] = switch_button.config(bg='#000000')
        
        else:           
           #diagonal: similar base
           if row == col: 
            lights[row][col] = switch_button.config(bg='#00FF00')
           
           #reverse-diagonal: hybridization
           if row != col:
            lights[row][N - 1 - col] = switch_button.config(bg='#FFFF00')
             
           #non diagonal: mismatches 
           if (row + col < N - 1):
            #top non diagonal
            if (row < col and row != col and row + col):
             lights[row][col] = switch_button.config(bg='#FF0000')
            #left non diagonal
            elif row != col:
             lights[row][col] = switch_button.config(bg='#FF0000') 
           
           else:
            #bottom non diagonal
            if (row > col and row + col != N - 1):
             lights[row][col] = switch_button.config(bg='#FF0000')
            #right non diagonal
            else:
             if (row + col != N - 1 and row!=col):
              lights[row][col] = switch_button.config(bg='#FF0000')
                  
    window.mainloop()

def Hashed_chip(initial_hex_codes, switches, title):
 
    window = tk.Tk()
    window.title(title)
    
    N = 4
    
    lights = [[None for _ in range(N)] for _ in range(N)]
    
    for row in range(N):
      for col in range(N):
        switch_button = tk.Label(window, width=10, height=5, bg = '#000000')
        switch_button.grid(row=row, column=col, padx=5, pady=5)
        
        if switches[row][col] == None:
           lights[row][col] = switch_button.config(bg='#000000')
           
        else:
        
         #reverse-diagonal: hybridization
         if row != col:
          lights[row][N - 1 - col] = switch_button.config(bg= initial_hex_codes[3])
                 
         #diagonal: similar base
         if row == col: 
          lights[row][col] = switch_button.config(bg= '#000000')
          if (row == 0 and col == 0) or (row == 2 and col == 2):
           lights[row][col] = switch_button.config(bg= initial_hex_codes[0]) 
                              
         #non diagonal: mismatches 
         if (row + col < N - 1):
          #top non diagonal
          if (row < col and row != col and row + col):
           lights[row][col] = switch_button.config(bg= initial_hex_codes[1])
          if (row == 0 and col == 2):
           lights[row][col] = switch_button.config(bg= initial_hex_codes[2])
         
          #left non diagonal
          elif row != col:
           lights[row][col] = switch_button.config(bg= initial_hex_codes[1])
           if (row == 2 and col == 0):
            lights[row][col] = switch_button.config(bg= initial_hex_codes[2])  
           
         else:
           #bottom non diagonal
           if (row > col and row + col != N - 1):
            lights[row][col] = switch_button.config(bg= initial_hex_codes[1])
           if (row == 3 and col == 1):
            lights[row][col] = switch_button.config(bg= '#000000')
          
           #right non diagonal
           else:
            if (row + col != N - 1 and row!=col):
             lights[row][col] = switch_button.config(bg= initial_hex_codes[1])
            if (row == 1 and col == 3):
             lights[row][col] = switch_button.config(bg= '#000000')
    
                      
    window.mainloop()






    

