from src.QueryModule import QueryClass


def main():
    print("Run")
    query = QueryClass()
    print(query.queryRun().content.decode())


if __name__ == "__main__":
    main()
