import moviepy.editor as mp

audio_clip = mp.AudioFileClip("./tmp/music.mp3")

video_clip = mp.VideoFileClip("./tmp/loop.gif")
small_clip = video_clip.resize(0.5)

small_clip = small_clip.set_audio(audio_clip.set_duration(small_clip.duration))
small_clip.set_fps(60).write_videofile(
  "./tmp/painting.mp4", 
  threads=12,
  codec="mpeg4",
  audio_codec="aac"
)