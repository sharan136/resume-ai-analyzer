import PyPDF2


def extract_text(file_path):

    text = ""

    pdf_file = open(file_path, "rb")

    reader = PyPDF2.PdfReader(pdf_file)

    for page in reader.pages:
        text += page.extract_text()

    pdf_file.close()

    return text