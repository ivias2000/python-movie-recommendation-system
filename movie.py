
## Start of Programming
feature1 = 33
feature2 = "M"
feature3 = "I"

ages = [0, 16, 35, 50]
gender = ['M', 'F']
m_or_s = ['I', 'II']

# Method 1:
if (feature1 > ages[0]) and (feature1 < ages[1]):
    if feature2 == gender[0]:
        if feature3 == m_or_s[0]:
            out = "'Coco'"
        elif feature3 == m_or_s[1]:
            out = "'Stranger things'"
        else:
            print("Please enter a valid type.")
        
    elif feature2 == gender[1]:
        if feature3 == m_or_s[0]:
            out = "'Frozen'"
        elif feature3 == m_or_s[1]:
            out = "'Madrese moushha'"
        else:
            print("Please enter a valid type.")
    else:
        print("Please enter a valid gender.")
elif (feature1 > ages[1]) and (feature1 < ages[2]):
    if feature2 == gender[0]:
        if feature3 == m_or_s[0]:
            out = "'Fight club'"
        elif feature3 == m_or_s[1]:
            out = "'Peacky blinders'"
        else:
            print("Please enter a valid type.")
        
    elif feature2 == gender[1]:
        if feature3 == m_or_s[0]:
            out = "'Titanic'"
        elif feature3 == m_or_s[1]:
            out = "'Friends'"
        else:
            print("Please enter a valid type.")
    else:
        print("Please enter a valid gender.")
elif (feature1 > ages[2]) and (feature1 < ages[3]):
    if feature2 == gender[0]:
        if feature3 == m_or_s[0]:
            out = "'Its a wonderful life'"
        elif feature3 == m_or_s[1]:
            out = "'Fargo'"
        else:
            print("Please enter a valid type.")
        
    elif feature2 == gender[1]:
        if feature3 == m_or_s[0]:
            out = "'Gone with the wind'"
        elif feature3 == m_or_s[1]:
            out = "'Shahrzad'"
        else:
            print("Please enter a valid type.")
    else:
        print("Please enter a valid gender.")
else:
    print("Please enter a valid age.")

print("See " + out + " and enjoy your time.")

