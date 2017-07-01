def createDatabase():
    """
    This code asks for a user input and converts the contents of the text file into a list
    :return: 
    """
    filename = input('Enter name of file: ')
    infile=open(filename,'r')
    contents=infile.readlines()
    infile.close()

    data=[]
    # this loop is being used to index the given text file according to certain headings
    for i in range (len(contents)):
        dataStr=contents[i]
        dataList = dataStr.split(',')
        dataList[0] = str(dataList[0])
        dataList[1] = str(dataList[1])
        dataList[2] = str(dataList[2])
        dataList[3] = float(dataList[3])
        data.append(dataList)

    return data


def DisplayMenu():
    """
    Function to display as a user interface
    :return: 
    """
    print('1. Print List of CDs')
    print('2. Sort CDs by Title')
    print('3. Sort CDs by Artist')
    print('4. Sort CDs by Genre')
    print('5. Sort CDs by Price')
    print('6. Find All CDs by Title')
    print('7. Find All CDs by Artist')
    print('8. Find All CDs by Genre')
    print('9. Find All CDs by Price at Most X')
    print('10. Quit')


def PrintList(data):
    """
    Function to display the result
    :param data: 
    :return: 
    """

    for i in range(len(data)):
        print('Title- ' +str(data[i][0])+', '+ 'Artist- ' + str(data[i][1])+', '+'Genre- '+ str(data[i][2])+', '+'Price- '+ str(data[i][3]))

def SortByTitle(data):
    """
    Function to sort the list according to the title
    :param data: 
    :return: 
    """

    for i in range (len(data)-1):
        minIndex = i
        title = data[minIndex][0]
        artist= data[minIndex][1]
        genre= data[minIndex][2]
        price = data[minIndex][3]
        for j in range(i+1, len(data)):
            if title > data[j][0]:
                title = data[j][0]
                artist = data[j][1]
                genre = data[j][2]
                price = data[j][3]
                minIndex = j

        tempTitle = data[i][0]
        tempArtist=data[i][1]
        tempGenre=data[i][2]
        tempPrice=data[i][3]
        
        data[i][0]= title
        data[i][1]=artist
        data[i][2]=genre
        data[i][3]=price
        data[minIndex][0] = tempTitle
        data[minIndex][1]=tempArtist
        data[minIndex][2]=tempGenre
        data[minIndex][3]=tempPrice
        print(str(data[i][0])+', '+str(data[i][1])+', '+str(data[i][2])+', $'+str(data[i][3]))
    return print(str(data[i][0])+', '+str(data[i][1])+', '+str(data[i][2])+', $'+str(data[i][3]))

                   
def SortByArtist(data):
    """
        Function to sort the list according to the Artist
        :param data: 
        :return: 
        """
    for i in range (len(data)-1):
        minIndex = i
        title = data[minIndex][0]
        artist=data[minIndex][1]
        genre=data[minIndex][2]
        price=data[minIndex][3]
        for j in range(i+1, len(data)):
            if artist > data[j][1]:
                title = data[j][0]
                artist=data[j][1]
                genre=data[j][2]
                price=data[j][3]
                minIndex = j
                
        tempTitle = data[i][0]
        tempArtist=data[i][1]
        tempGenre=data[i][2]
        tempPrice=data[i][3]
        
        data[i][0]= title
        data[i][1]=artist
        data[i][2]=genre
        data[i][3]=price
        data[minIndex][0] = tempTitle
        data[minIndex][1]=tempArtist
        data[minIndex][2]=tempGenre
        data[minIndex][3]=tempPrice
    return data



def SortByGenre(data):
    """
        Function to sort the list according to the genre
        :param data: 
        :return: 
        """
    for i in range (len(data)-1):
        minIndex = i
        title = data[minIndex][0]
        artist=data[minIndex][1]
        genre=data[minIndex][2]
        price=data[minIndex][3]
        for j in range(i+1, len(data)):
            if genre > data[j][2]:
                artist=data[j][1]
                title = data[j][0]
                genre=data[j][2]
                price=data[j][3]
                minIndex = j


        tempTitle = data[i][0]
        tempArtist=data[i][1]
        tempGenre=data[i][2]
        tempPrice=data[i][3]
        
        data[i][0]= title
        data[i][1]=artist
        data[i][2]=genre
        data[i][3]=price
        data[minIndex][0] = tempTitle
        data[minIndex][1]=tempArtist
        data[minIndex][2]=tempGenre
        data[minIndex][3]=tempPrice
    return data


