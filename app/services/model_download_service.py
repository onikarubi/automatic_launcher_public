from abc import ABC, abstractclassmethod
from app.models.model import DownloadModel
from concurrent.futures import ThreadPoolExecutor
import requests
import logging
import os
import tqdm
import sys

class ModelDownloadService(ABC):
    def __init__(
        self,
        download_models: list[DownloadModel],
        destination: str,
        chunk: int = 1024
    ) -> None:
        self.download_models = download_models
        self.destination = destination
        self.chunk = chunk

        if not os.path.isdir(self.destination):
            self._create_dir()

    def _get_model_dest_path(self, model: DownloadModel) -> str:
        if model.is_url_in_model_name:
            file_name = model.get_model_download_url().split('/')[-1]
            combined_path = os.path.join(self.destination, file_name)

        else:
            combined_path = os.path.join(self.destination, model.model_name)

        return combined_path

    def _save_model(self, model: DownloadModel) -> None:
        dest_path = self._get_model_dest_path(model)
        res = requests.get(model.download_model_url, stream=True)
        total_size_in_bytes = int(res.headers.get('content-length', 0))

        with tqdm.tqdm(total=int(total_size_in_bytes / self.chunk), unit='KB', unit_scale=True, file=sys.stdout, desc=model.model_name) as pbar:
            with open(dest_path, 'wb') as f:
                for data in res.iter_content(chunk_size=self.chunk):
                    f.write(data)
                    pbar.update(1)
                    f.flush()

    def _create_dir(self):
        try:
            os.mkdir(self.destination)

        except Exception as e:
            raise e

    @abstractclassmethod
    def run(self) -> None:
        pass

class ModelMultiThreadDownloadService(ModelDownloadService):
    def run(self) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

        with ThreadPoolExecutor() as executor:
            for download_model in self.download_models:
                executor.submit(self._download_thread, download_model)

            executor.shutdown(wait=True)
        logging.debug('All tasks have been completed.')

    def _download_thread(self, model: DownloadModel):
        
        logging.debug(f'started {model.model_name} download.')
        self._save_model(model)
        logging.debug(f'Completed {model.model_name} download.')


