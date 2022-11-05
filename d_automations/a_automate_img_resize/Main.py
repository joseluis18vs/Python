from a_automate_img_resize.Controllers import DirectoryController, ImageController


def main():
    # Get Path
    path = DirectoryController.get_file()
    # Resize
    resize_img = ImageController.resize_img(path)
    # Save
    ImageController.save_image(resize_img)


if __name__ == "__main__":
    main()
