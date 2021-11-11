# CS361 Assignment 7: Microservices Integration
# Author: Elaine Zamora
# Date: 11/11/2021
# 

import sys
import json
import demjson
import requests
import wikipedia
import pullSaidImage as pi


def display_info(words, location):
    """
        Takes as input a query and writes result to a text file named search_result.txt
        Uses Wikipedia to search and return a summary of text related to search query
        """
    to_file = location

   # search wikipedia, parse data, and write summary to search_result.txt
    summary = wikipedia.summary(words)

    #create dictionary to store results for user to access
    r_dict = {'name':words, 'summary':summary}

    # pull image and attach url to r_dict with key: 'image'
    image_list = get_image(words)
    r_dict["Images"] = image_list

    # write results of name, summary, image to json outfile
    with open(to_file, "w") as outfile:
        json.dump(r_dict, outfile)
    outfile.close()


def get_image(search_term):
    """
    Takes as input a search term and returns a url corresponding to an image
    found with the user's query. Uses team member (Laura) microservice
    """
    to_file = 'C:\\Users\\elain\\361\\search\\CS361_search\\TEST_JSON.json'
    pi.pullSaidImage_give(search_term, to_file)
    with open(to_file, 'r') as openfile:
        json_obj = json.load(openfile)
    json_final = demjson.decode(json_obj)
    return json_final


def main():
    # Note: You can use the following to simply call the function with search terms as args
    #     : user query must be entered with spaces between terms
    user_query = 'nelson mandela'
    display_info(user_query, 'C:\\Users\\elain\\361\\search\\CS361_search\\search_result.txt')

if __name__ == "__main__":
        main()