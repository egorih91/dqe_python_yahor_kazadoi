class Publication:
    def __init__(self, name_of_category):
        self.name_of_category = name_of_category


class News:
    def __init__(self, text, city):
        import datetime
        self.text = text
        self.city = city
        self.date = datetime.date.today()


class PrivateAd:
    def __init__(self, text, expiration_date):
        import datetime
        self.text = text
        self.expiration_date = expiration_date
        self.days_left = (self.expiration_date - datetime.date.today()).days


class SportResult:
    def __init__(self, kind_of_sport, participants, result):
        self.kind_of_sport = kind_of_sport
        self.participants = participants
        self.result = result


type_of_publication = input("Print the category number of the publication \n 1 - news \n 2 - private ad \n 3 - sport result \n")

if type_of_publication == '1':
    name_of_category = 'news'
    new_publication = News()
elif type_of_publication == '2':
    name_of_category = 'private ad'
elif type_of_publication == '3':
    name_of_category = 'sport result'
else:
    name_of_category = False
# print(name_of_category)




# x = Publication(str(type_of_record))
# x.category_definition()

# x.type_of_publication()

