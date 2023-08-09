from typing import Any
from app.models.model import DownloadModel
from app.services.model_downloader import ModelDownloader, MultiThreadModelDownloader, DownloadModel
from app.services.factory.model_downloader_factory import IntroduceLora
import os

class TestModelDownloader:
    @classmethod
    def setup_class(cls):
        cls.multithread_models = [
            DownloadModel(
                download_model_url='https://civitai.com/api/download/models/61409',
                model_name='sample_lora.safesors'
            ),
        ]
        cls.multithread_downloader = MultiThreadModelDownloader(
            models=cls.multithread_models,
        )

    def test_add_model_downloader(self):
        add_model = DownloadModel(download_model_url='hogehoge', is_url_in_model_name=False, model_name='hoge model')

        initialize_model_nums = len(self.multithread_downloader.models)
        self.multithread_downloader.add_use_model(add_model)
        assert len(self.multithread_downloader.models) == initialize_model_nums + 1
        assert_target_model = self.multithread_downloader.models.pop()
        assert assert_target_model == add_model
        assert len(self.multithread_downloader.models) == initialize_model_nums


class TestMultiThreadModelDownloader:
    @classmethod
    def setup_method(cls):
        cls.lora = IntroduceLora()

    def test_get_properties(self):
        assert self.lora.destination == self.lora.DEFAULT_DESTINATION
        assert self.lora.download_mode == 'multithread'

    def test_download_models(self, tmpdir):
        self.lora.downloader.download(tmpdir)
        assert os.path.exists(tmpdir) is True

