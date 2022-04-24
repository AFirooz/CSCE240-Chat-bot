Required before running:

1. Please install the packages "fuzzywuzzy" and "Levenshtein" to avoid any problems

2. select the district 78, to start the chatbot

3. Chatbot functionality overview : https://youtu.be/VFGppk7KbUY

----------------------------------------------------------------


Notes:

1. If the class file name has "_info" in it, like "basic_info", that means it is responsible for answering the user.

2. To add a question to the bot:
    a. find the right file (basic, personal, other)
    b. add a private list that contain your question ( __example = [["something"]] )
    c. make sure that you use 2 dimension list. The bot will look and try to match the user's question with the list you added in step "a"
    d. add the private variable (__example) inside the "__trainingList"
    e. Add a name for it in "__strTrainingList" that would fit this sentence "You requested information regarding the ----- of your representative"
    f. add the bot answer (which is a string) at the end of the method "basicCheck()"

3. If you are looking to create an "_info" file (to answer questions), you need to inherit the "abstract_chat_class"

4. If you add support to a district, please add its number inside "other_info.py", in class first list called "__supportedDistrictsAnswer"