def SortByPrice(data):
    """
        Function to sort the list according to the price
        :param data: 
        :return: 
        """
    for i in range (len(data)-1):
        minIndex = i
        title = data[minIndex][0]
        artist=data[minIndex][1]
        genre=data[minIndex][2]
        price=data[minIndex][3]
        for j in range(i+1, len(data)):
            if price > data[j][3]:
                artist=data[j][1]
                title = data[j][0]
                genre=data[j][2]
                price=data[j][3]
                minIndex = j

        tempTitle = data[i][0]
        tempArtist=data[i][1]
        tempGenre=data[i][2]
        tempPrice=data[i][3]
        
        data[i][0]= title
        data[i][1]=artist
        data[i][2]=genre
        data[i][3]=price
        data[minIndex][0] = tempTitle
        data[minIndex][1]=tempArtist
        data[minIndex][2]=tempGenre
        data[minIndex][3]=tempPrice
    return data



def FindByTitle(data,target):
    """
        Using binary search to find the an album by its title
        :param data: 
        :return: 
        """
    minIndex=0
    maxIndex=len(data)-1
    midIndex=(minIndex+maxIndex)//2
    for midIndex in range (1+maxIndex):
        if data[midIndex][0]<target:
            midIndex=midIndex+1
        elif data[midIndex][0]>target:
            midIndex=midIndex-1
        elif data[midIndex][0]==target:
            print(data[midIndex])
            midIndex=midIndex+1
        
    return target                                 
	          

def FindByArtist(data,target):
    """
           Using binary search to find the an album by its artist
           :param data: 
           :return: 
           """
    minIndex=0
    maxIndex=len(data)-1
    midIndex=(minIndex+maxIndex)//2
    for midIndex in range (1+maxIndex):
        if data[midIndex][1]<target:
            midIndex=midIndex+1
        elif data[midIndex][1]>target:
            midIndex=midIndex-1
        elif data[midIndex][1]==target:
            print(data[midIndex])
            midIndex=midIndex+1
        
    return target                                 
	          


def FindByGenre(data,target):
    """
           Using binary search to find the an album by its genre
           :param data: 
           :return: 
           """
    minIndex=0
    maxIndex=len(data)-1
    midIndex=(minIndex+maxIndex)//2
    for midIndex in range (1+maxIndex):
        if data[midIndex][2]<target:
            midIndex=midIndex+1
        elif data[midIndex][2]>target:
            midIndex=midIndex-1
        elif data[midIndex][2]==target:
            print(data[midIndex])
            midIndex=midIndex+1
        
    return target                                 
	          

def FindByPrice(data,target):
    """
           Using binary search to find the an album by its price
           :param data: 
           :return: 
           """
    data=SortByPrice(data)


    minIndex=0
    maxIndex=len(data)-1
   
    for minIndex in range (1+maxIndex):
        if data[minIndex][3]<=(float(target)):
            print(data[minIndex])
            minIndex=minIndex+1
            


def loopFunction(choice):
    """
    This is the main driver function
    :param choice: 
    :return: 
    """
    if choice==1:
        c1=PrintList(data)
        print(c1)
    elif choice==2:
        c2=SortByTitle(data)
        
    elif choice==3:
        c3=SortByArtist(data)
        print(c3)
    elif choice==4:
        c4=SortByGenre(data)
        print(c4)
    elif choice==5:
        c5=SortByPrice(data)
        print(c5)
    elif choice==6:
        target=str(input('Enter The Title Name: '))
        c6=FindByTitle(data,target)
    elif choice==7:
        target=str(input('Enter The Artist Name: '))
        c7=FindByArtist(data,target)
    elif choice==8:
        target=str(input('Enter The Genre: '))
        c8=FindByGenre(data,target)
    elif choice==9:
        target=float(input('Enter The Price: '))
        c9=FindByPrice(data,target)

data=createDatabase()
Menue=DisplayMenu()
while True:
    choice=int(input('Enter Your Choice: '))
    a=loopFunction(choice)
    if choice==10:
        break
    

        
    
        
        
        
    
    



    
