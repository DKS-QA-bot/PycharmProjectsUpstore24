import datetime
from pathlib import Path

class Base():
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self,driver):
        self.driver =driver


    """Method Get current url"""
    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    def assert_url(self,result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')

    """Method Screenshot"""
    def get_screenshot(self):
        # Определяем корень проекта (на уровень выше папки main_project/tests)
        project_root = Path(__file__).resolve().parents[2]

        # Собираем путь до папки screen внутри вашего проекта
        screen_dir = project_root / "main_project" / "screen"

        # Гарантируем, что папка существует
        screen_dir.mkdir(parents=True, exist_ok=True)

        # Формируем имя файла БЕЗ лишних пробелов
        now_date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d.%H.%M.%S")
        file_name = f"screenshot_{now_date}.png"

        # Полный путь
        full_path = screen_dir / file_name

        # Selenium принимает строку, поэтому преобразуем объект Path в строку
        success = self.driver.save_screenshot(str(full_path))

        if not success:
            print(f"Ошибка сохранения скриншота по пути: {full_path}")
    # def get_screenshot(self):
    #     now_date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d.%H.%M.%S")
    #     name_screenshot = f'screenshot {now_date} .png'
    #     self.driver.save_screenshot("C:\\Users\\DKS\\PycharmProjects\\pythonProjectSwag\\main_project\\screen" + name_screenshot)


