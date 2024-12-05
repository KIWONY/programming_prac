import os
import psutil

def is_file_in_use(file_path):
    """
    특정 파일을 열고 있는 프로세스가 있는지 확인합니다.
    :param file_path: 확인할 파일 경로 (str)
    :return: 파일 사용 여부 (bool)
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        for proc in psutil.process_iter(['open_files', 'pid']):
            open_files = proc.info.get('open_files')
            if open_files:
                for file in open_files:
                    if file.path == file_path:
                        return True
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass  # 권한 문제나 프로세스 종료 시 무시

    return False


if __name__ == "__main__":
    # 확인할 PNG 파일 경로
    file_to_check = "path/to/your/file.png"

    try:
        in_use = is_file_in_use(file_to_check)
        if in_use:
            print(f"The file '{file_to_check}' is currently in use.")
        else:
            print(f"The file '{file_to_check}' is not in use.")
    except Exception as e:
        print(f"Error: {e}")
