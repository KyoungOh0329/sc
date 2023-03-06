import os
import random
import shutil

# 이미지 파일이 저장된 디렉토리 경로
dir_path = "/path/to/directory"

# 랜덤으로 선택할 이미지 파일의 개수
num_files = 2000

# 디렉토리 내의 이미지 파일 리스트를 가져옴
file_list = os.listdir(dir_path)

# 무작위로 이미지 파일 리스트에서 num_files 개수만큼 파일을 선택
random_files = random.sample(file_list, num_files)

# 선택된 이미지 파일을 새로운 디렉토리에 복사
output_dir = "/path/to/output/directory"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file_name in random_files:
    src_file_path = os.path.join(dir_path, file_name)
    dst_file_path = os.path.join(output_dir, file_name)
    shutil.copyfile(src_file_path, dst_file_path)