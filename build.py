
from jinja2 import Template
import glob, os

pages = []

def auto_generate_content():
    all_html_files = glob.glob("content/*.html")
    for html_file in all_html_files:
        file_name = os.path.basename(html_file)
        output = "docs/" + file_name
        name_only, extension = os.path.splitext(file_name)
        pages.append({
            "filename" : html_file,
            "title" : name_only,
            "output" : output,
        })
        
 

auto_generate_content()



# this opens and reads the base html
def template_html():
    template_html = open('templates/base.html').read()
    print('template read ran')
    return template_html
             


#uses page variable to loop through when called to apply (missing) content to template
def apply_template(page):
    file_name = page["filename"]
    output = page["output"]
    page_title = page["title"]
    template = Template(template_html()) #template (top/bottom) read and put into template var
    index_html = open(file_name).read() #opens the content files: about/experience/contact and puts into var
    content = template.render(
        title = page_title,
        content = index_html,
    ) #does the actual replacement for each of the above on each loop 
    # content = content.replace("{{title}}", page_title)#updates content to include the dynamic title 
    writing_output(output,content)#writes to output file destination
    print('apply template ran')



def writing_output(output, content):
    open(output, 'w+').write(content)
    print('output ran')

def main():
    for page in pages:
        apply_template(page)#goes through for loop to apply the template from info gathered through pages list
        print('main ran')

main()





