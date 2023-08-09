from app.models.model import DownloadModel, DownloadModelURL
import pathlib
import pytest
import os

class TestDownloadModel:

    @classmethod
    def setup_class(cls):
        cls.ex_model1 = DownloadModel(
        download_model_url='https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/VAEs/orangemix.vae.pt',
        is_url_in_model_name=True
    )

    def test_get_download_model(self):
        assert self.ex_model1.is_url_in_model_name == True
        assert self.ex_model1.get_model_download_url() == 'https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/VAEs/orangemix.vae.pt'

