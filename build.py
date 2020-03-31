
#Reads in the top.html

top_html = open('./templates/top.html').read()
print('this actually worked 1')

#Reads in the bottom.html

bottom_html = open('./templates/bottom.html').read()

print('this actually worked 2')
#Reads in the middle index.html file by combining index/expereince/projects together

middle_html = open('./content/index.html').read()
print('this actually worked 3')

#time to combine all the contents from the contents folder

combine_html = top_html + middle_html + bottom_html
print('combined html successfully')

#Write this into a brand new directory in the same file

open('./docs/index.html', 'w+').write(combine_html)
print('this finally happened')



#here's the seond part to make the 2nd part work - experience 

#Reads in the middle index.html file by combining index/expereince/projects together

middle_html = open('./content/experience.html').read()
print('this actually worked 3')

#time to combine all the contents from the contents folder

combine_html = top_html + middle_html + bottom_html
print('combined html successfully')

#Write this into a brand new directory in the same file

open('./docs/experience.html', 'w+').write(combine_html)
print('this finally happened')


#here is the third part to make the projects portion work 

#Reads in the middle index.html file by combining index/expereince/projects together


#Reads in the middle index.html file by combining index/expereince/projects together

middle_html = open('./content/contact.html').read()
print('this actually worked 3')

#time to combine all the contents from the contents folder

combine_html = top_html + middle_html + bottom_html
print('combined html successfully')

#Write this into a brand new directory in the same file

open('./docs/contact.html', 'w+').write(combine_html)
print('this finally happened')










