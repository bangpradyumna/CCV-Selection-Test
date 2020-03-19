# CCV-Selection-Test

## Ingesting xml data into sqlite database
Use the function "parse_and_store_xml" in ccv_app/views.py
This will parse post data from "bioinformatics_posts_se.xml" and will create an instance of Post model for each post.

## Endpoint for Posts
After starting developement server, Navigate to http://127.0.0.1:8000/api/posts/ to get all the posts sorted by creation_date. In case you 
want posts to be ordered according to score or comment_count then navigate to http://127.0.0.1:8000/api/posts/?sort_by=YOUR_SORTING_PARAM

## Endpoint for Search
After starting developement server, Navigate to http://127.0.0.1:8000/api/search/?search=YOUR_SEARCH_TERM and replace YOUR_SEARCH_TERM with the term you are searching for. 
