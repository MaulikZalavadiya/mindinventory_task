from bson.objectid import ObjectId

class Video:
    def __init__(self, db):
        self.collection = db.videos_to_mp4

    def insert_video(self, video_data):
        return self.collection.insert_one(video_data).inserted_id

    def find_video(self, query):
        return self.collection.find_one(query)
