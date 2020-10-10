#NIHARS.COM: BACKEND AND TEMPLATE

## Description
This static webpage generator is to source https://nihars.com.

## Prerequisites
* PyYAML:	To consume the config file and header of blog posts.
* jinja2:	Templating engine
* markdown2:	To convert markdown to HTML

## Structure
* config.yml:	To configure the title, name, CSS file, js file, and other configurations.
* resource:	Location to store all CSS, js, image data.
* content:	All markdown files are stored here.
* layout:	Layouts for different HTML pages are kept here.
* nihars.py :	Main file. Programs start from here.

## Usage:
* nihars.py publish: to publish all files inside a public directory
* nihars.py new post_name: to create a new post with name post_name (post name should be separated by "-" )
* nihars.py server : to creata a local server at 0.0.0.0:8000
