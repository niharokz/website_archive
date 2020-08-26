#!/usr/bin/python
import os
import datetime
import errno
from shutil import copytree, rmtree, copy
from glob import glob
from operator import itemgetter
from yaml import safe_load
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader


config_file = 'config.yml'
home_layout_file = 'layout/home_layout.html'
post_layout_file = 'layout/post_layout.html'
home_path = 'public'
content_path = 'content'


def dir_copy(src, dest):
    try:
        copytree(src, dest)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)


def post_filter(posts, postfilter):
    filtered_posts=[]
    for item in posts:
        if(item.get(list(postfilter.keys())[0]) == list(postfilter.values())[0]):
            filtered_posts.append(item)
    return filtered_posts


def parse_post(post):
    yaml_lines, ym, md = [],'',''
    with open(post) as infile:
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
    return ym,md


def create_post(post_detail,md,i):
    post_layout_template = Environment(loader=FileSystemLoader(searchpath='./'))
    post_template = post_layout_template.get_template(post_layout_file)
    post_title = post_detail.get("title")
    post_subtitle = post_detail.get("subtitle")
    post_in_home = post_detail.get("showInHome")
    post_date = post_detail.get("date")
    post_type = post_detail.get("type")
    if post_type=="singlepage":
        post_path = os.path.join(home_path,post_detail.get("url")[1:])
        post_file = "index.html"
        post_data = post_detail.get("url")[1:0]
    else:
        post_data = i.split('/')
        post_path = os.path.join(home_path,post_data[1])
        post_file = post_data[2].replace('.md','.html')
        post_data = post_data[1]
    os.makedirs(post_path,exist_ok=True)
    with open(os.path.join(post_path,post_file),'w') as output_file:
        output_file.write(
            post_template.render(
                title = title,
                post_title = post_title,
                post_subtitle = post_subtitle,
                date = post_date,
                url = os.path.join(url,post_data,post_file),
                css = '/'+css,
                js = '/'+js,
                favicon = '/'+favicon,
                avatar = '/'+avatar,
                navigation = header,
                article = markdown(md),
                footer = footer
            )
        )
    return os.path.join(post_data,post_file)


def create_page(path,posts):
    home_layout_template = Environment(loader=FileSystemLoader(searchpath='./'))
    home_template = home_layout_template.get_template(home_layout_file)
    post_pages = [posts[post:post+no_of_post] for post in range(0,len(posts),no_of_post)]
    total_page = len(post_pages)
    for item in range(0, total_page):
        pagination = {'prev':'','next':''}
        if(item==0):
            file_name='index.html'
        else:
            file_name='page'+str(item+1)+'.html'
            if(item==1):
                pagination['prev']='index.html'
            else:
                pagination['prev']='page'+str(item)+'.html'
        if(total_page-item != 1):
            pagination['next']='page'+str(item+2)+'.html'
        if(path==home_path):
            home_about = markdown(about)
            show_type = True
        else:
            home_about = ''
            show_type = False
        os.makedirs(path,exist_ok=True)
        with open(os.path.join(path,file_name),'w') as output_file:
            output_file.write(
                home_template.render(
                    url = url,
                    title = title,
                    subtitle = subtitle,
                    css = '/'+css,
                    js = '/'+js,
                    avatar = '/'+avatar,
                    favicon = '/'+favicon,
                    navigation = header,
                    about = home_about,
                    show_type = show_type,
                    posts = post_pages[item],
                    pagination=pagination,
                    footer = footer
                 )
            )



try :
    if os.path.exists(home_path):
        rmtree(home_path)
        os.makedirs(home_path)
        dir_copy('resource',os.path.join(home_path,'resource')) 
except OSError as e:
    print('Directory not created. Error: %s' % e)


with open(config_file,'r') as config_data:
    config=safe_load(config_data)

posts = []
url = config.get('url')
title = config.get('title')
subtitle = config.get('subtitle')
css = config.get('css')
js = config.get('js')
avatar = config.get('avatar')
favicon = config.get('favicon')
header = config.get('header')
footer = config.get('footer')
no_of_post = config.get('no_of_post_per_page')
about = config.get("home_about")
pages = post_filter(header,{'type' : 'list'})
single_pages = post_filter(header,{'type' : 'singlepage'})
single_pages += post_filter(footer,{'type' : 'singlepage'})

with open(about,'r') as about_data:
    about = about_data.read()

for post in pages:
    page_url = post.get('url')[1:]
    for post_file in glob(os.path.join("content",page_url,"*.md")):
        ym,md = parse_post(post_file)
        post_detail=safe_load(ym)
        if (post_detail is not None):
            post_url = create_post(post_detail,md,post_file)
            ymd = safe_load(ym)
            ymd.update({'type':post.get("name")})
            ymd.update({'url' : '/'+post_url})
            posts += [ymd]

posts= sorted(posts, key=lambda post :  post['date'], reverse=True)

for page in single_pages:
    page_url = page.get('url')[1:]
    post_file = page.get('file')
    ym,md = parse_post(post_file)
    post_detail=safe_load(ym)
    post_detail.update(page)
    if (post_detail is not None):
        post_url = create_post(post_detail,md,post_file)

create_page(home_path,post_filter(posts,{'showInHome' : True}))

for page in pages:
    create_page(os.path.join(home_path,page.get('url')[1:]),post_filter(posts,{'type' : page.get('name')}))
