import os

def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f'{folderName}/{file}')


files = os.listdir()
files.remove("folder_cleaner.py")


createIfNotExists('Images')
createIfNotExists('Excel Sheets')
createIfNotExists('PDF')
createIfNotExists('Documents')
createIfNotExists('Others')
createIfNotExists('Media')


imgExts = [".png", ".jpg", ".jpeg", ".raw", ".gif"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

excelExts = [".xlsx", ".csv"]
excels = [file for file in files if os.path.splitext(file)[1].lower() in excelExts]

docExts = [".txt", ".docx", "doc"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4", ".mp3", ".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

pdfExts = [".pdf"]
pdfs = [file for file in files if os.path.splitext(file)[1].lower() in pdfExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)

move("Images", images)
move("Excel Sheets", excels)
move("Documents", docs)
move("PDF", pdfs)
move("Other", others)
move("Media", medias)