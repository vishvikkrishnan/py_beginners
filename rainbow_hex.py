# returns the hex value for any of the colors of the rainbow ('R', 'O', 'Y', 'G', 'B', 'I', 'V')
def hex(color):
    switcher={
        'red': 'FF0000',
        'orange': 'FF7F00',
        'yellow': 'FFFF00',
        'green': '00FF00',
        'blue': '0000FF',
        'indigo': '2E2B5F',
        'violet': '8B00FF'
    }
    return switcher.get(color, "This is not a base color in the rainbow!")

def main():
    #get color input from user
    color = input("Please enter a color of the rainbow: ")
    
    #print the hex value of the color
    print (f'The hexadecimal value for this color is: {hex(color.lower())}')

if __name__=="__main__":
    main()

#simple unit test
def test():
    assert hex('red')=='FF0000' , "Should be FF0000"
    assert hex('indigo')=='2E2B5F', "Should be 2E2B5F"
    assert hex('violet')=='8B00FF', "Should be 8B00FF"
    print('success!')