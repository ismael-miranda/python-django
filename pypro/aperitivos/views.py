<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import Video


def indice(request):
    videos = Video.objects.order_by("creation").all()
=======
from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video("motivacao", "Video Aperitivo: Motivação", 576216807),
    Video("instalacao-windows", "Instalação Windows", 577835849),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
>>>>>>> 83a38f729d5f31c96782abcd39317d57734f628a
    return render(request, 'aperitivos/indice.html', context={"videos": videos})


def video(request, slug):
<<<<<<< HEAD
    video = get_object_or_404(Video, slug=slug)
=======
    video = videos_dct[slug]
>>>>>>> 83a38f729d5f31c96782abcd39317d57734f628a
    return render(request, 'aperitivos/video.html', context={"video": video})
