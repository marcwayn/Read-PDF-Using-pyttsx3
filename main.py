import pyttsx3,PyPDF2

#Read PDF via PyPDF2
reader = PyPDF2.PdfFileReader(open('AP Biology for Dummies.pdf','rb'))

#Initialize the speaker program
speaker = pyttsx3.init()
speaker.setProperty("rate", 150)

begin = input("Which page do you want to start with? ")
end = input("Which page do you want to end on? ")

for num in range(int(begin),int(end)):  #For each page in the PDF
    text = reader.getPage(num).extract_text() #Extract the text on that page
    clean_text = text.strip().replace('\n',' ') #Replace the new lines with spaces so it's one blob of text


speaker.say(clean_text) #Say the text on the pages mentioned

speaker.runAndWait() #Run speaker program and wait for other commands

speaker.stop() #Stop speaker program