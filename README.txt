Welcome to Wikipedia search term microservice.

INPUT: To use the search.py microservice please use the following format where 
		'Nelson Mandela' is the desired search term and location refers to the 
		file that you wish your return information to be stored:
					user_query = 'Nelson Mandela'
					display_info(user_query, location)


OUTPUT: To access results of your search query, please visit your file at user-specified location
		The result will be stored in JSON format with the following key:value pairs:
			'name':		corresponds to the entered search terms
			'summary':	contains a text string that describes a Wikipedia 
						summary resulting from user's search term(s)

ERROR: If an invalid search term (e.g. misspelling, not searchable term) is entered, 'summary' will be set to NULL.
