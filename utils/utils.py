import os
import sys

from exception.exception import CustomException
from logger.logging import logging
import pickle


def save_object(obj, file_path: str):

    try:
        os.makedirs(os.path.dirname(file_path),exist_ok =True)

        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)

