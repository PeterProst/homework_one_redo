#list of pages that are accessed via for loop
pages = [
    {
        "filename" : "content/index.html",
        "output" : "faker/index.html",
        "title" : "About Me",
    },
    {
        "filename" : "content/experience.html",
        "output" : "faker/experience.html",
        "title" : "My Experience",
    },
    {
        "filename" : "content/contact.html",
        "output" : "faker/contact.html",
        "title" : "Contact Page",
    },
]


# def apply_template(content):
#     for page in pages:
#         file_name = page['filename']
#         output = page['output']
#         title = page['title']
#         template = open('./templates/base.html').read()
#     return template

# apply_template()

# def main():
#     content = open(file_name).read()
#     resulting_html_index = apply_template(content)

# main()

# main():
#     for page in pages:
#         file_name = page['filename']
#         output = page['output']
#         title = page['title']
#         template = open('./templates/base.html').read() <----template (top/bottom) read and put into template var
#         index_content = open(file_name).read() <----opens the content files about/experience/contact and puts into var
#         finished_pages = template.replace("{{content}}", index_content)  <---does the actual replacement for each of the above on each loop
#         open(output, 'w+').write(finished_pages)  <---writes the final pages into the docs folder
        
#         print('tested')


# main()

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

# def write_to_file(page):
#     output = page['output']
#     apply_template
#     open(output, 'w+').write(finished_pages)   
#     print('done2') 

def main():
    for page in pages:
        template_read()
        apply_template(page)
        print(' 3')
        #write_to_file(page)

main()


