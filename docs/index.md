# Assignment 07 - Files & Exceptions

**Name:**		Mohammed Qadri

**Date:**		2023-08-25

**Course:** 	IT FDN 110 A

**GitHub URL:**	[https://github.com/mqadri22/IntroToProg-Python-Mod07](https://github.com/mqadri22/IntroToProg-Python-Mod07)

**GitHub Site:**	[https://mqadri22.github.io/IntroToProg-Python-Mod07/](https://mqadri22.github.io/IntroToProg-Python-Mod07/)

## Introduction

The objective of Assignment 07 is to gain familiarity with working with files (specifically, binary files) and structured error handling in Python. Unlike previous assignments, Assignment 07 was relatively free form – with the only stipulation being that a script be created demonstrating how pickling (serializing data and saving it in binary format) and structured error handling work.

As the author works in the aerospace industry, it was decided that a script be created that would create, load, pickle (serialize as binary), unpickle (un-serialize from binary), and analyze basic data recorded during a hypothetical airplane flight. The following sections describe the basic structure of the script, how pickling was utilized, and how errors are handled in a structured fashion therein.

## Basic Code Structure

As mentioned previously, this assignment was relatively free form, so no starter file was provided. However, the author elected to use a similar basic structure to previous assignments, namely the separation of concerns.

The script was thus broken into four sections: Data declaration, Presentation (Input/Output), Processing (of data), and the Main Body. Data declaration consists of the declaration of variables that are used in the main body and passed in as arguments to methods in other sections. 

Presentation (Input/Output) consists of methods to display menus to the user and capture their input in response to the menus; these captured inputs are saved as variables in the main body for use in methods from other sections. A custom class “IO” was created to encompass these methods.

Processing consists of methods to process data either stored in memory or persistently in a file. Methods are included for the “import” (unpickling) and “export” (pickling) of data out of or into binary format, respectively. Also contained in Processing are methods to load data at the outset of the script main body and to display data when prompted by the user. Lastly, another method is included to perform rudimentary analyses on the recorded flight data.

The main body of the script consists of a while loop that performs actions based on user response to displayed menus until the user elects to exit. The subsequent sections cover the four sections of the script in more detail.

## Data Declaration

The Data Declaration portion of the script consists of the declaration of variables that will be used later in the script, primarily in the main body. Despite only being called only in the main body of the script, these functions are there passed as arguments for methods defined in other sections.

Before the variables are declared, however, code is imported from two different sets of files: pickle and os.path. pickle is imported to handle the pickling/unpickling portion of the assignment, whereas os.path enables use of methods later on that pertain to file paths. Figure 1 below shows the importation of these two packages.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f01.png "tooltip text")

*Figure 1. Importation of code from other files*

Two variables are declared in the Data Declaration section: fileName and binaryFile. fileName is a string consisting of the name of a txt file containing hypothetical flight parameter data captured by the flight recorder on an airplane during a flight. This data is tabulated with the top row being a header describing the parameters quantified in subsequent rows. This tabulated data can be visualized as seen in Table 1 and Figure 2 below, in table and txt forms.

*Table 1. Tabulated flight data format*

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/t01.png)

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f02.png)

*Figure 2. Hypothetical recorded flight data*

binaryFile is a string containing the name of a file that the user may elect to import binary data from or export binary data to. The serialization of data into binary and de-serialization from binary are covered in the Processing section of the script. Figure 3 below shows how the two variables were declared.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f03.png)

*Figure 3. Declaration of fileName and binaryFile variables*

## Presentation

The presentation portion of the script consists of the “IO” method class. The methods in this class are fairly similar to those in previous assignments, namely Assignments 06 and 05. These methods either present menus to the user or record user responses to these menus. There are two menus in particular that are displayed to the user: the Main Menu and the Performance Analysis menu. The Main Menu provides the user a list of options (import data, export data, analyze data, or exit) whereas the Performance Analysis Menu is a sub-option of the analyze data option where the user can choose what type of analysis to perform on the data. Due to the similarity to previous assignments, these methods are not discussed here in great detail. Figures 4 and 5 below show the menu display and input retrieval methods for both menus.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f04.png)

*Figure 4. Main menu display and user input retrieval methods*

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f05.png)

*Figure 5. Performance analysis menu display and user input retrieval methods*

## Processing

The Processing portion of the script consists of the “Processor” class, which contains methods that “process” data. “Processing” here encompasses the reading of data from a text file (i.e., imagined as received from a flight recorder system, though this more realistically would be a binary file, json, or other), generation of placeholder data if no data exists, pickling of data and export to a file, unpickling of binary data from a file and importation into memory, performance of rudimentary analysis on data in memory, and display of data in memory.

