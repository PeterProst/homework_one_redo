
from utils import main
import sys


print("This is argv:", sys.argv)
command = sys.argv[1] 
print('this is command---', command)
if command == "build":
    print("Build was specified")
    main()
elif command == "new":
    open('content/new_html_page.html', 'w+').write('''
    <h1>New content</h1>
    <p>new content...</p>

    ''')
else:
    print("Please use 'build' or 'new'.")