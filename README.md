# Computational Art Studio
Computational Art Studio written in Python, Flask as web Framework,Deep AI style transfer API for Style Transfer.

Main functions:
* Style Transfer 
* Color Harmonization [Colour Harmony a video on Youtube](https://www.youtube.com/watch?v=4LhcNbFMkTw) | [A Youtube video about color theory](https://www.youtube.com/watch?v=_2LLXnUdUIc)
* Gallery of Style Transfer.
* About page sparks thinking about AI and art.
 
[A Live Demo](https://computationalartstudio.herokuapp.com/) has been deployed to Heroku.
Please try it out, and have fun.

[Your feedback is valuable for us grow, or join us and we can do it together](https://forms.gle/jSujZZMwUCouGzYg6)
 
## Getting started
This project includes three Python files:
* `app.py`: for route to different pages and style transfer and gallery function.
* `color.py`: Blueprint (or module) for color harmonization function. Process GET request and return color harmonization page. Process POST request to harmonize the image user upload. 
* `wheel.py`: A color harmonization API written in Python. Please check this research paper [link](https://igl.ethz.ch/projects/color-harmonization/harmonization.pdf
) for more details about color harmonization. 
* `templates`: Jinja2 html templates. 
* `static/colorhar_results`: uploads folder to store images user will upload for color harmonization. results folder to store result images of color harmonization.
 
Other files have been included for Heroku deployment: `requirements.txt`, `Aptfile`and `Procfile`.
 
## Dependencies
`flask` with its dependencies (`werkzeug`, `jinja2`, `markupsafe`, `itsdangerous`), It is recommended to use the provided `requirements.txt` file:
```
sudo pip install -r requirements.txt
```
 
 ## Tech Stack
 * Bootstrap for CSS Framework
 * Jinja2 for html templates
 * Flask for web framework
 * Firebase for image storage for style transfer and gallery module
## Run local
To test the app locally, run `FLASK_ENV=development FLASK_APP=app.py python -m flask run` and then you will find a link in your console, use ctrl + click to open that link in your browser.
 
Use the `Browse` button to upload the desired image.
 
If successful, you will be able to preview your uploaded image on the same page.
 
* For color harmonization, your uploaded image and the processed image will be provided to you at the same time.
 
* For Style transfer, you will see a button show up along with your uploaded image, and then you can click on that button, and after about 15 seconds, you will see the result image(Your uploaded image in Van Gogh Starry Night style).
 
* In the Gallery page, you will see 30 pokemon images in Van Gogh Starry Night style.

## Reference
* [Color Harmonization Research Paper](https://igl.ethz.ch/projects/color-harmonization/harmonization.pdf)
* [A youtube video showing color harmonization technique](https://www.youtube.com/watch?v=DvrUYtLju4Y)
 
## Thanks
* Our starter code [image-api](https://github.com/gxercavins/image-api) .
* [Deep AI](https://deepai.org/machine-learning-model/fast-style-transfer)
* [Flask official documentation](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja2 documentation](https://jinja.palletsprojects.com/en/2.11.x/)
* [Bootstrap](https://getbootstrap.com/)
* Feng Liu and Qiqi Hou for exposure author to Color Harmonization
 
## Inspiration
* [Google Arts & Culture](https://artsandculture.google.com/)
* [How old do I look](https:www.how-old.net/)
* [Make Me zombie](http://makemezombie.com/)

## Issues
Report any issue to the GitHub issue tracker. Email aihuacville@gmail.com for color harmonization API.
 
 
 




