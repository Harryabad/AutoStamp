# Adding an approval stamp (watermark) to multiple PDF documents in one go

## My work life requires me to stamp approve several PDF documents a week.
## My goal was to find a way to do this all in bulk.

# Using PyPDF2 to manipulate pdf 
# Using os to forloop a directorys
import PyPDF2, os

# Folder for PDF files awaiting aproval

directory = "Desktop\\PDF bulk stamp\\Unstamped" 

for file in os.listdir(directory):
    #
    input_file = file

    # New destination for output files & name changes
    output_file = "Desktop\\PDF bulk stamp\\Approved\\(Approved) " + file 

    # Stamp to be pasted over PDF files
    watermark_file = "Desktop\\PDF bulk stamp\\Stamp.pdf"

    with open((directory + "\\" + input_file), "rb") as pdf_input:

        # Read content of the original file
        pdf = PyPDF2.PdfFileReader(pdf_input)
        
        with open(watermark_file, "rb") as watermark_input:
            # Read watermark
            watermark = PyPDF2.PdfFileReader(watermark_input)

            # Create new blank PDF
            new_pdf = PyPDF2.PdfFileWriter()

            # Add a new Page (Setting the first page to be the same as the first of our pdf)
            new_pdf.addPage(pdf.getPage(0))

            # Merge the two pdfs (Overlay the watermark ontop of the original pdfs)
            new_pdf.getPage(0).merge_page(watermark.getPage(0))
        
            # Open output file
            with open(output_file, "wb") as pdf_output:
                # write the watermarked file to the new file
                new_pdf.write(pdf_output)
