import datetime
from pathlib import Path

class Base():
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self,driver):
        self.driver =driver

    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print(f"Current url {get_url}")


    def assert_word(self, word, result):
        """Method assert word"""
        value_word = word.text
        assert value_word == result
        print('Good value word')

    def assert_url(self,result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')


    def get_screenshot(self):
        """Method Screenshot"""
        project_root = Path(__file__).resolve().parents[2]

        screen_dir = project_root / "main_project" / "screen"

        screen_dir.mkdir(parents=True, exist_ok=True)

        now_date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d.%H.%M.%S")
        file_name = f"screenshot_{now_date}.png"

        full_path = screen_dir / file_name

        success = self.driver.save_screenshot(str(full_path))
        print("Сделал скриншот")

        if not success:
            print(f"Ошибка сохранения скриншота по пути: {full_path}")



