FROM  bvlc/caffe:cpu
COPY nsfw_model /workspace/nsfw_model
COPY classify_nsfw.py /workspace
RUN mkdir -p /root/.pip/
COPY pip.conf /root/.pip/pip.conf
RUN pip install Flask && pip install nltk && pip install jieba && pip install PyMySQL && pip install sqlalchemy \
    && pip install flask_sqlalchemy && pip install flask_jsontools && pip install redis && pip install gevent \
    && rm -rf /root/.cache/pip
COPY classify_nsfw_rest_api.py /workspace
COPY config.py /workspace
COPY rest_api.py /workspace
RUN mkdir -p /workspace/utils
RUN mkdir -p /workspace/route
COPY utils /workspace/utils
COPY route /workspace/route
CMD ["python", "./rest_api.py"]
EXPOSE 5000