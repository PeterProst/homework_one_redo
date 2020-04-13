# {% for page in pages %}
#     <a href="{{page.output_filename}}">{{page.title}}</a>
# {% endfor %}
import os
import glob

# file_path = "content/blog.html"
# file_name = os.path.basename(file_path)
# print(file_name)
# name_only, extension = os.path.splitext(file_name)
# print(name_only)

pages= []
def auto_generate_content():
    all_html_files = glob.glob("content/*.html")
    for html_file in all_html_files:
        file_name = os.path.basename(html_file)
        name_only, extension = os.path.splitext(file_name)
        output = 'docs/' + file_name    
        print(name_only)
        print(file_name)
        print(html_file)
        print(output)
        pages.append({
            "filename" : file_name,
            "title" : name_only,
            "output" : output,
        })

auto_generate_content()