from class_models.ProviderModule import ProviderClass


def main():
    print("Run")
    print(ProviderClass.name)
    print(ProviderClass().getPetitionNumber())


if __name__ == "__main__":
    main()
