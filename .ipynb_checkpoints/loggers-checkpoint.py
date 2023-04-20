import logging


class ResultsLogger:

    def __init__(self, file='results_log'):
        self.file = file
        self.logger = logging.getLogger(file)
        self.logger.setLevel('INFO')

        self.fhandler = logging.FileHandler(filename=f'{file}.log', mode='a')
        self.logger.addHandler(self.fhandler)

        self.formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        self.fhandler.setFormatter(self.formatter)

    def log_result(self, **kwargs):
        msg = f'Results:\n'
        for key, value in kwargs.items():
            text = ' '.join(str(value).split())
            msg += f'    {key}: {text},\n'

        self.logger.info(msg)
