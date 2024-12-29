def escape_markdown(text: str, version: int = 2) -> str:
    """
    Экранирует специальные символы для Markdown или MarkdownV2.
    :param text: Текст, который нужно экранировать.
    :param version: Версия Markdown (1 или 2). По умолчанию 2.
    :return: Экранированный текст.
    """
    if version == 1:
        escape_chars = r"_*`["
    elif version == 2:
        escape_chars = r"_*[]()~`>#+-=|{}.!"
    else:
        raise ValueError("Invalid Markdown version. Use 1 or 2.")

    return "".join(f"\\{char}" if char in escape_chars else char for char in text)
