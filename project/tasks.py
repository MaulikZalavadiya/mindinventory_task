import os
from moviepy.editor import VideoFileClip
from project.models import Video
from project import celery
from bson.objectid import ObjectId
from pymongo import MongoClient

@celery.task
def convert_video_task(video_id):
    mongo_client = MongoClient('mongodb://localhost:27017')
    db = mongo_client.video_management
    video = Video(db)
    video_data = video.find_video({'_id': ObjectId(video_id)})
    
    if video_data:
        input_path = video_data['filepath']
        output_path = os.path.splitext(input_path)[0] + '.mp4'
        
        clip = VideoFileClip(input_path)
        clip.write_videofile(output_path, codec='libx264')
        
        video.collection.update_one(
            {'_id': ObjectId(video_id)},
            {'$set': {'filepath': output_path, 'converted': True}}
        )

    
    mongo_client.close()
