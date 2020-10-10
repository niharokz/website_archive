# NIHARS.COM : source

## Description
This static webpage generator is to source https://nihars.com.

## Prerequisites
* PyYAML	:	To consume config file and header of blog posts.
* jinja2	:	Templating engine
* markdown2	:	To convert markdown to html

## Structure
* config.yml	:	To configure title, name, css file, js file and other configurations.
* resource		:	Location to store all css, js, image data.
* content		:	All markdown files are stored here.
* layout		:	Layouts for different html pages are kept here.
* nihars.py		:	Main file. Programs starts from here.

## Usage: 
* nihars.py publish : to publish all files inside public directory
* nihars.py new post_name : to create new post with name post_name (post name should be separated by "-" )
* nihars.py server : to creata a local server at 0.0.0.0:8000
