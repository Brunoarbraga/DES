from des_encryption_function import *
from PIL import Image, ImageFilter

def main():
    encrypt_image('../images/lenna.png', '../images/lenna_encrypted_keys=0.png', key)

if __name__ == "__main__":
    main()