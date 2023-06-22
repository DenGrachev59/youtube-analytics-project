from src.video import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    broken_video1 = Video('AWX4JnAnjBE')
    assert broken_video.title is None
    assert broken_video.like_count is None

    # print(broken_video1.title)
    # print(broken_video.title)
    # print(broken_video.like_count)
    # print(broken_video.video_id)
    # print(broken_video1.video_response['items'][0])