The loading of data from a text file has been accomplished in previous assignments, and is accomplished similarly here – with the exception of structured error handling being introduced. This and other instances of structured error handling are covered in the Structured Error Handling section below, but at a high level this instance handles errors that could emerge from a specific file not being found where expected. Note that the list being created is of mixed data types, which aids in the analysis of the data later on. Figure 6 below shows the method that handles the loading of data (as formatted in previous images) from a text file.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f06.png)

*Figure 6. Method to load data from a text file into a mixed-data-type list for processing*

Serializing of data into binary format and exporting to a file is accomplished via the exportBinaryData function. This function receives two inputs, the name of a target file and data to be serialized, and then proceeds to serialize the data and then save it to the specified target file. The specific mechanics of the pickling are discussed in the Pickling & Unpickling section below. Figure 7 below shows the method that handles the serialization of data into binary and its saving into data.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f07.png)

*Figure 7. Method for data serialization and export*

De-serialization (i.e., “unpickling”) of binary data and importation into memory is accomplished by the importBinaryData function. This method receives one argument, the name of a binary data file from which to import and de-serialize data from. The details of de-serialization are covered in the Pickling & Unpickling section below. Figure 8 below shows the method through which serialized (“pickled”) data is de-serialized (“unpickled”) and imported back into memory.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f08.png)

*Figure 8. Method for data de-serialization and import*

The next method in the Processor class is analyzePerformance, which performs airplane performance analysis on data in list form. The actual analysis performed on the data is rudimentary and not intended to meet the objectives of the assignment. However, structured error handling is incorporated in this method in an attempt to preclude expected errors. This is covered in more detail in the Structured Error Handling section below. Figure 9 below shows analyzePerformance method.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f09.1.png)

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f09.2.png)

*Figure 9. Method to analyze data*

The method to display data from memory is very similar to previous assignments, so is not discussed in detail here. Figure 10 below shows the method that displays data from memory.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f10.png)

*Figure 10. Method to display data from memory*

## Main Body

The main body of the script resembles that of Assignment 06 to an extent. It begins with the loading of data from a text file using a method from the Processor class. Then a while loop is initiated; at the beginning of each iteration, the main menu is displayed to the user and their response is recorded. This recorded response is fed into an if-elif-else statement, through which the correct corresponding method is called and the results produced. The novelty in this script lies in the called functions, which are discussed previously and in the next two sections; thus, no further discussion of the main body is warranted. Figure 11 below shows the main body of the script.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f11.png)

*Figure 11. Main body of script*

## Pickling & Unpickling

As alluded to in the Processing section above, this script makes use of pickling and unpickling (i.e., data serialization and de-serialization). In the theoretical use case for this script, flight parameter data is received in the form of a text file directly from the flight recorder. (In all likelihood such data would already be serialized, but this is ignored here for the purposes of illustration). Unlike the example data provided, real life flight parameter data can consist of hundreds of columns and millions of rows; serialization of such data would thus be useful to reduce file sizes. Figure 2 above shows how tabulated data may be received or generated; for persistent, reduced size storage, it would be useful for this to be serialized as binary data (i.e., “pickled”). Using the code in Figure 7, the data in Figure 2 can be serialized and then saved persistently as a file. Figure 12 below shows the resultant binary data file after the data in Figure 2 is serialized and saved.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f12.png)

*Figure 12. Result of serializing and saving flight data from Figure 2 as binary data*

As expected, the data has been obscured following serialization. As can be seen via the scroll wheel in Figure 12, pickling this small an amount of data isn’t very useful as far as reducing file sizes. But in instances with enormous files (e.g., real airplane flight parameter data), serializing can aid in file size reduction.

If instead serialized data was received for analysis purposes, the importBinaryData shown in Figure 8 can be called to “unpickle” the data and read it into memory, overwriting the existing data object. Figure 13 below illustrates such an example. Here, the initial flight data (see Figure 2) is deleted from the directory. This prompts the program to generate largely empty data (zeros for parameters and Static for flight phase). When the user elects to import data (i.e., “unpickle” and load data), it can be seen that the binary data file has been “unpickled” and passed into the flight data variable. As can be seen in these two examples, pickling and unpickling can be of substantial use in data handling. 

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f13.1.png)

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f13.2.png)

*Figure 13. De-serialization of binary data and loading into memory for processing*

## Structured Error Handling

