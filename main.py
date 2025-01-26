import cv2
import face_recognition

def capture_user_image():
    # 웹캠 캡처
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 웹캠에서 캡처한 이미지를 RGB로 변환
        rgb_frame = frame[:, :, ::-1]  # OpenCV는 BGR 형식, face_recognition은 RGB 형식 필요

        # 얼굴 인식
        face_locations = face_recognition.face_locations(rgb_frame)

        # 얼굴에 사각형 표시
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 얼굴 인식 결과 보여주기
        cv2.imshow('Face Recognition', frame)

        # 키 입력 대기
        key = cv2.waitKey(1) & 0xFF

        # 'c' 키를 누르면 캡처
        if key == ord('c'):
            img_name = "captured_image.png"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} 저장 완료!")

        # 'q' 키를 누르면 종료
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    capture_user_image()