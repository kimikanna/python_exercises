# Откройте и прочитайте данные с файла lorum.txt, способом, который рассматривается в видео

try:
    file = open('task_1/lorum.txt', 'a+')
    file.write('\n\nhello, world!')
    file.seek(0)
    print(file.read())
except Exception:
    print("Произошла ошибка")
finally:
    file.close()
