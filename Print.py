
def print_slides(slides):
    with open("out.txt","w")as outfile:
        lines = str(len(slides))+"\n"
        for slide in slides:
            lines+= " ".join([str(x+1) for x in slide.photos])
            lines+="\n"
        outfile.write(lines)
