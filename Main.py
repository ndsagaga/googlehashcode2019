import Read
import Score
import Slide
import Print

photos = []

def main():
    photos = Read.read("data/a_example.txt")
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

if __name__ == '__main__':
    main()
