import yt_dlp
import instaloader

insta_loader = instaloader.Instaloader()

# YouTube yuklab olish
def download_youtube(url):
    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "video.mp4"

# Instagram yuklab olish
def download_instagram(url):
    post = instaloader.Post.from_shortcode(insta_loader.context, url.split("/")[-2])
    return post.video_url
