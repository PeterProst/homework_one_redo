
from jinja2 import Template
import glob, os

pages = []

def auto_generate_content():
    all_html_files = glob.glob("content/*.html")
    for html_file in all_html_files:
        file_name = os.path.basename(html_file)
        name_only, extension = os.path.splitext(file_name)
        output = 'docs/' + file_name    
        pages.append({
            "filename" : file_name,
            "title" : name_only,
            "output" : output,
            "file_path" : html_file
        })

auto_generate_content()



def template_html():
    template_html = open('templates/base.html').read()
    print('template read ran')
    return template_html
             


def apply_template(page):
    file_name = page["filename"]
    output = page["output"]
    page_title = page["title"]
    file_path = page['file_path']
    template = Template(template_html())
    content_html = open(file_path).read()
    content = template.render(
        pages = pages,
        content = content_html, 
        title = page_title,
    )
    writing_output(output, content)
    print('apply template ran')



def writing_output(output, content):
    open(output, 'w+').write(content)

    print('output ran')

def main():
    for page in pages:
        apply_template(page)
        print('main ran')






