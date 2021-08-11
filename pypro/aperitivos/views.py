from django.shortcuts import render, get_object_or_404
from .models import Video


# class Video:
#     def __init__(self, slug, titulo, vimeo_id):
#         self.slug = slug
#         self.titulo = titulo
#         self.vimeo_id = vimeo_id
#
#     def get_absolute_url(self):
#         return reverse('aperitivos:video', args=(self.slug,))


# videos = [
#     Video(slug="motivacao", titulo="Video Aperitivo: Motivação", vimeo_id='576216807'),
#     Video(slug="instalacao-windows", titulo="Instalação Windows", vimeo_id='577835849'),
# ]
#
# videos_dct = {v.slug: v for v in videos}


def indice(request):
    videos = Video.objects.order_by('creation').all()
    return render(request, 'aperitivos/indice.html', context={"videos": videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)

    # video = videos_dct[slug]

    return render(request, 'aperitivos/video.html', context={"video": video})
