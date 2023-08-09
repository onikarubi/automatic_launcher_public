from app.services.factory.model_downloader_factory import IntroduceLora

if __name__ == '__main__':
    lora = IntroduceLora(destination='./models')
    lora.downloader.download()

