import re
import codecs


def delete_html_tags(html_file: str, result_file: str = "cleaned.txt"):

    with codecs.open(html_file, 'r', encoding='utf-8') as file:
        html_text = file.read()
    print(f"Файл '{html_file}' успішно прочитано.")

    cleaned_text = re.sub(r'<[^>]*>', '', html_text)
    print("HTML-теги видалено.")

    with codecs.open(result_file, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_text)
    print(f"Очищений текст успішно записано у файл '{result_file}'.")
    return True