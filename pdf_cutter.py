import os
from PyPDF2 import PdfWriter, PdfReader

# 자르고자 하는 페이지 번호
remove_pages = [0, 1, 2] # 0부터 시작

# PDF 파일의 경로
pdf_dir = '/Users/mazoola12/Documents/pdf_input/'

# 출력 폴더 생성
output_dir = '/Users/mazoola12/Documents/pdf_output/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 모든 PDF 파일 가져오기
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

# 각 PDF 파일에 대해 반복하여 페이지 자르기
for file in pdf_files:
    # PDF 파일 열기
    input_pdf = PdfReader(pdf_dir + file)

    # 출력 파일 생성
    output_pdf = PdfWriter()

    # 페이지 수
    page_count = len(input_pdf.pages)

    # 출력 파일에 페이지 추가
    for i in range(page_count):
        if i not in remove_pages:
            output_pdf.add_page(input_pdf.pages[i])

    # 자른 PDF 파일 저장
    output_file_name = output_dir + file
    with open(output_file_name, 'wb') as f:
        output_pdf.write(f)
