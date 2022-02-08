#!/usr/bin/env python3

"""
타겟 클릭 시 이미지(가장 최근에 캡쳐된 이미지 파일)를 출력하는 함수
A function that outputs the target image(most recently captured image file) when target is clicked.
"""

import os


def newest_show(path: str):
    """
    Return name of the most recently created or modified file.
    :param path: target path
    :return: Recent target file name.
    """
    files_path = path
    file_name_and_time_lst = []
    for f_name in os.listdir(f"{files_path}"):
        written_time = os.path.getctime(f"{files_path}{f_name}")
        file_name_and_time_lst.append((f_name, written_time))
    sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
    recent_file = sorted_file_lst[0]
    recent_file_name = recent_file[0]

    return recent_file_name
