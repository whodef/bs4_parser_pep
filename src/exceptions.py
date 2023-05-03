class ParserFindTagException(Exception):
    """Выбрасывается исключение для парсера не нашедшего тег."""
    pass


class ResponseIsEmptyException(Exception):
    """Исключение для пустого response."""
    pass
