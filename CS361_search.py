# CS361 Assignment 5: MVP Microservices
# Author: Elaine Zamora
# Date: 10/27/2021
# 

import sys
import argparse
import json
import requests
import wikipedia

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
        Takes as input a query and creates a text file named query_name.txt
        Writes to that file the wikipedia url and information related to query
    
        todo: 1) add error checking for bad wikipedia return results, 
              2) figure out how to write an error to file and update README
        
        """
    # join query words separated by underscore to append to url
    query_name = join_words(words)

    # search wikipedia, parse data, and write summary to search_result.txt
    summary = wikipedia.summary(query_name)
    #print(summary)
    r_dict = {'name':query_name, 'summary':summary}

    with open("search_result.txt", "w") as outfile:
        json.dump(r_dict, outfile)



if __name__ == "__main__":
    arg = sys.argv
    display_info(arg[1:])

