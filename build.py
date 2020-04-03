#list of pages that are accessed via for loop
pages = [
    {
        "filename" : "content/index.html",
        "output" : "docs/index.html",
        "title" : "About Me",
    },
    {
        "filename" : "content/experience.html",
        "output" : "docs/experience.html",
        "title" : "My Experience",
    },
    {
        "filename" : "content/contact.html",
        "output" : "docs/contact.html",
        "title" : "Contact Page",
    },
]


# def main():
#     for page in pages:
#         file_name = page['filename']
#         output = page['output']
#         title = page['title']
#         template = open('./templates/base.html').read()
#         index_content = open(file_name).read()
#         finished_pages = template.replace("{{content}}", index_content)
#         open(output, 'w+').write(finished_pages)
        
#         print('tested')




def template_read():
    template_read = open('./templates/base.html').read()
    print('ready 1')

def apply_template(page):
    file_name = page['filename']
    output = page['output']
    title = page['title']
    template = open('./templates/base.html').read() #<----template (top/bottom) read and put into template var
    index_content = open(file_name).read() #<----opens the content files about/experience/contact and puts into var
    finished_pages = template.replace("{{content}}", index_content) # <---does the actual replacement for each of the above on each loop
    open(output, 'w+').write(finished_pages)
    print('2')

def main():
    for page in pages:
        template_read()
        apply_template(page)
        

main()





