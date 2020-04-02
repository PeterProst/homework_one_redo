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


def main():
    for page in pages:
        file_name = page['filename']
        output = page['output']
        title = page['title']
        top_html = open('./templates/top.html').read()
        bottom_html = open('./templates/bottom.html').read()
        middle_html = open(file_name).read()
        combine_html = top_html + middle_html + bottom_html
        open(output, 'w+').write(combine_html)
        
        print('tested')


main()







