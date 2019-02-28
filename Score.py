def score(slides):
    s = 0
    for i in range(0, len(slides) - 1):
        s += scoreTwoSlides(slides[i].tags, slides[i + 1].tags)

    return s


def scoreTwoSlides(slide1, slide2):
    inter = len(slide1 & slide2)
    s1 = len(slide1 - slide2)
    s2 = len(slide2 - slide1)

    return min(inter, s1, s2)

