import dataclasses

@dataclasses.dataclass
class DownloadModelURL:
    download_model_url: str

    def __str__(self) -> str:
        return self.download_model_url

@dataclasses.dataclass
class DownloadModel:
    download_model_url: DownloadModelURL
    is_url_in_model_name: bool
    model_name: str

    def __init__(
        self,
        download_model_url: DownloadModelURL | str,
        is_url_in_model_name: bool = False,
        model_name: str = None
    ) -> None:
        if not isinstance(download_model_url, DownloadModelURL):
            download_model_url = DownloadModelURL(download_model_url)

        self.download_model_url = download_model_url
        self.is_url_in_model_name = is_url_in_model_name
        self.model_name = self.configure_model_name(model_name)

    def configure_model_name(self, model_name: str) -> str:
        if self.is_url_in_model_name:
            return self.download_model_url.download_model_url.split('/')[-1]

        if not model_name:
            raise ValueError('モデル名を定義するか、is_url_in_model_nameのデフォルト値をTrueにしてください。')

        return model_name

    def get_model_download_url(self) -> str:
        return str(self.download_model_url)


