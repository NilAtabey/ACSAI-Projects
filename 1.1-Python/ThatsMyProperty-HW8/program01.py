import images

def ex1(input_file, output_file):
    img = images.load(input_file)
    backcolor = img[0][0] # is a tuple of RGB values
    result = recursive_search(img, backcolor)
    
    if not result:
        images.save([[backcolor]], output_file)
        return 1 # works for cases named "empty", no plots divided
    else:
        images.save([[backcolor]+result], output_file)
        return 1+len(result)*3
    
def recursive_search(img, backcolor):
    index_x = None
    for item in range(0, len(img)):
        if backcolor not in set(img[item]) and len(set(img[item])) == 1:
            index_x = item
            divisorcolor = set(img[item]).pop() # get rid of the set approach
            break
    
    if index_x is None:
        return []
    
    # images.save(img, "TRIALS/trialimage.png")
    index_y = img[0].index(divisorcolor)
    res = [divisorcolor]

    img_list = [[item[index_y+1:] for item in img[index_x+1:]],
                [item[:index_y] for item in img[index_x+1:]],
                [item[index_y+1:] for item in img[:index_x]],
                [item[:index_y] for item in img[:index_x]]]
    
    for v in img_list:
        # images.save(v, f"TRIALS/trialimage{index_x}--{index_y}.png")
        res.extend(recursive_search(v, backcolor))
    
    return res

# ex1("puzzles/small03.in.png", "TRIALS/small03trial1.png")