import pptx
from pdfminer.high_level import extract_text
import re

def ppt_to_pdf(ppt_path, pdf_path):
    prs = pptx.Presentation(ppt_path)
    prs.save(pdf_path)

def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    texts = text.split('\f')
    return texts

def parse_texts(texts):
    result = ""
    current_title = ""
    
    for text in texts:
        title_match = re.search(r'(.*):$', text)
        if title_match:
            current_title = title_match.group(1)
            result += f'## {current_title}\n'
        else: 
            result += f'{text}\n'
            
    return result

def main():
    ppt_path = "E:\\学科网资料2024020301(29)份\\4.1采 集 数 据课件 西北大学出版社中职信息技术（基础模块）下册 .pptx"
    pdf_path = "E:\\4.1采 集 数 据课件 西北大学出版社中职信息技术（基础模块）下册 .pdf"
    
    # ppt_to_pdf(ppt_path, pdf_path)
    
    texts = extract_text_from_pdf(pdf_path)
    
    result = parse_texts(texts)
    print(result)
    with open('E:\\output.md', 'w', encoding='utf-8') as f:
        f.write(result)
        
if __name__ == '__main__':
    main()