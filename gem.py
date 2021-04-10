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
#       SOURCE [gem.py] LAST MODIFIED ON 06-04-21

from glob import glob
from os import path,mkdir
from shutil import rmtree
from yaml import safe_load


home_path = 'capsule'
content_path = 'content'


if path.exists(home_path):
    rmtree(home_path)
mkdir(home_path)


indexgmi='\n'
indexgmi+='``` \n'
indexgmi+='             ███  █████                                 \n'
indexgmi+='            ░░░  ░░███                                  \n'
indexgmi+=' ████████   ████  ░███████    ██████   ████████   █████ \n'
indexgmi+='░░███░░███ ░░███  ░███░░███  ░░░░░███ ░░███░░███ ███░░  \n'
indexgmi+=' ░███ ░███  ░███  ░███ ░███   ███████  ░███ ░░░ ░░█████ \n'
indexgmi+=' ░███ ░███  ░███  ░███ ░███  ███░░███  ░███      ░░░░███\n'
indexgmi+=' ████ █████ █████ ████ █████░░████████ █████     ██████ \n'
indexgmi+='░░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ░░░░░     ░░░░░░  \n'
indexgmi+='```\n'
indexgmi+='\n'
indexgmi+='# nihar samantaray \n'
indexgmi+='\n'
indexgmi+='Hello everyone! I am a Systems programmer from India. I work at Edgeverve where we build modern banking applications. This website is my online garden - an abridgment of the stuff I\'ve learned and created over the years. I also write about amazing technology, ideas that matter, writing clean code, open-source source codes.\n'
indexgmi+='\n'
indexgmi+='## project\n'
indexgmi+='\n'
indexgmi+='=> https://nihars.com/two_list_compare.html Compare two list - Remove Duplicates, Join, Intersection\n'
indexgmi+='=> https://nihars.com/website_collection.html Yesteryear\'s collections of website designs, interface, blog sites.\n'
indexgmi+='=> https://gitlab.com/niharokz/nihars.com The source of this website using minimal static page generator.\n'
indexgmi+='\n## note\n\n'


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
    filename=note.split('/')[2].replace('.md','.gmi')
    
    if ((post_detail is not None) and (post_detail.get("showInHome")!='No')) :
        with open(path.join(home_path,filename),'w') as output_file:
            output_file.write('# '+post_detail.get("title")+'\n\nPosted on '+post_detail.get("date").strftime('%d %b %Y')+'\n\n'+md)
            output_file.write('\n\n=> index.gmi Homepage')
            indexgmi+='=> '+filename+' '+post_detail.get("title")+'\n'
        output_file.close()


indexgmi+='\n## social\n\n'
indexgmi+='=> https://nihars.com nihars.com\n'
indexgmi+='=> https://fosstodon.org/@nihars mastodon\n'
indexgmi+='=> https://gitlab.com/niharokz gitlab\n'
indexgmi+='=> https://twitter.com/niharokz twitter\n'


with open(path.join(home_path,'index.gmi'),'w') as output_file:
    output_file.write(indexgmi)
output_file.close()


with open(path.join(home_path,'favicon.txt'),'w') as output_file:
    output_file.write('🖊️')
output_file.close()