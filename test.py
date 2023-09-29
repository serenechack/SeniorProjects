import speech_recognition as sr
from PIL import Image
import matplotlib.pyplot as plt


r = sr.Recognizer()

# Define a mapping from text to image filenames
sign_language_dict = {
    'A': '.\images\A.png',
    
    'B': '.\images\B.png',
    'C': '.\images\C.png',
    'D': '.\images\D.png',
    'E': '.\images\E.png',
    'F': '.\images\F.png',
    'G': '.\images\G.png',
    'H': '.\images\H.png',
    'I': '.\images\I.png',
    'J': '.\images\J.png',
    'K': '.\images\K.png',
    'L': '.\images\L.png',
    'M': '.\images\M.png',
    'N': '.\images\\N.png',
    'O': '.\images\O.png',
    'P': '.\images\P.png',
    'Q': '.\images\Q.png',
    'R': '.\images\R.png',
    'S': '.\images\S.png',
    'T': '.\images\T.png',
    'U': '.\images\\U.png',
    'V': '.\images\V.png',
    'W': '.\images\W.png',
    'X': '.\images\X.png',
    'Y': '.\images\Y.png',
    'Z': '.\images\Z.png',
    ' ': '.\images\space.png',  # Define a blank image for spaces
}


def text_to_sign_language(text):
    # Create a list to store the sign language images
    sign_language_images = []

    for letter in text.upper():
        if letter in sign_language_dict:
            image_path = sign_language_dict[letter]
            try:
                img = Image.open(image_path)
                sign_language_images.append(img)
            except FileNotFoundError:
                print(f"Image not found for letter: {letter}")

    return sign_language_images

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    try:
        text = r.recognize_google(audio_text, language='en')
        translated_images = text_to_sign_language(text)
        if translated_images:
            plt.figure(figsize=(12, 4))
            total_width = sum(img.width for img in translated_images)
            max_height = max(img.height for img in translated_images)
            combined_image = Image.new('RGB', (total_width, max_height))

            x_offset = 0
            for img in translated_images:
                combined_image.paste(img, (x_offset, 0))
                x_offset += img.width

            plt.imshow(combined_image)
            plt.axis('off')  # Turn off axis labels and ticks
            plt.show()
            print("Text: " + text)
    except:
        print("Sorry, I did not get that")
