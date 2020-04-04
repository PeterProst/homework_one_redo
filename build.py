#original function for reference
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


#this function is currently useless :(
def template_read():
    template_read = open('./templates/base.html').read()
    print('ready 1')
    return template_read
    
# def title_change(page):
#     file_name = page['filename']
#     output = page['output']
#     title = page['title']
#     template = template_read() #template (top/bottom) read and put into template var
#     index_content = open(file_name).read() #opens the content files about/experience/contact and puts into var
#     content = template.replace("{{content}}", index_content) #does the actual replacement for each of the above on each loop 
#     content1 = template.replace("{{title}}", index_content)
#     writing_output(output,content, content1)#writes to output file destination
#     print(3)      
    

#takes variables from libraries, opens the templates/content folders and writes to them
def apply_template(page):
    file_name = page['filename']
    output = page['output']
    title = page['title']
    template = template_read() #template (top/bottom) read and put into template var
    index_content = open(file_name).read() #opens the content files about/experience/contact and puts into var
    content = template.replace("{{content}}", index_content) #does the actual replacement for each of the above on each loop 
    writing_output(output,content)#writes to output file destination
    print(2)



def writing_output(output, content):
    open(output, 'w+').write(content)
    print(4)

def main():
    for page in pages:
        apply_template(page)#goes through for loop to apply the template from info gathered through pages list
        print(5)

main()





