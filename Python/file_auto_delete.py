import os
import sys
import time
import shutil
from datetime import datetime


diskLabel = 'D:\\'
total, used, free = shutil.disk_usage(diskLabel)

# Create Folders in D:\\Test\mask, target, vista
basepath = diskLabel + 'Test'
mask = os.path.join(basepath, 'mask')
target = os.path.join(basepath, 'target')
vista = os.path.join(basepath, 'vista')

os.makedirs(mask, exist_ok=True)
os.makedirs(target, exist_ok=True)
os.makedirs(vista, exist_ok=True)


def byte_transform(bytes, to, bsize=1024):
    """Unit conversion of byte received from shutil

    :return: Capacity of the selected unit (int)
    """
    unit = {'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4}
    r = float(bytes)
    for i in range(unit[to]):
        r = r / bsize
    return int(r)


def delete_oldest_files(path, minimum_storage_GB: int):
    is_old = {}

    if minimum_storage_GB <= byte_transform(free, 'GB'):

        for f in os.listdir(path):
            i = os.path.join(path, f)
            is_old[f'{i}'] = int(os.path.getmtime(i))

        # is_old.sort()

        value = list(is_old.values())
        print()
        print(is_old)
        print(value)
        try:
            # os.remove(is_old[0])
            pass
        except IndexError:
            print('File auto delete complete.')
            sys.exit()

    else:
        print('Already you have enough storage.')
        sys.exit()


if __name__ == "__main__":

    print("D 드라이브 총 공간: ", byte_transform(total, 'GB'), "GB")
    print("D 드라이브 사용 공간: ", byte_transform(used, 'GB'), "GB")
    print("D 드라이브 남은 공간: ", byte_transform(free, 'GB'), "GB")
    print('')

    try:
        storage = int(input('Enter the storage space(GB) you want: '))
    except ValueError:
        print('Enter it in the form of int')
        sys.exit()

    # while storage < byte_transform(free, 'GB'):
    delete_oldest_files('D:\\Test/vista', minimum_storage_GB=storage)
