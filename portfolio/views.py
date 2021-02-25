from django.shortcuts import render
from .models import Images
from django.core.mail import EmailMessage
from .models import Photo, Location


def home(request):
    context = {}
    images = Images.objects.all()
    context["images"] = images

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        email_message = EmailMessage(
            subject=name + " : " + subject,
            body=message,
            to=['twikoslol@gmail.com'],
            headers={"Reply-To": email}
        )
        email_message.send()
    return render(request, "index.html", context)


def gallery(request):
    photos = Photo.show_all_photos()
    locations = Location.objects.all()
    return render(request, "gallery.html", context={"photos": photos,
                                                    "locations": locations})

def location_filter(request, id):
    photos = Photo.objects.filter(location__id = id)
    results = len(photos)
    location = Location.objects.get(id = id)
    locations = Location.objects.all()

    return render(request, "location.html", context={"photos":photos,
                                                             "results":results,
                                                             "location":location,
                                                             "locations":locations})