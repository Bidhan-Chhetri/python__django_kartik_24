class Country():
    continent = "Asia"

    @classmethod
    def show_continent(cls):
        print(f"Coninent Name : {cls.continent}")

Country.show_continent()