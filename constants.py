CAPTCHA_FOLDER = 'generated_images'
LETTERS_FOLDER = 'letters'

CHARACTERS = list('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
NR_CAPTCHAS = 1000
NR_CHARACTERS = 5 # Adjust according to the target CAPTCHA

MODEL_FILE = 'model.hdf5'
LABELS_FILE = 'labels.dat'

MODEL_SHAPE = (100, 100) # Adjust according to the target CAPTCHA pixels. Default seems to be 160 x 60
