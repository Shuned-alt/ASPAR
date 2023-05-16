#!/usr/bin/env python
# coding: utf-8

# In[12]:

## MAIN
def ASPAR():
    import pandas as pd
    from datetime import datetime, timedelta
    
    # MAIN ASPAR
    
    #`free_timeslot` is a function that takes in a start time, end time, duration, a list of events, 
    # and a list of days. It filters the events by the days of the week specified, sorts them by start
    # time, and then iterates through the events to find a free time slot of the specified duration. 
    # If a free time slot is found, the function returns a list with the value `True`, the start time of 
    # the free slot, and the end time of the free slot. If no free time slot is found, the function returns 
    # a list with the value `False`.

    def free_timeslot(start_time, end_time, duration, events, days):
        # filter events by days of the week
        events = [event for event in events if event['day'] in days]

        # sort the events by start time
        events.sort(key=lambda x: x['start'])

        # initialize the start time for the free slot search
        free_slot_start = start_time

        # iterate through the events to find a free slot
        for event in events:
            if free_slot_start + duration <= event['start']:
                free_slot_end = free_slot_start + duration
                return [True, free_slot_start, free_slot_end]
            else:
                free_slot_start = event['end']
        else:
            if free_slot_start + duration <= end_time:
                free_slot_end = free_slot_start + duration
                return [True, free_slot_start, free_slot_end]
            else:
                return [False]
    
    #`has_consecutive_schedules` is a function that takes in a list of schedules 
    # and checks if there are any consecutive schedules on the same day. It first 
    # checks if the length of the list is less than or equal to 1, in which case 
    # there are no consecutive schedules. It then sorts the schedules by start time 
    # and iterates through the list, checking if the day of the current schedule is the 
    # same as the day of the next schedule and if the end time of the current schedule is 
    # greater than or equal to the start time of the next schedule. If this condition is met, 
    # it returns True, indicating that there are consecutive schedules. If the loop completes 
    # without finding any consecutive schedules, the function returns False.


    def has_consecutive_schedules(schedules):
        if len(schedules) <= 1:
            return False
        sorted_schedules = sorted(schedules, key=lambda x: x["start"])
        for i in range(len(sorted_schedules) - 1):
            if sorted_schedules[i]["day"] == sorted_schedules[i+1]["day"] and \
            sorted_schedules[i]["end"] >= sorted_schedules[i+1]["start"]:
                return True
        return False

    def is_time_available(day, start, end, availability):
        if not isinstance(availability, list) or len(availability) == 0 or not all(isinstance(item, dict) for item in availability):
            return False
        for avail_dict in availability:
            avail_day = avail_dict.get('Day', '').lower()
            avail_start = datetime.strptime(avail_dict.get('StartTime'), '%H:%M')
            avail_end = datetime.strptime(avail_dict.get('EndTime'), '%H:%M')
            #Check day
            if avail_day == "m" or avail_day == "th":
                avail_day = "MTh"
            elif avail_day == "t" or avail_day == "f":
                avail_day = "TF"
            elif avail_day == "w" or avail_day == "s":
                avail_day = "WS"

            if avail_day != day:
                continue
            if start >= avail_start and end <= avail_end:
                # The requested time range is completely within the available time range
                return True
        # Otherwise, the requested time range overlaps with the available time range
        return False
    
    ## DATA CLEANING 

    # The below code is cleaning and transforming data from a raw course data file. 
    # It reads the data from an Excel file, creates a new dataframe, and iterates over 
    # each row in the original dataframe. For each row, it creates a new row for each 
    # section of the course, with a unique identifier for each section. It also adds the 
    # original course title to a new column called 'name'. 
    # Finally, it drops the 'Sections' column from the new dataframe.
    
    # Data cleaning courses
    course_raw_df = pd.read_excel('data/course_raw_data.xlsx')
    courses_df = pd.DataFrame(columns=course_raw_df.columns)
    # iterate over each row in the original dataframe
    for index, row in course_raw_df.iterrows():
        # get the number of sections for this course
        sections = row['Sections']
        
        # create a new row for each section
        for i in range(1, sections+1):
            # create a copy of the original row
            new_row = row.copy()
            
            # set the 'Sections' value to 1 for each new row
            new_row['Sections'] = 1
            
            # create a unique identifier for each section of each course
            section_id = f"-Sec{i}"
            new_row['Course_Title'] = f"{new_row['Course_Title']}{section_id}"
            
            # add the original Course_Title to a new column called 'name'
            new_row['name'] = row['Course_Title']

            # append the new row to the new dataframe
            courses_df = courses_df.append(new_row, ignore_index=True)

    courses_df.drop('Sections', axis=1, inplace=True)


    # The below code is performing data cleaning on two Excel sheets, 
    # "Authorized Courses" and "Faculty Availability", and merging them 
    # into a single dataframe called "faculty_df". The code converts the 
    # "StartTime" and "EndTime" columns in the "Faculty Availability" sheet 
    # to datetime values, formats them as strings with only the hour and minute 
    # components, and then converts them back to datetime objects. It groups the 
    # "Faculty Availability" sheet by "unique_id" and aggregates the "Day", "StartTime", 
    # and "EndTime" columns into a list of dictionaries. It then merges the two sheets on "unique_id

    #Data cleaning faculty
    # Load the two Excel sheets into separate dataframes
    authorized_courses_df = pd.read_excel('data/faculty_raw_data.xlsx', sheet_name='Authorized Courses')
    faculty_availability_df = pd.read_excel('data/faculty_raw_data.xlsx', sheet_name='Faculty Availability')

    # Specify the format of the datetime string
    date_format = '%H:%M:%S'

    # Convert "StartTime" and "EndTime" columns to datetime values, format them as strings with only the hour and minute components, and then convert them back to datetime objects
    faculty_availability_df['StartTime'] = pd.to_datetime(faculty_availability_df['StartTime'], format=date_format).dt.strftime('%H:%M')
    faculty_availability_df['EndTime'] = pd.to_datetime(faculty_availability_df['EndTime'], format=date_format).dt.strftime('%H:%M')

    # Group the faculty_availability_df by masked_id and aggregate the day, starttime, and endtime into a list of dictionaries
    grouped_availability_df = faculty_availability_df.groupby('unique_id').apply(lambda x: x[['Day', 'StartTime', 'EndTime']].to_dict('records')).reset_index(name='availability')
    # Merge the two dataframes on masked_id using a left join
    merged_df = pd.merge(authorized_courses_df, grouped_availability_df, on='unique_id', how='left')
    # Replace NaN values in the availability column with an empty dictionary
    merged_df['availability'].fillna({}, inplace=True)
    # Convert the authorized_courses column from a string with comma-separated values to a list
    merged_df['authorized_courses'] = merged_df['authorized_courses'].apply(lambda x: x.split(',') if isinstance(x, str) else [])
    # add a new column "max_units" with the value of 15 for all rows
    merged_df['max_units'] = 15
    # add a new column "schedules" with an empty dictionary for each row
    merged_df['schedules'] = [[] for _ in range(len(merged_df))]
    # rename the dataframe to "faculty_df"
    faculty_df = merged_df


    #The below code is reading an Excel file containing raw data about rooms and 
    # creating a new column called "schedules" with an empty dictionary for each row. 
    # It then renames the resulting dataframe to "rooms_df". 
    
    #Data cleaning rooms
    rooms_raw_df = pd.read_excel('data/room_raw_data.xlsx')
    # add a new column "schedules" with an empty dictionary for each row
    rooms_raw_df['schedules'] = [[] for _ in range(len(rooms_raw_df))]
    # rename the dataframe to "faculty_df"
    rooms_df = rooms_raw_df
    
    #The below code is fixing a bug in the code by ensuring that the 'schedules' column 
    # in both the 'rooms_df' and 'faculty_df' dataframes contains a list. 
    # It does this by using the apply() method to check if the value in each row of the 
    # 'schedules' column is a list, and if not, it replaces it with an empty list.
    #Bugfix
    rooms_df['schedules'] = rooms_df['schedules'].apply(lambda x: x if isinstance(x, list) else [])
    faculty_df['schedules'] = faculty_df['schedules'].apply(lambda x: x if isinstance(x, list) else [])

    # The below code is generating a course schedule by assigning courses to suitable 
    # rooms, timeslots, and faculty members based on various constraints such as course 
    # duration, room occupancy, lab requirements, faculty availability, and authorized courses. 
    # The output is stored in a pandas dataframe and exported to an Excel file.
    #Timeslots
    istart_time = datetime.strptime('7:30', '%H:%M')
    iend_time = datetime.strptime('21:00', '%H:%M')

    #Days 
    days = ['MTh', 'TF', 'WS']

    # Initialize output dataframe
    output_df = pd.DataFrame(columns=['Course', 'Room', 'day', 'start_time', 'end_time', 'Faculty'])

    # Loop through courses
    for i, course in courses_df.iterrows():
        
        # Determine course duration based on units and need_lab
        if course['units'] == 3 and course['need_lab'] == 1:
            duration = timedelta(hours=2.5)
        elif course['units'] == 4 and course['need_lab'] == 0:
            duration = timedelta(hours=2)
        else:
            duration = timedelta(hours=1.5)
        
        # Loop through Rooms
        for j, room in rooms_df.iterrows():
            
            # Check if if room is suitable for course based on max occupancy and need_lab
            if (course['max_occupancy'] <= room['max_occupancy']) and (course['need_lab'] == room['is_lab']):

                # Find timeslot
                for day in days:

                    if free_timeslot(istart_time, iend_time, duration, room['schedules'], day)[0]:
                        
                        # Set timeslot and add in room schedules
                        start_time = free_timeslot(istart_time, iend_time, duration, room['schedules'], day)[1]
                        end_time = free_timeslot(istart_time, iend_time, duration, room['schedules'], day)[2]
                        new_schedules = {'day': day, 'start': start_time, 'end': end_time}
                        rooms_df.at[j, "schedules"].append(new_schedules)

                        # Loop through faculty
                        for k, faculty in faculty_df.iterrows():
                            
                            # Check if faculty is available and can teach the course
                            if course['units'] <= faculty['max_units'] and course['name'] in faculty['authorized_courses'] and free_timeslot(start_time, end_time, duration, faculty['schedules'], day)[0] and not has_consecutive_schedules(faculty['schedules']) and is_time_available(day, start_time, end_time, faculty["availability"] ):
                                # Assign course to room, timeslot, and faculty
                                faculty_df.at[k, 'max_units'] -= course['units']  # Directly update the value in faculty_df
                                faculty_df.at[k, 'schedules'].append(new_schedules)
                                output_df = output_df.append({'Course': course['Course_Title'], 'Room': room['room_number'], 'day':day, 'start_time': start_time.strftime("%H:%M"), 'end_time': end_time.strftime("%H:%M"), 'Faculty': faculty['unique_id']}, ignore_index=True)
                                break  # Only assign one faculty member per course
                            
                        else:  # No suitable faculty found
                            output_df = output_df.append({'Course': course['Course_Title'], 'Room': room['room_number'], 'day':day,'start_time': start_time.strftime("%H:%M"), 'end_time': end_time.strftime("%H:%M"), 'Faculty': "No faculty available"}, ignore_index=True)
                        break  # Only assign one faculty member per course

                else:
                    continue
                break  # Only assign one timeslot per course
        else:  # No suitable room found
            output_df = output_df.append({'Course': course['Course_Title'], 'Room': 'No room available', 'day':'No day available','start_time': 'No time available', 'end_time': 'No time available', 'Faculty': "No faculty available"}, ignore_index=True)
            
    #Export output into a csv file
    from pathlib import Path  
    filepath = Path('output/course_schedule.xlsx')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    output_df.to_excel(filepath)  

    return

# %%
