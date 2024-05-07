from fpdf import FPDF
from PIL import Image
import csv
import os

def create_id_card(pdf, template_path, name, title, photo_path):
    pdf.add_page()
    pdf.image(template_path, x=0, y=0, w=85, h=54)
    pdf.set_font("Arial", size=12,style='B')
    pdf.cell(0, 15, txt=f"{name}", ln=True)
    pdf.cell(0, 0, txt=f"{title}", ln=True)
    #pdf.cell(10, 10, txt=f"{title}", ln=True)
    pdf.image(photo_path, x=48, y=5, w=30,h=32)

def generate_id_cards(template_path, csv_path, photo_dir, output_path):
    pdf = FPDF()
    with open(csv_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header
        for row in csvreader:
            name, title, photo_name = row
            photo_path = os.path.join(photo_dir, photo_name)
            create_id_card(pdf, template_path, name, title, photo_path)
    pdf.output(output_path)

# Example usage:
template_path = "template.jpg"
csv_path = "employees.csv"
photo_dir = "Images"
output_path = "id_cards.pdf"

generate_id_cards(template_path, csv_path, photo_dir, output_path)
