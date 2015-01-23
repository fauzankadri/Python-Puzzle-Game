# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*


PUZZLE1 = '''
glkutqyu
onnkjoaq
uaacdcne
gidiaayu
urznnpaf
ebnnairb
xkybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyotiutuvpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''



def rotate_puzzle(puzzle):
  '''(str) -> str
  Return the puzzle rotated 90 degrees to the left.
  '''
  
  raw_rows = puzzle.split('\n')
  rows = []
  # if blank lines or trailing spaces are present, remove them
  for row in raw_rows:
    row = row.strip()
    if row:
      rows.append(row)
  
  # calculate number of rows and columns in original puzzle
  num_rows = len(rows)
  num_cols = len(rows[0])
    
  # an empty row in the rotated puzzle
  empty_row = [''] * num_rows
    
  # create blank puzzle to store the rotation
  rotated = []
  for row in range(num_cols):
    rotated.append(empty_row[:])
  for x in range(num_rows):
    for y in range(num_cols):
      rotated[y][x] = rows[x][num_cols - y - 1]
  
  # construct new rows from the lists of rotated
  new_rows = []
  for rotated_row in rotated:
    new_rows.append(''.join(rotated_row))
  
  rotated_puzzle = '\n'.join(new_rows)
  
  return rotated_puzzle
  
def lr_occurrences(puzzle, word):
  '''(str, str) -> int
  Return the number of times word is found in puzzle in the 
  left-to-right direction only.
  
  >>> lr_occurrences('xaxy\\nyaaa', 'xy')
  1
  '''
  return puzzle.count(word)


# ---------- Your code to be added below ----------

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.

#outputs the number of given word found in given puzzle
def total_occurrences(puzzle, word):
  '''(str, str) -> int
  Return total occurrences of word in puzzle.
  All four directions are counted as occurrences:
  left-to-right, top-to-bottom, right-to-left, and bottom-to-top.
  
  >>> total_occurrences('xaxy\\nyaaa', 'xy')
  2
  '''
  # your code here
  total_occurrences=0
  total_occurrences = lr_occurrences(puzzle,word)+ \
  lr_occurrences(rotate_puzzle(puzzle),word)+ \
  lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)),word)+ \
  lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle))),word)
  
  return total_occurrences
                                
  

# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

#if word is found horizontally, it will return True. otherwise False
def in_puzzle_horizontal(puzzle, word):
  '''
  (str,str) -> bool
  
  >>> in_puzzle_horizontal('xyyyyxpxy','xy')
  True
  >>> in_puzzle_horizontal('abuuuubauufab','ab')
  True
  >>> in_puzzle_horizontal ('xxxx\\nxxxx', 'xy')
  False
  
  REQ: puzzle as str and word and str
  
  Returns True if the given word can be found horizontally in the given puzzle
  from left to right or right to left or both ways. Otherwise Returns False
  '''
  
  return ((lr_occurrences(puzzle,word)>0) or \
          (lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)),word))>0)


# *task* 8: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

#if word is found vertically, it will return True. Otherwise False
def in_puzzle_vertical(puzzle, word):
  '''
  (str,str) -> bool
  >>> in_puzzle_vertical('xyyyyxpxy','xy')
  False
  >>> in_puzzle_vertical ('abuuuubauufab','ab')
  False
  >>> in_puzzle_vertical ('xxxx\\nxxay', 'xy')
  True
  
  REQ: puzzle and word to be str
  
  Returns if and only if the word can be found in the puzzle vertically from 
  top to bottom or bottom to top or both ways. Otherwise Returns False
  
  '''
  
  return ((lr_occurrences(rotate_puzzle(puzzle),word)>0) or \
         (lr_occurrences(rotate_puzzle(rotate_puzzle \
                                       (rotate_puzzle(puzzle))),word)>0))


# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

#Looks for the word in all 4 directions. if found returns True else False
def in_puzzle(puzzle, word):
  '''
  (str,str) -> bool
  
  >>> in_puzzle('xxxx\\nyxxx','fr')
  False
  >>> in_puzzle('xxxx\\nyxxx','xy')
  True
  >>> in_puzzle('fasgreatgrs\\npolpopoleqr','great')
  True
  >>> in_puzzle('fasgreatgrs\\npolpopoleqr', 'qqq')
  False
  
  REQ: puzzle and word as str
  
  Returns True if the word is found in the puzzle once or more from 
  left to right, right to left,top to bottom, or bottom to top.
  Otherwise Returns False
  
  '''
  return ((in_puzzle_horizontal(puzzle,word)) or \
         (in_puzzle_vertical(puzzle,word)))


# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

#Check if word is only in horizontal and not vertical or 
#is in vertical but not in horizontal
def in_exactly_one_dimension(puzzle, word):
    '''
    (str,str) -> bool
    
    >>> in_exactly_one_dimension('xxyx','xy')
    True
    >>> in_exactly_one_dimension('xxyx\\nxyxx','xy')
    False
    >>> in_exactly_one_dimension('xxgreatuu\\ngreatvvyy','great')
    True
    >>> in_exactly_one_dimension('xtyuo\\neroqw','yo')
    True
    >>> in_exactly_one_dimension('xxxxx\\nyyyyy','ff')
    True
    
    REQ: puzzle and word to be string
    
    Returns True iff the word is found horizontally and not vertically or
    is found vertically and not horizontally. Otherwise Returns False
    
    '''
    
    return (((in_puzzle_horizontal(puzzle,word)==True) and \
            (in_puzzle_vertical(puzzle,word))==False)or\
            ((in_puzzle_horizontal(puzzle,word)==False) and\
            ((in_puzzle_vertical(puzzle,word))==True)) or \
            ((in_puzzle_horizontal(puzzle,word)==False) and \
             (in_puzzle_vertical(puzzle,word)==False)))


# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

#Returns true if the word is in horizontal or not in puzzle but the word cannot
#be in vertical
def all_horizontal(puzzle, word):
  '''
  (str,str)-> bool
  
  >>> all_horizontal('abc\\nbac\\ncab','abc')
  False
  >>> all_horizontal('abc\\nbbb','abc')
  True
  >>> all_horizontal('gra\\ngba','gg')
  False
  >>> all_horizontal('abc\\naac\\ncab','xyz')
  True
  
  Returns True if the word is found horizontally or not in puzzle but the word
  cannot be found vertical. If word is found vertical, it will return False
  '''
  return (in_puzzle_vertical(puzzle,word)!=True)


# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

#True if the word occures only once and the occurrence is vertical
def at_most_one_vertical(puzzle, word):
  '''
  (str,str)->bool
  
  >>> at_most_one_vertical('abc\\nbba\\nbba','abc')
  False
  >>> at_most_one_vertical('abc\\nagg\\naty','aaa')
  False
  >>> at_most_one_vertical('aac\\naay\\naat','aaa')
  False
  >>> at_most_one_vertical('abc\\nabc','abc')
  False
  
  REQ: puzzle and word to be str
  
  Returns True of the word occures once and the occurrences is vertical
  Otherwise returns False
  
  '''
  return ((total_occurrences(puzzle,word)==1) and \
          (in_puzzle_vertical(puzzle,word)))


def do_tasks(puzzle, name):
  '''(str, str) -> NoneType
  puzzle is a word search puzzle and name is a word.
  Carry out the tasks specified here and in the handout.
  '''

  # *task* 1a: add a print call below the existing one to print
  # the number of times that name occurs in the puzzle left-to-right.
  # Hint: one of the two starter functions defined above will be useful.

  print('Number of times', name, 'occurs left-to-right: ', end='')
  # your print call here
  occurrences_lr = lr_occurrences(puzzle, name)
  print(occurrences_lr) 

  
  # *task* 1b: add code that prints the number of times
  # that name occurs in the puzzle top-to-bottom.
  # Hint: both starter functions are going to be useful this time!
  occurrences_tb=lr_occurrences(rotate_puzzle(puzzle), name)
  
  print('Number of times', name, 'occurs top to bottom: ', end='')
  print(occurrences_tb)


  # *task* 1c: add code that prints the number of times
  # that name occurs in the puzzle right-to-left.
  occurrences_rl=lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), name)
  
  print('Number of times', name, 'occurs right to left: ', end='')
  print(occurrences_rl)  


  # *task* 1d: add code that prints the number of times
  # the number of times that name occurs in the puzzle bottom-to-top.
  occurrences_bt = lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle(
    puzzle))), name)
  
  print('Number of times', name, 'occurs bottom to top: ', end='')
  print(occurrences_bt)

  
  # *task* 4: print the results of calling total_occurrences on puzzle and name.
  # Add only one line below. 
  # Your code should print a single number, nothing else.
  print(total_occurrences(puzzle,name))


  # *task* 6: print the results of calling in_puzzle_horizontal on 
  # puzzle and name.
  # Add only one line below. The code should print only True or False.
  print(in_puzzle_horizontal(puzzle,name))



do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, 'nick')

# *task* 7: call do_tasks on PUZZLE2 (that's a 2!) and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, 'nick')

# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE1,'nick'))

# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'anya'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE2,'anya'))
