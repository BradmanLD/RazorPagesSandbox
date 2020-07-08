from fpdf import FPDF

def main():
    filePath = "textFile.txt"
    fileContent = read_file(filePath)
    numberOfLines = fileContent.count('\n')

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 10, fileContent)
    pdf.output('tuto1.pdf', 'F')

def read_file(filePath):
    file = open(filePath, mode='r')
    content = file.read()
    file.close()
    return content

main()
