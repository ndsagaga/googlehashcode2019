from Photo import Photo


def read(filename):
    photos = []
    try:
        with open(filename,'r') as infile:
            numOfImages = int(infile.readline())
            for i in range(numOfImages):
                terms = infile.readline().split()
                photos.append(Photo(terms[0],set(terms[2:])))
    except IOError:
        print("IO Exception occured")

    return photos
