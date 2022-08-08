# RGUTask
Technical Interview Coding Task

This Repo was produced as part of a coding task for the job position of Research Assistant in Artificial Intelligence and Reasoning at the RGU.

The Repo contains two main files: app.py, and plotter.html. There are also two images and an XML document included.

# Installation and Execution
1. Download and extract the Repo to your computer. (or clone)

2. Navigate to the file directory and open a powershell window (or just open the folder in Visual Studio Code).

3. Use the command "flask run" to execute the app.py code and start the webserver (Make sure Flask is available in your dev environment).

4. Open the plotter.html file in your favourite browser (Brave).

5. View the lovely plots?

# Specific Task Information

- Task 1) The contents of task 1 occur in the file app.py
    - a) Firstly ElementTree is used to parse the XML file. Then the element tree object is restructured into a Python dictionary using two python classes (XmlListParse, XmlDictParse) which work recursively on the ElementTree object to create a dictionary called xmlData.
    - b) The Flask Library is used to simply create a local webserver, and a single route (/scores) is setup. Accessing this endpoint with a get request will return the contents of the XML file in a JSON format.

- Task 2) The contents of the task occur in the file plotter.html
    - a) There is a single html file (plotter.html) which contains all of the html/js/css used as part of the task.
    - b) Each scenario has two graphs (line graph + parallel coordinate plot)
    - c) I used Plotly to make the graphs
    - d) The plots are created in real time and are not images
    - e) A GET request is made in JS to the /scores API and the required JSON data retrieved.

- Task 3) Each plot has a 9th feature called Global which is a "sum" of the local feature similarities. Note that for the line graph the global feature has been normalised to be between the values of [0,1] to make it look better. 

# Additional Notes

Since this was a simple interview task I included all of the code in as few files as possible, e.g. all html/js/css in a single file, normally I would separate these into separate files if they became too complex. 

Also again since this was an interview task I used comments differently than I normally do, I made additional comments (often verbose) to better explain the code.