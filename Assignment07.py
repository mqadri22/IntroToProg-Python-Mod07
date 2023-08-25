# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Script to demonstrate pickling and error handling
#   via handling and processing of airplane flight data
# ChangeLog (Who,When,What):
# MQadri,8.22.2023,Wrote code to complete assignment 07
# ---------------------------------------------------------------------------- #

import pickle       # import pickle for pickling
import os.path      # import os.path for file path handling

# Data ---------------------------------------------------------------------- #
# Declare and load variables and constants

fileName = "C:\\_PythonClass\\Assignment07\\flight_data.txt"    # create string object pointing to data text file
# fileName = "flight_data.txt"                                  #   use if not using command window
binaryFile = "C:\\_PythonClass\\Assignment07\\flightData.dat"   # create string object pointing to target binary file
# binaryFile = "flightData.dat"                                 #   use if not using command window

# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    # class to handle presentation of menus and retrieving of user response to menus

    @staticmethod
    def main_menu_tasks():
        """ Display a main menu of choices to the user

        :return: nothing
        """
        print('''
                Menu of Options
                1) Display flight data
                2) Export flight data
                3) Import flight data
                4) Analyze flight performance
                5) Exit Program
                ''')                            # displays a menu of options to the user
        print()                                 # adds a line for looks

    @staticmethod
    def main_menu_choice():
        """ Gets the main menu choice from a user

        :return: (string)
        """
        choice = str(input("Which option would you "
                           "like to perform? [1 to 5] - ")).strip()  # prompt user selection from menu options
        print()                                                      # adds a line for looks
        return choice                                                # return user choice as variable output

    @staticmethod
    def perf_menu_tasks():
        """ Displays a menu of performance analyses for the user to choose from

        :return: nothing
        """
        print('''
                        Performance Analyses
                        1) Calculate flight time
                        2) Calculate maximum climb rate       
                        3) Return to Main Menu
                        ''')                            # displays a menu of options to the user
        print()                                         # adds a line for looks

    @staticmethod
    def perf_menu_choice():
        """ Gets the performance analysis menu choice from a user

        :return: (string)
        """
        choice = str(input("Which analysis would you "
                           "like to perform? [1 to 3] - ")).strip()     # prompt user selection from menu options
        print()                                                         # add a line for looks
        return choice                                                   # return user choice as variable output

# Processing  --------------------------------------------------------------- #

