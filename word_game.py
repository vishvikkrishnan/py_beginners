#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import modules
import time
import random

#Make a list of questions and respective answers
Questions=['snow-carrot-buttons', 'face-see-two', 'sky-bright-morning', 'big-blue-water', 'insect-colours-cocoon', 'plant-colours-fragrance', 'amphibian-tadpole-hop', 'night-white-sky', 'leaves-stem-root', 'furniture-four legs-sit']
answers=['snowman', 'eyes', 'sun', 'ocean', 'butterfly', 'flower', 'frog', 'moon', 'tree', 'chair']
#Initialise score
score=0
#Make a list of numbers
no=[0,1,2,3,4,5,6,7,8,9]
random.shuffle(no)
#Instructions to play game
print('**This is a word guessing game**')
print('Type a word connecting the given three words. Example: eat-healthy-sweet Answer is: fruit')
print('You have 20 seconds to guess 10 questions')
print('Shall we start? press y if you want to play the game')
#Start the game
if str(input()).lower()=='y':
    now = int(time.time())
    future = now + 20
    i=0
    while int(time.time()) < future:
        print('Time Left: ', future-int(time.time()))
        print(Questions[no[i]])
        if str(input()).lower()==answers[no[i]]:
            score=score+1
        i=i+1
        pass
#Print the score
print('Total Score is: ',score)
