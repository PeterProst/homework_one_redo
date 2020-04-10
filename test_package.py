# import glob
# all_html_files = glob.glob("content/*.html")
# print(all_html_files)

# import os

# file_path = "content/blog.html"
# file_name = os.path.basename(file_path)
# print(file_name)
# name_only, extension = os.path.splitext(file_name)
# print(name_only)



from jinja2 import Template
index_html = open("index.html").read()


template_html = open("base.html").read()
template = Template(template_html)
template.render(
    title="Homepage",
    content=index_html,)