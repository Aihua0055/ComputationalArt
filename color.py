
import os
from flask import Flask, render_template, Blueprint, request, current_app
from wheel import harmonize_image

# Use Blueprint to create color harmonization component.
colorhar_page = Blueprint('colorhar_page', __name__,
                          template_folder='templates')

ALLOWED_EXTENSIONS = set(['.png','.jpg','.jpeg','.gif'])

@colorhar_page.route('/colorhar', methods=['GET', 'POST'])
def colorhar():
    # Render jumbotron in both GET and POST request. 
    kwargs = {
        'title': 'Color Harmonization',
        'jumbotron': {
            "header": "Color Harmonization",
            "bg_image": "static/images/colorHarJ.jpg",
            "text": "Research paper:https://igl.ethz.ch/projects/color-harmonization/harmonization.pdf"
        }
    }
    
    if request.method == 'GET':
        return render_template('colorhar.html', **kwargs)
    # Harmonize photos of user upload
    elif request.method == 'POST':
        # Folder to store upload images to local
        uploads_dir = "static/colorhar_results/uploads/"
        # Folder to store processed images to local
        results_dir = "static/colorhar_results/results/"

        # create image directory if not found
        if not os.path.isdir(uploads_dir):
            os.mkdir(uploads_dir)

        # retrieve file from html file-picker
        upload = request.files.getlist("file")[0]
        current_app.logger.debug(f"File name: {upload.filename}")
        filename = upload.filename

        # file support verification
        ext = os.path.splitext(filename)[1]
        current_app.logger.debug(f"ext={ext}")
        if ext in ALLOWED_EXTENSIONS:
            current_app.logger.debug("File accepted")
        else:
            return render_template("error.html", message="The selected file is not supported"), 400

        # save file
        destination = os.path.join(uploads_dir, filename)
        current_app.logger.debug(f"File saved to to:{destination}")
        upload.save(destination)
        kwargs['image_name'] = destination
        current_app.logger.debug(f"destination={destination}")

        # pass path of result image to template
        image_fpath_harmonized = os.path.join(results_dir, filename)
        # Append result_image_path to Kwargs
        kwargs['result_image_name']= image_fpath_harmonized

        # pass harmony score to templage: the lower the harmony score, the more harmony the color is .
        img_score_size = 30.
        img_ret_size = 300.
        current_app.logger.debug(f"The shorter edge will be resize to {img_ret_size}.")
        har_result = harmonize_image(destination, image_fpath_harmonized, img_score_size=img_score_size, img_ret_size=img_ret_size)
        
        # append har_result to Kwargs
        kwargs.update(har_result)

        return render_template('colorhar.html', **kwargs)
