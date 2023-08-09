from abc import ABCMeta, abstractclassmethod, ABC
from app.models.model import DownloadModel
from app.services.model_downloader import ModelDownloader
from app.services.model_downloader import MultiThreadModelDownloader


class IModelDownloaderFactory(metaclass=ABCMeta):
    @classmethod
    @abstractclassmethod
    def create_downloader(cls) -> ModelDownloader:
        pass

class MultiThreadModelDownloaderFactory(IModelDownloaderFactory):
    @classmethod
    def create_downloader(cls, d_mode: str, download_models: list[DownloadModel], destination: str) -> ModelDownloader:
        if d_mode == 'multithread':
            return MultiThreadModelDownloader(download_models, destination)

        raise ValueError('value error.')


class IntroduceModel(ABC):
    download_models: list[DownloadModel]
    downloader: ModelDownloader

    def __init__(self, destination: str, download_mode: str = 'multithread') -> None:
        self.destination = destination
        self.download_mode = download_mode
        self.download_models = self._create_download_models()
        self.downloader = MultiThreadModelDownloaderFactory.create_downloader(self.download_mode, self.download_models, self.destination)

    @abstractclassmethod
    def _create_download_models(self) -> list[DownloadModel]:
        pass

class IntroduceLora(IntroduceModel):
    DEFAULT_DESTINATION = '/content/stable-diffusion-webui/models/Lora'

    def __init__(self, destination: str = '', download_mode: str = 'multithread') -> None:
        super().__init__(destination, download_mode)

        if not self.destination:
            self.destination = self.DEFAULT_DESTINATION

        else:
            self.destination = destination

        print('モデルの出力先->', self.destination)

    def _create_download_models(self) -> list[DownloadModel]:
        return [
            DownloadModel(
                download_model_url='https://civitai.com/api/download/models/61409',
                is_url_in_model_name=False,
                model_name='RyuunoOsigoto_lora.safetensors'
            ),
            DownloadModel(
                download_model_url='https://civitai.com/api/download/models/9409',
                model_name='Arona.safetensors'
            ),
            DownloadModel(
                download_model_url='https://civitai.com/api/download/models/62833',
                model_name='DetailTweaker.safetensors'
            )
        ]

