#code made by Laura Elder
# I used the following sources:
#[1] https://www.geeksforgeeks.org/image-scraping-with-python/

import requests
import json
import demjson
from bs4 import BeautifulSoup



def getdata(url): 
    r = requests.get(url)
    return r.text 
    

def pullSaidImage_give(search_term, location):
    #This function takes in a value and returns the URL for that image
    #the "term" is the value you wish to find an image for
    #the "location" is the location that you wish to have the JSON writen at
    #Keep in mind an absolute file path
    #Example 'C:\Users\Laura\' becomes 'C:\\Users\\Laura\\'
    htmldata = getdata("https://www.everypixel.com/search?q="+search_term+"&meaning=&stocks_type=free&media_type=0&page=1") 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    #filename ='C:\\Users\\Laura\\source\\repos\\SoftwareOneWebPage-LauraElderStocks\\images.json'
    filename = location
    with open(filename,'w') as file_object:
        count = 1
        for item in soup.find_all('img'):
            link=(item['src'])
            if count ==1:
                linked = link
                count = 2
            else:
                linked = linked + str(", "+link)
        var = [{"Link": {linked}}]
        newVar=demjson.encode(var)
        json.dump(newVar,file_object)
        #return link
    pass

#def main():
    
#   pullSaidImage_give("blue",'C:\\Users\\Laura\\source\\repos\\SoftwareOneWebPage-LauraElderStocks\\images.json')

#if __name__ == "__main__":
#    main()