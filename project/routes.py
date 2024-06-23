import os
from flask import Blueprint, request, jsonify, g, current_app
from werkzeug.utils import secure_filename
from project.tasks import convert_video_task
from project.models import Video
from project.utils import allowed_file

main = Blueprint('main', __name__)

@main.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('media', filename)
        file.save(filepath)
        
        video = Video(g.db)
        video_id = video.insert_video({'filename': filename, 'filepath': filepath})
        
        # import pdb;pdb.set_trace()
        convert_video_task.delay(str(video_id))
        
        return jsonify({'message': 'File successfully uploaded', 'video_id': str(video_id)}), 201

@main.route('/search', methods=['GET'])
def search_video():
    query = request.args.to_dict()
    video = Video(g.db)
    result = video.find_video(query)
    
    if result:
        result['_id'] = str(result['_id'])
        return jsonify(result), 200
    
    return jsonify({'error': 'Video not found'}), 404
