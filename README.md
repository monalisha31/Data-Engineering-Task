# Data-Engineering-Task

# Task 1

Write a script (named “wiki_extractor.py”) that performs a Wikipedia search using the provided keyword, and returns urls of “n” related Wikipedia pages. Additionally, the script should also extract one paragraph from each such page and return the result as a json file

Input Arguments

- --keyword (string argument to define the query string)
- --num_urls (integer argument for number of wikipedia pages to extract from)
- --output (output json-file name)

Solution

All the files related to Task 1 is present in the Task 1 folder. Here, I have used the Wikipedia Python library to scrape the search results and paragraphs. The output.json file is a sample output of the code. The attached video will explain the working of the solution. In order to execute the code, do follow the code instructions mentioned below:


```
git clone https://github.com/monalisha31/Data-Engineering-Task/
cd Data-Engineering-Task
cd 'Task 1'
python3 wiki_extractor.py --keyword "Coronavirus" --num_urls 4 --output 'final'

```
Video of the solution :

https://user-images.githubusercontent.com/42024284/152732710-29f2a130-fc75-414b-8044-f05b844d1448.mp4


# Task 2

Extract pdf content from all the url’s present in the google spreadsheet:

There are two kind of url’s in the following sheet:
- A. Urls which are ending with “.pdf” which directly trigger downloading of the pdf file.

- B. Urls with the link to the page where “pdf” files are located. In order to extract from files like these you would need to scrape the html content and look for pdf links in it!

Solution

Due to time constraint, I could not implement the OCR feature to extract the marathi characters. The task 2.ipynb file divides the Task 2 into subtasks:

- Convert Excel file to CSV and drop all the columns except the Links column
- Check if the extensions of the URLs ends with .pdf or not.
- In .pdf section, extract content from the pdf and save it in json file [OCR feature is not implemented]
- In other types of files extension, scraped the links containing the .pdf extension.
- Extract the content of the PDF links. [OCR feature is not implemented]
- Combine the results from the two methods and save it in the json file.




