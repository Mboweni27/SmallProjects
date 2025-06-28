
from docx2pdf import convert as docx_to_pdf
from pdf2docx import Converter
import os

def doc_to_pdf(input_path: str , output_path: str= None):
	print("Converting from word to pdf")
	try:
		docx_to_pdf(os.path.dirname(input_path) or input_path, output_path)
	except Exception as e:
		print("Failed to locate the file.\nNB Check the file path, and make sure to add it in the file path\n",e)


def pdf_to_doc(input_path: str, output_path: str=None):
	print("Converting from pdf to word")
	try:
		output_path = output_path or input_path.replace('.pdf', '.docx')
		convert = Converter(input_path)
		convert.convert(output_path)
		convert.close()
	except Exception as e:
		print("Failed to locate the file.\nNB Check the file path, and make sure to add it in the file path\n",e)
	



doc_to_pdf('input_path')

pdf_to_doc('input_path')

