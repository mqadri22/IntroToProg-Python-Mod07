# Assignment 07 - Files & Exceptions

**Name:**		Mohammed Qadri

**Date:**		2023-08-25

**Course:** 	IT FDN 110 A

**GitHub URL:**	https://github.com/mqadri22/IntroToProg-Python-Mod07 

**GitHub Site:**	https://mqadri22.github.io/IntroToProg-Python-Mod07/ 

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

![alt text](https://github.com/mqadri22/IntroToProg-Python-Mod07/blob/main/docs/images/f01.png)

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

