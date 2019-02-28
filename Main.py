import Read
import Score
import Slide
import Print
import random

photos = []

def shuffling(slides):
    random.shuffle(slides)
    return slides

def main():
    photos = Read.read("data/b_lovely_landscapes.txt")
    Slide.photo_array = photos
    slides = []
    slideV = []
    for i in range(len(photos)):
        if photos[i].type == 'H':
            slides.append(Slide.Slide([i]))
        else:
            if len(slideV) == 0:
                slideV.append(i)
            else:
                slides.append(Slide.Slide([slideV.pop(),i]))

    print(Score.score(slides))
    Print.print_slides(slides)

    population = [slides]

    for i in range(50):
        population.append(shuffling(slides))
        print(Score.score(population[-1]))


if __name__ == '__main__':
    main()