Structured error handling is utilized in a few instances throughout the script. It is first used in the loadDataFromFile method in the Processor class (see Figure 6). In this case, structured error handling is used in the event that no file of the specified name can be found in the same folder. Attempting to open a non-existent file with read permissions would generate a FileNotFoundError exception. To preclude the premature shutdown of the program, an exception is made in the method whereby a FileNotFoundError would prompt the program to generate a placeholder data table list populated by zeros (see beginning of Figure 13). 

Structured error handling is again used in the performance analysis method (analyzePerformance) in the Processor class. The first instance arises when the user elects to calculate flight time. If it is determined that airplane never took off and/or never landed, then the flight time calculation would yield a TypeError due to a one or more non-numbers being subtracted from each other. Depending on which case (never took off and/or never landed), an exception is raised via the testing of a variable; and if statement in the exception statement then filters which response to send the user, informing them of the data’s unsuitability. See Figure 14 for the results of this structured error handling.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f14.png)

*Figure 14. Result of structured error handling when running analysis on faulty data*

The second instance arises if the user elects to calculate the maximum climb rate (change in altitude/change in time) during flight. Two possible errors were thought of: erroneous data where two successive data points share the same time resulting in a ZeroDivisionError, and TypeError if a string were to be subtracted from a number (e.g., header subtracted from first row data during loop). In both cases, the program should continue on (skipping over faulty data or skipping the header row in math operations). As such, exceptions are raised for both errors with no action taken, allowing for the loop to continue. See the second part of Figure 9 to see this script.

## Results

As the implementation of pickling/unpickling and structured error handling are discussed in detail in the previous two sections, this section covers the results of running the script – in instances without errors and instances where errors are handled.

### Trivial case

First is the trivial case: when the necessary data text file is present, the data can be pickled, and analysis performed without error. Figure 15 below shows the preconditions for this case, with a valid flight_data.txt file, but no binary .dat file.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f15.png)

*Figure 15. Trivial case preconditions*

Figure 16 below shows execution of the script in a PyCharm console printout. First, the data is displayed to demonstrate successful loading from text file (see Figure 2 for default data). Next, the user selects to export (serialize and save) the data (see Figure 12 for serialization results). The user then elects to perform an analysis, with the expected results displayed. The program is then exited. Figure 17 shows the same being performed in the command module. Figure 18 shows the resulting binary data file (flightData.dat) saved in the folder.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f16.1.png)

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f16.2.png)

*Figure 16. Trivial case running in PyCharm*

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f17.1.png)

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f17.2.png)

*Figure 17. Trivial case running in command window*

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f18.png)

*Figure 18. Trivial case binary data saved in folder*

### Unpickling case

The second case focuses on unpickling. In this instance, the pickled data .dat file is present, but no flight_data.txt file is to be found. The program begins by failing to load data from a non-existent text file. Instead, the program creates filler data that is displayed by the user. Binary data (see Figure 12) is unpickled and loaded; the imported data is displayed. Analysis is then successfully performed. Figure 19 below shows the preconditions, Figure 20 below shows the script running in PyCharm via a console printout, and Figure 21 below shows the script running in command window.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f19.png)

*Figure 19. Unpickling case preconditions*

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f20.1.png)

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f20.2.png)

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f20.3.png)

*Figure 20. Unpickling case running in PyCharm*

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f21.1.png)

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f21.2.png)

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f21.3.png)

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f21.4.png)

*Figure 21. Unpickling case running in command window*

### Error handling case

The final case focuses on structured error handling. In this case, the necessary flight_data.txt file is present, but contains faulty data (no Takeoff is recorded). In this case, the data is read from the text file and analysis attempted. However, the program recognizes a fault in the data and informs the user of the issue before returning to the menu. Figure 22 below shows the faulty data (note no Takeoff Roll), Figure 23 below shows the case running in PyCharm, and Figure 24 shows the case running in command window.

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f22.png)

*Figure 22. Error handling case erroneous data*

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f23.png)

*Figure 23. Error handling case running in PyCharm*

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f24.png)

*Figure 24. Error handling case running in command window*

## Conclusion

Though the examples used here to demonstrate pickling and structured error handling are perhaps contrived or unrealistic, they provided good experience in both aspects. Robustness to additional errors could likely be implemented and code efficiency code likely be improved as well, but this module demonstrated additional means by which realistic and useful programs can be created in Python. Therefore, the objective of the assignment was accomplished.

## Resources

The only resources used in this module with respect to pickling or structured error handling were the module notes, lecture, and the textbook.

Miscellaneous sources were used in helping to correct syntax, however.
