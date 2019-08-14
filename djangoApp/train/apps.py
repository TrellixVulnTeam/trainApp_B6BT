from django.apps import AppConfig

class TrainConfig(AppConfig):
    name = 'train'

    def ready(self):
        # Pycharm does'nt recognize but it works
        import train.signals
