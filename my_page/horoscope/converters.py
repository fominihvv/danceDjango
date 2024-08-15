class SplitConverter:
    regex = '[\w,]+'

    @staticmethod
    def to_python(value: str) -> list:
        return list(value.split(','))

    @staticmethod
    def to_url(value: list[str]) -> str:
        return ','.join(value)


class UpperConverter:
    regex = '[\w]+'

    @staticmethod
    def to_python(value: str) -> str:
        return value.upper()

    @staticmethod
    def to_url(value: str) -> str:
        return value.lower()
