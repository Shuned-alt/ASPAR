# ASPAR
ASPAR: ACADEMIC SCHEDULE PLANNING AUTOMATED RECOMMENDER SYSTEM MANUAL (v1.2)

This Python-based system aims to assign courses to rooms and faculty members based on their availability and specific criteria such as room capacity, course duration, and faculty availability. The script takes input data from Excel files containing information about courses, rooms, and faculty members.

Requirements:
The system is designed to run on Windows and can run on minimum computer specifications. The installer will install all the dependencies needed to run the software.


Data requirements for uploads:
The excel files that the user will input into the system (The column names must be the same!):

Course data:
- Course_Title (i.e, GED0101, APM0101)
- Sections (i.e, 10)
- need_lab (True or False)
- units (i.e, 3)
- max_occupancy (i.e., 40)

Room data:
- room_number (Room 101, Room 102)
- max_occupancy (Maximum occupancy of the room i.e., 40)
- is_lab (True, or False)

Faculty data:
Authorized Courses (sheet title)
- unique_id (id of the faculty)
- authorized_courses (a list of courses that faculty is allowed to teach)
Faculty Availability (sheet title)
- unique_id (id of the faculty)
- Day (Day that the faculty is available)
- StartTime (Start time that the faculty is available)
- EndTime (End time that the faculty is available)

How to install the program:
Simply run the installer provided. User’s experience will be better if the software is installed in an easily accessible folder i.e., Documents folder. 

How to use the program:

1. After installing the software, run the program either from the shortcut you opted to create or by simply searching “ASPAR” in the search tab.
2. At the main screen, the user will have to upload the needed files for the system via the buttons named “Upload *” where * is the required file to be uploaded. The files should be uploaded accordingly. Any mistake will lead the system to fail. 
3. After all the files are uploaded the user can run the program by simply pressing the button “Run Program”
4. A window will pop-up telling the user to that the script is running and it should not be closed. Closing this window will not terminate the program but it will be very hard for the user to know whether the program has finished or not. 
5. After the script has finished running, the user should check the ‘output’ folder in the install location of the program. 

Troubleshooting:
Not finding the install location/shortcut: 
- For this you can search ‘ASPAR’ in the search tab and it will show the app.

Uploaded the wrong file into the wrong upload button:
- For this just terminate the program and run it again. 

Closed the “Script is running” window:
- The window is only there for the user to know what is happening. If the user closes this the program will still run but the user will not know whether the script is still running or not.

Uploaded the correct data but output is not as intended:
- Double check the data being uploaded and cross-reference it to the data requirements shown above.
