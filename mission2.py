import cv2
import numpy as np

# 글로벌 변수 설정
drawing = False  # 마우스를 누르고 있는지 확인
mode = 'rectangle'  # 기본 모드: 사각형 (왼쪽 클릭 시)
ix, iy = -1, -1  # 마우스를 누른 초기 좌표 저장

# 마우스 콜백 함수
def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode, img

    # 마우스 왼쪽 버튼 클릭 시 다각형 그리기 시작
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # 마우스를 움직이는 동안, 그리기 중일 때 임시 이미지를 그려 화면에 보여줌
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_img = img.copy()
            if mode == 'rectangle':
                cv2.rectangle(temp_img, (ix, iy), (x, y), (255, 0, 0), 2)
            elif mode == 'triangle':
                pts = np.array([[ix, iy], [(x + ix) // 2, y], [x, iy]], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(temp_img, [pts], True, (0, 255, 0), 2)
            cv2.imshow('draw', temp_img)

    # 마우스 왼쪽 버튼 떼면 다각형 그리기 완료
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == 'rectangle':
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)
        elif mode == 'triangle':
            pts = np.array([[ix, iy], [(x + ix) // 2, y], [x, iy]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (0, 255, 0), 2)
        cv2.imshow('draw', img)

    # 마우스 오른쪽 버튼 클릭 시 원 그리기 시작
    elif event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # 마우스 오른쪽 버튼 떼면 원 그리기 완료
    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        radius = int(np.sqrt((x - ix) ** 2 + (y - iy) ** 2))
        cv2.circle(img, (ix, iy), radius, (0, 255, 255), 2)
        cv2.imshow('draw', img)

# 이미지 초기화 및 윈도우 생성
img = np.ones((512, 512, 3), np.uint8) * 255
cv2.namedWindow('draw')
cv2.setMouseCallback('draw', draw_shape)

# 메인 루프
while True:
    cv2.imshow('draw', img)
    key = cv2.waitKey(1) & 0xFF

    # 모드 전환 ('m'을 누르면 삼각형/사각형 전환)
    if key == ord('m'):
        if mode == 'rectangle':
            mode = 'triangle'
        else:
            mode = 'rectangle'

    # 'r' 키를 누르면 이미지 초기화
    elif key == ord('r'):
        img = np.ones((512, 512, 3), np.uint8) * 255

    # 'q' 키를 누르면 종료
    elif key == ord('q'):
        break

# 리사이징 전 원본 이미지 저장
original_img = img.copy()

# 다양한 보간법을 사용한 리사이징
resized_nearest = cv2.resize(original_img, (256, 256), interpolation=cv2.INTER_NEAREST)
resized_area = cv2.resize(original_img, (256, 256), interpolation=cv2.INTER_AREA)
resized_cubic = cv2.resize(original_img, (256, 256), interpolation=cv2.INTER_CUBIC)
resized_lanczos = cv2.resize(original_img, (256, 256), interpolation=cv2.INTER_LANCZOS4)

# 결과 이미지들 출력
cv2.imshow('Original Image', original_img)
cv2.imshow('Resized - INTER_NEAREST', resized_nearest)
cv2.imshow('Resized - INTER_AREA', resized_area)
cv2.imshow('Resized - INTER_CUBIC', resized_cubic)
cv2.imshow('Resized - INTER_LANCZOS4', resized_lanczos)




original_img = img.copy()

# --- 부드럽게 필터링(GaussianBlur) 후 리사이징 ---
# 필터링 적용
blurred_img = cv2.GaussianBlur(original_img, (5, 5), 0)

# 다양한 보간법을 사용한 리사이징
resized_nearest = cv2.resize(blurred_img, (256, 256), interpolation=cv2.INTER_NEAREST)
resized_area = cv2.resize(blurred_img, (256, 256), interpolation=cv2.INTER_AREA)
resized_cubic = cv2.resize(blurred_img, (256, 256), interpolation=cv2.INTER_CUBIC)
resized_lanczos = cv2.resize(blurred_img, (256, 256), interpolation=cv2.INTER_LANCZOS4)

# --- 필터링을 적용하지 않은 원본 이미지도 리사이징하여 비교 ---
resized_nearest_orig = cv2.resize(original_img, (256, 256), interpolation=cv2.INTER_NEAREST)
resized_area_orig = cv2.resize(original_img, (256, 256), interpolation=cv2.INTER_AREA)

# 결과 이미지들 출력
cv2.imshow('Original Image', original_img)
cv2.imshow('Filtered Image', blurred_img)
cv2.imshow('Resized - INTER_NEAREST', resized_nearest)
cv2.imshow('Resized - INTER_AREA', resized_area)
cv2.imshow('Resized - INTER_CUBIC', resized_cubic)
cv2.imshow('Resized - INTER_LANCZOS4', resized_lanczos)
cv2.imshow('Resized (no filter) - INTER_NEAREST', resized_nearest_orig)
cv2.imshow('Resized (no filter) - INTER_AREA', resized_area_orig)



cv2.waitKey(0)
cv2.destroyAllWindows()

