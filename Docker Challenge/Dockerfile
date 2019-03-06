FROM python:3
ADD hashDigestController.py /
ADD hashDigestService.py /
RUN pip install Flask
RUN pip install Flask-Restful
RUN pip install Flask-Jsonpify
CMD [ "python", "./hashDigestController.py" ]