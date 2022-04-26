# plassikortittaja
A simple script for automatic table card creation from .csv-files. Needs pandas to funciton. Takes .csv and the file to be created as arguments, for example ```python plassikortittaja.py vappu/ilmo_tekis.csv vappu/tekis_kortit``` would read ```ilmo_tekis.csv``` from the folder ```vappu``` and create ```tekis_kortit.html``` in the same folder. 

To future TKO-äly table party organizers: you get the ilmo-csv data from the bottom of the registration info (https://members.tko-aly.fi/registrations/listParticipantsAdmin/{id}). The resulting html file should be printed and made into table cards. Modify the script according to your registration form by changing the ```DETAIL_COL_IDS``` values, ```DETAIL_COL_SHOW``` values and possibly the ```parseval``` function.