class Processor():
    # class to handle processing for data (loading, pickling, unpickling, display, analysis)

    @staticmethod
    def loadDataFromFile(file_name):
        """ This function loads data from a file into a list table, converting any string numbers to floats

        :param file_name: (string) name of a file to extract data from
        :return: (list) list object containing data extracted from file
        """
        try:                                                                # try
            targetFile = open(file_name, "r")                               #   opening a text file with read permissions
            outputData = targetFile.readlines()                             #   read each line from the text file into a list
            for idx, row in enumerate(outputData):                          #   for each row of the list
                outputData[idx] = row.split(",")                            #       split that row into a list
                for idx2, elem in enumerate(outputData[idx]):               #       for each element in the new list row
                    if elem.isnumeric():                                    #           if the element is numeric
                        outputData[idx][idx2] = float(elem)                 #               make it a float
                    else:                                                   #           if it isn't numeric
                        outputData[idx][idx2] = elem.strip()                #               keep it as a string, but strip it
            return outputData                                               #   return output as variable
            # print(outputData)
        except FileNotFoundError:                                                                           # if the file can't be found and thus not opened
            print(file_name, " does not exist. Building empty file... ")                                    #   inform the user
            outputData = []                                                                                 #   initialize a list that will eventually be output
            header = "ID,Time [s],Phase,Alt [ft],Pitch [deg],Roll [deg],Yaw [deg],AOA [deg],Speed [ft/s]"   #   create a header for the data
            outputData.append(header.split(","))                                                            #   split the header into a list object and append as first row of output
            numel = 11                                                                                      #   pick a random number of rows to add
            for idx in range(1, numel):                                                                     #   for the random number of rows decided to add above
                ID = idx                                                                                    #       set the ID flight parameter to the row number
                t = 5.0 * idx                                                                               #       set the time to 5.0 sec * row number (5 sec per data point)
                phase = "Static"                                                                            #       set the phase to Static (plane not moving)
                params = [0.0] * 6                                                                          #       create list of zeros for other 6 flight parameters
                row = [ID, t, phase]                                                                        #       create a list from the first 3 flight parameters
                row.extend(params)                                                                          #       extend the list to include the 0s for the other flight parameters
                outputData.append(row)                                                                      #       append the list to the output list
            return outputData                                                                               #       return the list as an output variable

    @staticmethod
    def exportBinaryData(file_name="exportedData.dat", exportData=[]):
        """ This function pickles list data and exports it to a binary file

        :param file_name: (string) name of binary file to export pickled data to
        :param exportData: (list) list object to be pickled and exported to a binary file
        :return: nothing
        """
        print("Exporting data to ",file_name,"...\n")       # inform user that data is being exported (pickled and saved)
        targetFile = open(file_name,"ab")                   # open a dat file with append binary permissions
        pickle.dump(exportData,targetFile)                  # pickle and dump the data into that dat file
        targetFile.close()                                  # close the file
        print("Data successfully exported to ",file_name)   # inform the user that data was exported (pickled and saved)

    @staticmethod
    def importBinaryData(file_name):
        """ This function reads in data from a binary file and unpickles it

        :param file_name: (string) name of a binary data file to unpickle
        :return: (list) - list object containing unpickled data
        """
        ###
        if os.path.isfile(file_name):                                                           # use os.path to check if the specified file exists
            print("Importing data from ",file_name,"... \n")                                    #   if it does, inform user that data is being imported (unpickled)
            outputData = []                                                                     #   initialize list object to receive unpickled data
            targetFile = open(file_name,"rb")                                                   #   open a binary dat file with read permissions
            outputData = pickle.load(targetFile)                                                #   unpickle and load data from binary dat file into list object
            targetFile.close()                                                                  #   close the binary dat file
            print("Data imported from ",file_name,". Returning to main menu... \n")             #   inform user that unpickling has been completed
            return outputData                                                                   #   return list as output variable
        else:                                                                                   # if specified file does not exist
            print("No binary file named "+file_name+" exists. Returning to main menu... \n")    #   inform user that the file does not exist

    @staticmethod
    def analyzePerformance(option,inputData):
        """ This function reads in a user selected option and then performs
        corresponding analysis on selected data, finally displaying results

        :param option: (string) user-selected option from a menu determining type of analysis
        :param inputData: (list) list containing data to be analyzed
        :return: nothing
        """
        phase_column = None                             # initialize variable to check what column Phase is
        alt_column = None                               # initialize variable to check what column Alt [ft] is
        time_column = None                              # initialize variable to check what column Time [s] is
        for idx, elem in enumerate(inputData[0]):       # for each element in the header
            if elem.lower() == "Alt [ft]".lower():      #   if the element is "Alt [ft]"
                alt_column = idx                        #       update corresponding variable with the column number
            elif elem.lower() == "Time [s]".lower():    #   if the element is "Time [s]"
                time_column = idx                       #       update corresponding variable with column number
            elif elem.lower() == "Phase".lower():       #   if the element is "Phase"
                phase_column = idx                      #       update corresponding variable with column number

        # Calculate Flight Time
        if option == "1":                                                                           # if the user elected to calculate flight time
            takeoff_check = None                                                                    #   initialize variable to check if plane took off
            landing_check = None                                                                    #   initialize variable to check if plane landed
            takeoff_time = None                                                                     #   initialize variable to record when plane took off
            landing_time = None                                                                     #   initialize variable to record when plane landed
            if not(phase_column is None):                                                           #   if a column titled Phase exists
                for idx, row in enumerate(inputData):                                               #       for each row in the list table
                    if row[phase_column].lower() == "Takeoff Roll".lower():                         #           if the Phase in that row is Takeoff
                        takeoff_check = True                                                        #               update variable to record that plane took off
                        takeoff_time = row[time_column]                                             #               update variable to record time that plane took off
                for idx2, row in enumerate(reversed(inputData)):                                    #       for each row in reversed list table
                    if row[phase_column].lower() == "Landing Roll".lower():                         #           if the Phase in that row is Landing
                        landing_check = True                                                        #               update variable to record that plane landed
                        landing_time = row[time_column]                                             #               update variable to record time that plane landed
                try:                                                                                #       try checking if plane didn't land or didn't take off
                    if takeoff_check is None or landing_check is None:                              #           if it didn't do one and/or the other,
                        raise Exception                                                             #               raise exception
                    flight_time = landing_time - takeoff_time                                       #           subtract take off time from landing time to calculate duration
                    print("Flight time = %.2f s" % flight_time)                                     #           tell the user the flight duration
                except:                                                                             #       if the plane didn't land and/or take off
                    if takeoff_check is None and landing_check is None:                             #           if it didn't do either
                        print("The plane never took off or landed. Flight time = 0 s \n")           #               tell the user the plane never flew
                    elif takeoff_check is None:                                                     #           if it didn't take off
                        print("The plane never took off, but landed. Data unintelligible \n")       #               tell the user the data is faulty
                    elif landing_check is None:                                                     #           if it didn't land
                        print("The plane took off but never landed. Data unintelligible \n")        #               tell the user the data is faulty
            else:                                                                                   #   if no column titled Phase exists
                print("Data is partial or missing. Returning to main menu...")                      #       tell user data is faulty

        # Calculate Max Climb Rate
        elif option == "2":                                                                 # if user elected to calculated maximum climb rate
            max_climb_rate = 0                                                              #   set max climb rate to 0
            if not(alt_column is None or time_column is None):                              #   if columns titled Alt [ft] and Time [s] exist
                for idx2, row in enumerate(inputData):                                      #       for each row in list table
                    try:                                                                    #           try to see if the climb rate can be calculated
                        climb_rate = (row[alt_column]-inputData[idx2-1][alt_column])/\
                                     (row[time_column]-inputData[idx2-1][time_column])      #               if it can, calculate climb rate (change in Altitude/change in Time)
                        if climb_rate > max_climb_rate:                                     #               check if climb rate is higher than current recorded max
                            max_climb_rate = climb_rate                                     #                   if higher, updated recorded max
                    except ZeroDivisionError:                                               #           if climb rate calculation causes divide by zero error
                        None                                                                #               move on
                    except TypeError:                                                       #           if climb rate calculation causes type error
                        None                                                                #               move on
                print("\n The maximum climb rate is %.2f ft/s \n" % max_climb_rate)         #       tell the user the maximum climb rate
            else:                                                                           #   if either Alt [ft] or Time [s] do not exist in the header
                print("Data is partial or missing. Returning to main menu...")              #       tell the user the data is faulty

        # Return to Main Menu
        elif option == "3":                         # if the user elects to return to the main menu
            print("Returning to Main Menu... \n")   #   tell the user that they are being returned to the main menu

        else:                                                           # if the user entered some other option
            print("Invalid selection. Returning to Main Menu... \n")    #   tell the user their selection was invalid
        print()                                                         # add a line for looks

    @staticmethod
    def displayListData(inputList):
        """ This function displays data from a list object in a readable format

        :param inputList: (list) list to be displayed
        :return:
        """
        print("\n----------This is your current data-----------\n")     # tell the user they are about to see the current data
        for row in inputList:                                           # for each row in the list table
            print("|".join(map(str,row)))                               #   print a concatenated string of the list row elements
        print("\n-----------------------------------------------\n")    # add a footer at the end

