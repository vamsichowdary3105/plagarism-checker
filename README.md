# plagarism-checker

ABSTRACT 
A Python program called SoSorry was created to help with plagiarism detection. It has two different 
modes: "From Whole Server" and "One-To-One" comparison. The program interfaces with other 
services to check for plagiarism and uses Tkinter for its graphical user interface. 
Using HTTP queries to an external server, users can enter text for plagiarism analysis in the "From 
Whole Server" option. Users can enter text into the text entry form on the user interface, and then click 
a button to start the plagiarism check. After finishing, the program shows pertinent findings from the 
plagiarism check, such as word count, SoSorry Index, and matches found.. Users are able to compare 
the similarity of two text files using the "One-To-One" option. To load the files, users can either enter 
the file paths manually or use a file dialog. After loading, the application uses the SequenceMatcher 
module to determine the texts' similarity ratio. A percentage representing the degree of similarity 
between the two texts is displayed as the outcome.With SoSorry's easy-to-use interface, users may easily 
and conveniently detect possible plagiarism in a variety of settings when doing plagiarism checks.
