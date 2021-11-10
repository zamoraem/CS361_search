# CS361 Assignment 7: Microservices Integration
# Author: Elaine Zamora
# Date: 11/10/2021
# 

import sys
import argparse
import json
import demjson
import requests
import wikipedia
import pullSaidImage as pi

url = "https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search="

# ------------------------
def join_words(words):
    """ This takes list of words entered by the user and reformats it 
        separated by "_" where wordX is a word entered and X is the Xith
        word in the list: word1_word2_word3
    """
    search_q = "_".join(words)
    return search_q


def display_info(words):
    """
        Takes as input a query and writes result to a text file named search_result.txt
        Uses Wikipedia to search and return a summary of text related to search query
        """
    # join query words separated by underscore to append to url
    query_name = join_words(words)

    # search wikipedia, parse data, and write summary to search_result.txt
    summary = wikipedia.summary(query_name)

    #create dictionary to store results for user to access
    r_dict = {'name':query_name, 'summary':summary}

    # pull image and attach url to r_dict with key: 'image'
    search_term = " ".join(words)
    image_list = get_image(search_term)
    # attach to dictionary  here *****  TODO 
    r_dict["Images"] = image_list


    # write results of name, summary, image to json outfile
    with open("search_result.txt", "w") as outfile:
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



if __name__ == "__main__":
    # Note: The following can be utilized via CLI with search terms 
    # immediately after the filename separated by spaces
    arg = sys.argv
    display_info(arg[1:])
    
    # Note: You can use the following to simply call the function with search terms as args
    #     : user query must be entered with spaces between terms
    # user_query = 'Nelson Mandela'
    # display_info(user_query)