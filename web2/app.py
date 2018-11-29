import mlab
from movie import Movie
from resource import Resource
from faker import Faker
from random import randint

faker = Faker("en_US")

# for _ in range(500):
#     print(faker.state())

mlab.connect()

# m = Movie.objects().with_id("5bf7f9b5a18b970d48addaf4")
# print(m.title)
# m.delete()

# movie_list = Movie.objects()
# for m in movie_list:
#     print(m.title)
#     print(m.image)
#     print(m.year)

# resource_list = Resource.objects()
# print(len(resource_list))
# for r in resource_list:
#     print(r.name, r.city, r.yob, r.height, r.weight, sep='\n')


m = Movie(title="Batman", year=2005, image="https://upload.wikimedia.org/wikipedia/en/thumb/a/af/Batman_Begins_Poster.jpg/220px-Batman_Begins_Poster.jpg")
m.save()

# r = Resource(name="Hoang Ngoc Minh", city="Hanoi", yob=1991, height = 160, weight=52)
# r.save()

# r = Resource.objects().with_id("5bf7fc97a18b9726a85681cf")
# if r is None:
#     print("Not found")
# else:
#     print("Found")
#     r.delete()

# resource_list = Resource.objects()
# r = resource_list[0]
# r.delete()

# resource_list = Resource.objects()
# last_id= len(resource_list) - 1
# print(resource_list[last_id].id)

# r = Resource.objects().first()
# r.delete()

# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     yob = randint(1953, 2000)
#     height = randint(150, 200)
#     weight = randint(40, 150)
#     r = Resource(name=name, city=city, yob=yob, height=height, weight=weight)
#     r.save()

# records = Resource.objects(height=172)
# for r in records:
#     print(r.name, r.city, sep='\n')

# records = Resource.objects(height__gt=170, name__icontains="john")
# print(len(records))

# records = Resource.objects()
# for r in records:
#     r.update(set__availability=False)

#r = Resource.objects().with_id("5bf80d1ca18b972df81786c8")
#r.update(set__availability=True)

