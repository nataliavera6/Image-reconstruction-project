# explore.py
messages = [
    'Hpwnzxp ez esp ajeszytn ufyrwp! Hp slgp opepnepo l atpnp zq plces qcfte ty jzfc alnv. Estd td olyrpczfd ez esp Ajeszytn Ufyrwp pygtczyxpye. Awpldp cpxzgp te ez nzyetyfp.',
    'Hpwnzxp ez esp Ajeszytn Ufyrwp! Nzyetyfp jzfc piawzcletzy mj clqetyr lnnczdd esp ctgpc.',
    ]

pack = {'raft': {'origin': 'pythonic', 'length': 5, 'width': 5}}
        #'apple': {'origin': 'earth', 'size': 0.25, 'density': 0.8}}

### Additional Functions ##############

# Your code goes here.
#test functions 


    
# shifts message a inputted amount of times
def shift_message(number, message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_word = ""

   # loops through every letter in encoded message and finds its value after shifting
    for letter in message:
        if letter.isalpha():
            unshifted_index = alphabet.index(letter.lower())
            shifted_letter = alphabet[unshifted_index - number]
	  # handles uppercase letters
            if letter.isupper():
                shifted_letter = shifted_letter.upper()
            shifted_word += shifted_letter
	# handles non-alphabetic values
        else:
            shifted_word += letter
    return shifted_word


# loops through every number ranging from 1-25 and prints the shifted message
def decode_message(message):
    for number in range(0, 25):
        print(" ")
        #for sentence in message:
        print(shift_message(number, message))
        

#######################################

def check_pack(pack):
  '''
  pack is a dictionary with tools for exploring the pythonic jungle
  returns False if any earth fruit is contained in the pack.
  (Note: This is important for environmental stability.)
  '''
  for item in pack.values():
    if item.get('origin') == 'earth':
      return False
  return True

def cross_river(raft):
  '''
  raft is an object with properties for the raft.
  returns True if the raft can cross the river.
  '''
  length = raft.get('length')
  width = raft.get('width')
  depth = 1
  volume = length*width*depth
  density = 0.5
  p_water, gravity = 1, 10
  minimum_volume = 100/((p_water-density)*gravity)

  if length <= 0.0 or width <= 0.0:
    return("Please enter valid (nonzero) raft properties.")
  elif length < 2 or width < 2:
    return("Your raft is too small... you fell off!")
  elif length > 10 or width > 10:
    return ("Your raft is too big... it got stuck!")
  elif volume < minimum_volume:
    return("Your raft sank! Try again!")
  else:
    return("Congratulations! You made it across the river!")

while True:
  if check_pack(pack):
    print("Welcome to the Pythonic Jungle! Continue your exploration by rafting accross the river.")
    cross_river(pack.get('raft'))
  else:
    #print(messages[0])
    print(decode_message(messages[0]))
  
  break







