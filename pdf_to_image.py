from pdf2image import convert_from_path
import cv2

pages = convert_from_path('./computerphile-puzzle-2024.pdf')
image_path = './puzzle.png'
pages[0].save(image_path)

cv2.imshow('Puzzle', cv2.imread(image_path))
cv2.waitKey(0)
cv2.destroyAllWindows()
