# Employment-Agreement
Assignment is to extract key features from the employment agreements

Module 1: First build a model that classifies the two document types - whether it is employment letter or amendment letter.

Step 1: A file "dataset.py" is used to collect the name of all the files that ends with .txt extension and stored in "dataset.csv" file.
Step 2: After this, preprocessing is done for the "dataset.csv" file. This step includes tokenization, stop word removal, stemming using Porter Stemmer, removal of irrelevant characters like punctuations, etc. After cleaning the "dataset.csv" file, a clean dataset is stored finally in "clean_dataset.csv" file.
Step 3: After that two lists are made by matching with the name of two files - "amend and emp_aggr"
Step 4: Then, combined lists are formed with the joining of these two lists - "amend and emp_aggr".
Step 5: This step includes splitting of the combined list in the ratio of 70:30, where 70% includes training dataset and 30% includes test dataset.
Step 6: Probability Distance is calculated and labels are predicted by classifying the test dataset.
Step 7: Finally, performance measure is calculated with the help of Precision, Recall, Accuracy, F-Measure.
Step 8: Below is the result obtained with Naive Bayes Classifier:

{'Total Test data:': 292, 'Correcly predicted': 270, 'Wrong Predicted': 22, 'Accuracy': 92.46575342465754, 'Error rate': 7.534246575342466, 'Recall': 0.9777777777777777, 'precision': 0.9072164948453608, 'f1 score': 0.9411764705882353, 'tpr': 0.9777777777777777, 'fpr': 0.16071428571428573}


Module 2: Build a model to extract features from employment agreement document type and save it in CSV file.

Step 1: Employment Agreement file is opened for reading its data.
Step 2: The output of after reading the data from the Employment Agreement file is stored in some varaiable say, "sample" and it is passed as a parameter to various functions like get_human_names(), extract_notice_period(), extract_date, extract_salary(), extract_position().

The purpose of the above functions are listed as below:
get_human_names() - to extract names of the employee and employer.
extract_notice_period() - to extract notice period before termination if given.
extract_salary() - to extract base salary, bonus if given.
extract_date() - to extract employment start date, employment end date and employment agreement date if given.
extract_position() - to extract position/Job title of employee if given.

