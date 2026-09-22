# procode-task: CH-PATH-PARAMS-TASK1-EXTRACT-COURSE-ID@1
# path = "/courses/5/"


def extract_course_id(path: str):
    path_splitted = path.split("/")
    result = None

    if len(path_splitted) == 3 and path.startswith("/courses"):
        try:
            result = int(path_splitted[2])
        except ValueError:
            pass

    return result

   

# print(extract_course_id(path))