# ASPAR
ASPAR: ACADEMIC SCHEDULE PLANNING AUTOMATED RECOMMENDER SYSTEM (v1.3)

This Python-based system aims to assign courses to rooms and faculty members based on their availability and specific criteria such as room capacity, course duration, and faculty availability. The script takes input data from Excel files containing information about courses, rooms, and faculty members.

Features:
Automatically map courses to available rooms and their respective time slots as well as tag available faculty.
Outputs an Excel file where it has the course, the room assignment and its respective time slot for the week, and a tagged faculty if possible.
The program will note if there are no available rooms for the course.
The program will note if there are no available teachers for the course.
The program only has functionality for the following constraints:
One room and timeslot per section.
One faculty per section.
Using proper room assignments for lab requirements.
Room assignments that can accommodate the max number of students per section
The maximum number of units a faculty can be assigned to.
No faculty should be assigned 3 schedules in a row.
Faculty cannot be assigned into schedules where they are not available.
The program strictly needs the correct data listed in the data requirements.

Functionality:
The code is an implementation of an academic scheduling problem, where a schedule is generated for different courses, rooms, and faculties based on their respective schedules, capacities, and availability. 
The function ASPAR() loads datasets of courses, rooms, and faculties, iterates over each course, and assigns it to a suitable room, timeslot, and faculty member, if available.
The function defines two helper functions:
free_timeslot() to find a free slot for a course given a start and end time, course duration, and room schedule.
has_consecutive_schedules() to check if a faculty member has two consecutive schedules on the same day.
is_time_available() to check if the faculty’s availability can accommodate the scheduled time slot for the course.

The function then cleans the input datasets into the proper features to be used in the mapping algorithm. 
The function then initializes the output dataframe and loops through each course then assigns the proper duration of the course based on the units and the lab requirement of the course 
Then the function loops through each room and finds a proper room based on the lab requirements and the max occupancy for the course section. 
Then it loops through the faculty to assign a faculty that can teach the course and has an available schedule.
The code assigns only one faculty member per course, and the output is appended to the output dataframe. 
If a suitable faculty member is not available, the course is assigned to "No faculty available," and if a suitable room is not available, the course is assigned to "No room available." 
The output of the program is an Excel file of the output dataframe.

Requirements:
The system is designed to run on Windows and can run on minimum computer specifications. The installer will install all the dependencies needed to run the software.

Upload requirements:
Data requirements for uploads (see sample data here: https://imgur.com/a/OyOg5Lu):
The data the user will input into the system (The column name must be the same!):

Course data:
Course_Title (i.e, GED0101, APM0101)
Sections (i.e, 10)
need_lab (True or False)
units (i.e, 3)
max_occupancy (i.e., 40)

Room data:
room_number (Room 101, Room 102)
max_occupancy (Maximum occupancy of the room i.e., 40)
is_lab (True, or False)

Faculty data:
Authorized Courses (sheet title)
unique_id (id of the faculty)
authorized_courses (a list of courses that faculty is allowed to teach)
Faculty Availability (sheet title)
unique_id (id of the faculty)
Day (Day that the faculty is available)
StartTime (Start time that the faculty is available)
EndTime (End time that the faculty is available)

The program will then clean the uploaded data into the following:

Course data:
Course Title (Title of the course i.e., GED0101, GED0102)
Name (Name of the course including the section i.e., GED0101-LEC-Sec1-MN)
Units (Number of units)
Laboratory Requirement (True, or False)
Max Occupancy (i.e., 40)
Room data:
Room Number (Room 101, Room 102, based on the Master List)
Max Occupancy (Maximum occupancy of the room i.e., 40)
Laboratory Requirement (True, or False)
Schedules (To be added automatically by the system)
Faculty data:
School IDs (List of school IDs of the faculty)
Department (Department of the faculty i.e., MATHEMATICS)
List of Course Titles the faculty can teach 
Maximum number of units a faculty can be assigned to (i.e., 40)
Schedules (To be added automatically by the system)

How to install the program:
Simply run the installer provided. User’s experience will be better if the software is installed in an easily accessible folder i.e., Documents folder. 

How to use the program:
After installing the software, run the program either from the shortcut you opted to create or by simply searching “ASPAR” in the search tab.

At the main screen, the user will have to upload the needed files for the system via the buttons named “Upload *” where * is the required file to be uploaded. The files should be uploaded accordingly. Any mistake will lead the system to fail. 

After all the files are uploaded the user can run the program by simply pressing the button “Run Program”

A window will pop-up telling the user that the script is running and it should not be closed. Closing this window will not terminate the program but it will be very hard for the user to know whether the program has finished or not. 

After the script has finished running, the user should check the ‘output’ folder in the install location of the program. 

Troubleshooting:
Not finding the install location/shortcut: 
For this you can search ‘ASPAR’ in the search tab and it will show the app.
Uploaded the wrong file into the wrong upload button:
For this just terminate the program and run it again. 
Closed the “Script is running” window:
The window is only there for the user to know what is happening. If the user closes this the program will still run but the user will not know whether the script is still running or not.
Uploaded the correct data but output is not as intended:
Double check the data being uploaded and cross-reference it to the data requirements specified above.

Possible improvements:
Have a more flexible data validation system.
Built-in data editor.
Being able to connect to the ACOS system to have the created schedule seamlessly be uploaded.
Having a pipeline within ACOS and NetSuite.

Additional notes:
**Add notes for personal changes in the source code and instructions how to compile the code into the exe and the installer


