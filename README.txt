Welcome to Wikipedia search term microservice.

INPUT: To use this microservice via CLI, please run search.py with your search
		terms (separated by spaces) following the filename. To use the 
		functions within search.py please use the following format where 
		'Nelson Mandela' is the desired search term:
					user_query = 'Nelson Mandela'
					display_info(user_query)


OUTPUT: To access results of your search query, please visit search_result.txt
		The result will be stored in JSON format with the following key:value pairs:
			'name':		corresponds to the entered search terms
			'summary':	contains a text string that describes a Wikipedia 
						summary resulting from user's search term(s)
