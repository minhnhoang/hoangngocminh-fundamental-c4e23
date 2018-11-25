import mlab
from river import River

#exc1
mlab.connect()

#exc2
records = River.objects(continent__icontains= "africa")
for r in records:
    print(r.name)

print("--------------")
#exc3
records = River.objects(continent__iexact="S. America", length__lt=1000)
for r in records:
    print(r.name)