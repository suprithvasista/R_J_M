from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_pdf(content, file_name):
    # Create a PDF document
    c = canvas.Canvas(file_name, pagesize=letter)

    # Set font and size for the content
    c.setFont("Helvetica", 12)
    x = 30
    max_width = 100

    # Split content into lines and write to the PDF
    lines = content.split("\n")
    y = 750  # Starting y-coordinate
    for line in lines:
        # Draw the line with a maximum width of 300 characters
        while len(line) > max_width:
            c.drawString(x, y, line[:max_width])  # Draw the first 300 characters
            y -= 15  # Move to the next line
            line = line[max_width:]  # Remove the drawn characters from the line
        c.drawString(x, y, line)  # Draw the remaining part of the line
        y -= 15  # Move to the next line

    # Save the PDF
    c.save()