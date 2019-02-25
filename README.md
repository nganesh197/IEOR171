# IEOR171_Project2
Our IEOR 171 Project 2, Instattend, focuses on the creation of a BETTER attendance taking device than what is currently offered in the marketplace. We take a social aspect of participation, using Instagram, and use it to account for students in the classroom. Or to put it simply, "making taking attendance fun again" 

Our solution DOES NOT require a TA/GSI/Professor to download, store, upload any software. The only thing required is a Google Drive account (a tool given to most, if not all, universities). Files can be retrieved by Instattend's software team for verification of attendance. 

Backend: Instattend uses instagram-scraper, Google Sheets API, and related functions that will be mentioned below

instagram-scraper: allows Instattend to pull data from Instagram back to Earth. A folder is created with all data collected across the accounts specificied 

main_v2.py: is the central program that pulls together all the data, functions, and apis. First, it will look throught the directory of someone's computer, specifically for certain files and compile a list of the paths. These file paths are created once instagram-scraper has run. Next, the program will parse through these files and pull out the captions and timestamp of the post. 
