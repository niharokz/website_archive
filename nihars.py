#!/bin/python

#
#       ███╗░░██╗██╗██╗░░██╗░█████╗░██████╗░░█████╗░██╗░░██╗███████╗
#       ████╗░██║██║██║░░██║██╔══██╗██╔══██╗██╔══██╗██║░██╔╝╚════██║
#       ██╔██╗██║██║███████║███████║██████╔╝██║░░██║█████═╝░░░███╔═╝
#       ██║╚████║██║██╔══██║██╔══██║██╔══██╗██║░░██║██╔═██╗░██╔══╝░░
#       ██║░╚███║██║██║░░██║██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗
#       ╚═╝░░╚══╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝
#
#       DRAFTED BY NIHAR SAMANTARAY ON 13-12-20. [https://nihars.com]
#       SOURCE [nihars.py] LAST MODIFIED ON 13-03-21

# External imports
from shutil import copytree, rmtree, copy
from os import path, makedirs
from glob import glob
from yaml import safe_load
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown

# Global Constants
TITLE = "Nihar Samantaray"
URL = "https://nihars.com"
DESC = "Personal webpage of another Systems engineer who is interested on Open Source projects based for linux environments"
CSS = "resource/css/main.css"
FAV = "resource/image/favicon.ico"
PHT = "resource/image/nihar.jpg"
MAIL = "mail@nihars.com"

# Non mutable variables
no_of_post_home = 8
note_template = 'template/note_template.html'
home_template = 'template/home_template.html'
feed_template = 'template/feed_template.xml'
home_path = 'public'
content_path = 'content'
resource_path = 'resource'

home_md="content/home.md"
archive_md="content/archive.md"
footer_md="content/footer.md"


# Create Page
def create_page(template,post_detail,md,filename):
    post_template = Environment(loader=FileSystemLoader(searchpath='./')).get_template(template)
    post_title = TITLE
    post_subtitle = DESC
    post_date = post_data = posts_list = last_date = nextpage = post_meta = ""
    post_path =  home_path
    if filename=="index.html":
        post_file = filename
        posts_list = posts[0:no_of_post_home]
        nextpage = "archive.html" if (len(posts)>no_of_post_home) else ""
    elif filename=="archive.html":
        post_file = filename
        posts_list = posts[no_of_post_home:]
    elif filename.endswith(".xml") :
        post_file = filename
        posts_list = posts
        last_date = posts_list[0].get('date')
    elif post_detail == None :
        post_file = filename.replace('.md','.html')
    else:
        post_title = post_detail.get("title")
        post_subtitle = post_detail.get("subtitle")
        post_date = post_detail.get("date")
        post_meta = post_detail.get("meta")
        post_data = filename.split('/')
        post_path = path.join(home_path)
        post_file = post_data[2].replace('.md','.html')
        post_data = post_data[1]
        
        makedirs(post_path,exist_ok=True)
    with open(path.join(post_path,post_file),'w') as output_file:
        output_file.write(
            post_template.render(
                title = TITLE,
                post_title = post_title,
                post_subtitle = post_subtitle,
                date = post_date,
                metad = post_meta,
                url = path.join(URL,post_file),
                css = '/'+CSS,
                favicon = '/'+FAV,
                photo = URL+'/'+PHT,
                article = markdown(md),
                posts = posts_list,
                home = home_md,
                footer = markdown(readmd(footer_md)),
                nextpage = nextpage,
                last_date = last_date
            )
        )
    return post_file


# Markdown file to string
def readmd(md):
    with open(md,'r') as data:
        return data.read()


# PROGRAM STARTS HERE
# Recreated home path with resource
if path.exists(home_path):
    rmtree(home_path)
makedirs(home_path)
copytree("resource", path.join(home_path,resource_path))

#Create all pages from content/note
posts = []
for note in glob(path.join(content_path,"note","*.md")):
    yaml_lines, ym, md = [],'',''
    with open(note) as infile:
        for s in infile:
            if s.startswith('---'):
                for s in infile:
                    if s.startswith('---'):
                        break;
                    else:
                        yaml_lines.append(s)
                ym = ''.join(yaml_lines)
                md = ''.join(infile)
                break;
    post_detail=safe_load(ym)
    if (post_detail is not None):
        post_url = create_page(note_template,post_detail,md,note)
        ymd = post_detail
        ymd.update({'url' : '/'+post_url})
        ymd.update({'note' : md})
        posts += [ymd]

#Sort posts based on date in descending order
posts= sorted(posts, key=lambda post :  post['date'], reverse=True)

# Other pages are created here
create_page(home_template,None,readmd(home_md),"index.html")
create_page(home_template,None,readmd(archive_md),"archive.html")
create_page(feed_template,None,readmd(home_md),"rss.xml")

