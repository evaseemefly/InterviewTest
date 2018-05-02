def tag(tag_name):
    def add_tag(content):
        return "<{0}>{1}</{0}>".format(tag_name,content)
    return add_tag

content="hello"

add_tag=tag('a')
img_tag=tag('img')
print(add_tag(content))
print(img_tag('/sdsdfs/sss.jpg'))