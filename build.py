
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


#this opens and reads the base html
def template_read():
    template_read = open('./templates/base.html').read()
    print('template read ran')
    return template_read
             


#uses page variable to loop through when called to apply (missing) content to template
def apply_template(page):
    file_name = page['filename']
    output = page['output']
    title = page['title']
    template = template_read() #template (top/bottom) read and put into template var
    index_content = open(file_name).read() #opens the content files: about/experience/contact and puts into var
    content = template.replace("{{content}}", index_content) #does the actual replacement for each of the above on each loop 
    content = content.replace("{{title}}", title)
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





