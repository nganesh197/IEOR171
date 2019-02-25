# IEOR171_Project2
Our IEOR 171 Project 2, Instattend, focuses on the creation of a BETTER attendance taking device than what is currently offered in the marketplace. We take a social aspect of participation, using Instagram, and use it to account for students in the classroom. Or to put it simply, "making taking attendance fun again" 

Our solution DOES NOT require a TA/GSI/Professor to download, store, upload any software. The only thing required is a Google Drive account (a tool given to most, if not all, universities). Files can be retrieved by Instattend's software team for verification of attendance. 

Backend: Instattend uses instagram-scraper, Google Sheets API, and related functions that will be mentioned below

instagram-scraper: allows Instattend to pull data from Instagram back to Earth. A folder is created with all data collected across the accounts specificied 

main_v2.py: is the central program that pulls together all the data, functions, and apis. First, it will look throught the directory of someone's computer, specifically for certain files and compile a list of the paths. These file paths are created once instagram-scraper has run. Next, the program will parse through these .json files and pull out the captions and timestamp of the post. This data will then be formatted and combined based on timestamps into a specific format. This data is then parsed once more and updates to the Google Sheet. Lastly, the Google Sheet is customize to format when data is inputted. 

formatarr.py: main file of all the functions that main_v2.py will use. I did this to ensure that all functions are executed properly and to have a cleaner main_v2.py file. This file splits the caption array to those present and absent (also removing those words) and then splitting the results further to individual names (firstname lastname). There is also a function that sorts all the arrays by dates and combines them in one array. Lastly, there is a function that creates blanks specifically on the absent side (needed for when uploading data to Google Sheets).

findjson.py: Looks through a computer's directory to find the correct json files. This allows the user to store the json file in more general areas of the computer or of a folder. 

readjson.py: Reads each .json file and removes the captions and timestamps. The way that Instagram and the instagram-scraper formats the data into .json makes it difficult to parse through and analyse using Python. 


