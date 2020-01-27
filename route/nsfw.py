# -*- coding:utf-8 -*-
from config import app
from utils.function import *
from flask import request
from flask import render_template
from flask import session, url_for, redirect
from utils import request_tuils
from classify_nsfw_rest_api import classify as nsfw_classify
import logging
import base64

logger = logging.getLogger(__name__)


@app.route("/yahoo_nsfw/classify", methods=["GET", "POST"])
def classify():
    logger.info("classify")
    image_byte = request.files.get('file').read()
    # image_base64 = request.form.get("image_base64")
    # logger.info(image_base64)
    # image_byte = base64.b64decode(image_base64)
    # logger.info(image_byte)
    s = nsfw_classify(image_byte)
    return response_success(s)

