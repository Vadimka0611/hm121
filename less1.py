import codecs
import re


def delete_html_tags(html_file, result_file="cleaned.txt"):
    with codecs.open(html_file, "r", "utf-8") as file:
        result = []
        for line in file:
            current_text_list = re.findall(r">(.+)</", line)
            if len(current_text_list) > 0:
                result += current_text_list
        print(f"Result: {result}")
        if len(result) > 0:
            with open(result_file, "w", encoding= "utf-") as new_file:
                    new_file.write("\n".join(result))


delete_html_tags("draft.html")