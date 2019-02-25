import json, datetime, os, gspread, formatarr as fa
from oauth2client.service_account

wks = gc.open("...").sheet1
for cell in cell_list:
    cell.value = ''

# Update in batch
wks.update_cells(cell_list)


# first part is to find all the directories that have .json
# compiles into an array that can be used later
#dir_path needs to be more specific just to avoid weird inputs
dir_path = os.path.dirname(os.path.realpath('...'))
raw_json = []
json_dir = []
for root, dirs, files in os.walk(dir_path):
	for file in files:
		# finds all files that end with .json
		if file.endswith('.json'):
			raw_json.extend([root.replace("\\", '/') +'/'+str(file)])

#gets us all the files that concern the class
for give in raw_json:
	for take in team_list:
		if take in give:
			json_dir.extend([give])


#goes through each of the json files and obtains the captions and the timestamp
for js in json_dir:
	captions = []
	with open(js, encoding='utf-8-sig') as json_file:
	    json_data = json.load(json_file)
	for i in range(len(json_data)):
	    date_timestamp = datetime.datetime.fromtimestamp(int(json_data[i]["taken_at_timestamp"])).strftime('%m/%d/%Y')
	    captions += [[date_timestamp, json_data[i]["edge_media_to_caption"]["edges"][0]["node"]["text"].lower()]] #no longer case sensitive

	captions = fa.take_all(captions) #formats the array for each data entry using formatarr.py
	dates = fa.starboard(dates, captions)


dates = fa.create_blanks(dates)

#uploads to Google Sheets
date_index = 4 #column B row 4
bstart_index = 6
cstart_index = 6

for d in dates:
	date_cell = ".." + str(date_index)
	wks.update_acell(date_cell, d)
	wks.update_acell((".." + str(date_index+ 1)), "Present")
	wks.update_acell((".." + str(date_index+ 1)), "Absent")


	total_len = len(dates[d][0])

	for pres in dates[d][0]:
		wks.update_acell(".."+ str(bstart_index),pres)
		bstart_index +=1
	for abse in dates[d][1]:
		wks.update_acell(".."+ str(cstart_index), abse)
		cstart_index +=1
	date_index = bstart_index + 15
	bstart_index += 3
	cstart_index += 3
