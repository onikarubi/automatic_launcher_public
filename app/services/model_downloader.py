from abc import ABCMeta, abstractclassmethod
from app.models.model import DownloadModel
from .model_download_service import ModelMultiThreadDownloadService
import pathlib


class ModelDownloader(metaclass=ABCMeta):
    def __init__(self, models: list[DownloadModel], destination: str = '') -> None:
        self.models = models

        if not destination:
            raise ValueError('ダウンロード先のパスが指定されていません')

        self.destination = pathlib.Path(destination)

    def add_use_model(self, model: DownloadModel):
        self.models.append(model)

    @abstractclassmethod
    def download(self) -> None:
        pass


class MultiThreadModelDownloader(ModelDownloader):
    def __init__(self, models: list[DownloadModel], destination: str) -> None:
        super().__init__(models, destination)
        print('モデルのダウンロード先(model) ->', self.destination, 'end')

    def download(self) -> None:
        service = ModelMultiThreadDownloadService(self.models, self.destination)
        service.run()