# Main Body of Script  ------------------------------------------------------ #

flight_data = Processor.loadDataFromFile(file_name=fileName)                        # load in the flight data from a text file at the beginning

while (True):                                                                       # initiate while loop that iterates until user elects to exit (break)

    IO.main_menu_tasks()                                                            #   display the main menu to the user
    str_main_choice = IO.main_menu_choice()                                         #   retrieve and record user selection from main menu

    if str_main_choice.strip() == "1":                                              #       if user elects to display data
        Processor.displayListData(flight_data)                                      #           display data
    elif str_main_choice.strip() == "2":                                            #       if user elects to export (pickle and save) flight data
        Processor.exportBinaryData(file_name=binaryFile,exportData=flight_data)     #           export (pickle and save) flight data
    elif str_main_choice.strip() == "3":                                            #       if user elects to import (unpickle and load) flight data
        unpickledData=Processor.importBinaryData(file_name=binaryFile)              #           import (unpickle and load) flight data
        if not(unpickledData is None):                                              #           if unpickled data is not invalid
            flight_data=unpickledData                                               #               overwrite existing data with unpickled data
    elif str_main_choice.strip() == "4":                                            #       if user elects to analyze performance
        IO.perf_menu_tasks()                                                        #           display performance analysis menu
        str_perf_choice = IO.perf_menu_choice()                                     #           retrieve and record user response to performance analysis menu
        Processor.analyzePerformance(str_perf_choice,inputData=flight_data)         #           perform corresponding analysis
    elif str_main_choice.strip() == "5":                                            #       if the user elects to exit the program
        print("Exiting Program. Goodbye. ")                                         #           tell the user the program is terminating
        break                                                                       #           end the program via breaking the while loop
    else:                                                                           #       if the user selected some other option
        print("Invalid selection. Returning to main menu... \n")                    #           tell the user their selection is invalid
