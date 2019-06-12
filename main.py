from data_retrieve import QUANDLDATA


if __name__ == "__main__":
    q = QUANDLDATA()
    data = q.get_data()
    print(data)
