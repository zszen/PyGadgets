#! usr/bin/env python
# coding=utf-8
import os
from xml.etree import ElementTree
from PIL import Image

def tree_to_dict(tree):
    d = {}
    for index, item in enumerate(tree):
        if item.tag == 'key':
            if tree[index+1].tag == 'string':
                d[item.text] = tree[index + 1].text
            elif tree[index + 1].tag == 'true':
                d[item.text] = True
            elif tree[index + 1].tag == 'false':
                d[item.text] = False
            elif tree[index + 1].tag == 'dict':
                d[item.text] = tree_to_dict(tree[index+1]) 

    return d

def gen_png_from_plist(plist_filename, png_dir):
    # 第一步 读取plist的信息 解析
    to_list = lambda x: x.replace('{','').replace('}','').split(',')
    # 解析plist为字典
    root = ElementTree.fromstring(open(plist_filename, 'r').read())
    plist_dict = tree_to_dict(root[0])
    # 根据plist画一张大图作为底图
    get_size = plist_dict["metadata"]["size"]
    sizelist = [ int(x) for x in to_list(get_size) ]
    result_image = Image.new('RGBA', sizelist, (0,0,0,0))
    for k, v in plist_dict['frames'].items():
        full_path = os.path.join(png_dir, k)
        if not os.path.exists(full_path):
            print u"图片不存在:" + full_path
            continue
        # 打开子图片
        part_png = Image.open(full_path) 

        spriteSourceSize = v["spriteSourceSize"] if v.has_key("spriteSourceSize") else v["sourceSize"]
        spriteSourceSize = [ int(x) for x in to_list(spriteSourceSize) ]
        # pack后剩下的有效区域
        textureRect = v["textureRect"] if v.has_key("textureRect") else v["frame"]
        textureRect = [ int(x) for x in to_list(textureRect) ]
        # 是否旋转
        isRotate = v["textureRotated"] if v.has_key("textureRotated") else v["rotated"]
        # 小图在大图上的区域
        spriteOffset = v["spriteOffset"] if v.has_key("spriteOffset") else v["offset"]
        spriteOffset = [ int(x) for x in to_list(spriteOffset) ]
        # 获得长宽
        width = int( textureRect[3] if isRotate else textureRect[2] )  
        height = int( textureRect[2] if isRotate else textureRect[3] ) 

        if (part_png.size[0] != spriteSourceSize[0]) or (part_png.size[1] != spriteSourceSize[1]):
            print "图片和所描述尺寸不一致：目标替换尺寸->" + str(spriteSourceSize) + " 图片尺寸->" + str(part_png.size)
            continue

        if isRotate:
            rect_box=(   
                ( spriteSourceSize[0] - height)/2 + spriteOffset[0],  
                ( spriteSourceSize[1] - width)/2 - spriteOffset[1],  
                ( spriteSourceSize[0] + height)/2 + spriteOffset[0],  
                ( spriteSourceSize[1] + width)/2 - spriteOffset[1]   
                )
        else:
            rect_box=(  
                ( spriteSourceSize[0] - width)/2 + spriteOffset[0],  
                ( spriteSourceSize[1] - height)/2 - spriteOffset[1],  
                ( spriteSourceSize[0] + width)/2 + spriteOffset[0],  
                ( spriteSourceSize[1] + height)/2 - spriteOffset[1] 
                )  
        # 裁剪图片
        rect_png = part_png.crop(rect_box)
        result_box = ( textureRect[0], textureRect[1], textureRect[0] + width, textureRect[1] + height )
        if isRotate:
            new_png = rect_png.transpose(Image.ROTATE_270)#使图片旋转
            result_image.paste(new_png, result_box, mask = 0)
        else:
            result_image.paste(rect_png, result_box, mask = 0)
        print "paste", k
    # 保存图片
    save_name = os.path.join( os.path.dirname(plist_filename), plist_dict["metadata"]["realTextureFileName"] )
    result_image.save(save_name)

def walkFile(rootdir):
	list = os.listdir(rootdir)
	for i in range(0,len(list)):
		if ".plist" in list[i]:
			# plist 所在路径
		    plist_filename = os.path.dirname(__file__) + '/' +'../res/atlas/'+list[i]
		    # 图片所在文件夹（零碎的原始散图文件夹，不是生成后的png图片文件夹）
		    png_dir = os.path.dirname(__file__) + '/' + '../res_useless/texture/'+list[i][0:-6]
		    # print plist_filename,png_dir
		    # 根据plist生成图片
		    if (os.path.exists(plist_filename) and os.path.exists(png_dir)):
		        gen_png_from_plist( plist_filename, png_dir )
		    else:
		        print "make sure you have both plist and pngDir in directory"

walkFile("../res/atlas")
