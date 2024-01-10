import cv2
import numpy as np
import time

def count_target_images(main_image_path, target_image_paths):
    # 메인 이미지와 타겟 이미지 로드
    main_image = cv2.imread(main_image_path)

    lists = []
    for target_image_path in target_image_paths :
        target_image = cv2.imread(target_image_path)
        # 타겟 이미지의 높이와 너비
        target_height, target_width = target_image.shape[:2]

        # 템플릿 매칭 수행
        result = cv2.matchTemplate(main_image, target_image, cv2.TM_CCOEFF_NORMED)

        # 일정 유사도 이상의 위치 찾기
        threshold = 0.8
        obj = {
            "target_height" : target_height,
            "target_width" : target_width,
            "loc" : np.where(result >= threshold)
        }
        lists.append(obj)


    # 타겟 이미지가 등장한 횟수 계산
    # for obj in lists :
        # print(obj["loc"])
        # for pt in zip(*obj["loc"][::-1]):
        #     print(pt)
        #     bottom_right = (pt[0] + obj["target_width"], pt[1] + obj["target_height"])
        #     print(bottom_right)
        #
        #     cv2.rectangle(main_image, pt, bottom_right, (0, 255, 0), 2)

    # cv2.imwrite("res/log/test.bmp", main_image)


if __name__ == "__main__":
    main_image_path = "res/log/1.bmp"
    target_image_paths = ["res/m2.png","res/m1.png"]
    start_time = time.time()
    target_count = count_target_images(main_image_path, target_image_paths)
    end_time = time.time()
    execution_time = end_time - start_time
    print(execution_time)
    print(f"The target image appears {target_count} times in the main image.")
