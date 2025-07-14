# # scanner.py
# import cv2
# import numpy as np
# import pytesseract
# import imutils
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# def scan_document(image_path):
#     image = cv2.imread(image_path)
#     orig = image.copy()
#     image = imutils.resize(image, height=500)
#
#     # Edge detection and contour finding
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (5, 5), 0)
#     edged = cv2.Canny(blur, 75, 200)
#
#     contours = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#     contours = imutils.grab_contours(contours)
#     contours = sorted(contours, key=cv2.contourArea, reverse=True)
#
#     doc_cnt = None
#     for c in contours:
#         peri = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#         if len(approx) == 4:
#             doc_cnt = approx
#             break
#
#     if doc_cnt is None:
#         return None, "No document found."
#
#     def reorder(pts):
#         pts = pts.reshape(4, 2)
#         rect = np.zeros((4, 2), dtype="float32")
#         s = pts.sum(axis=1)
#         rect[0] = pts[np.argmin(s)]
#         rect[2] = pts[np.argmax(s)]
#         diff = np.diff(pts, axis=1)
#         rect[1] = pts[np.argmin(diff)]
#         rect[3] = pts[np.argmax(diff)]
#         return rect
#
#     rect = reorder(doc_cnt)
#     (tl, tr, br, bl) = rect
#     width = max(int(np.linalg.norm(br - bl)), int(np.linalg.norm(tr - tl)))
#     height = max(int(np.linalg.norm(tr - br)), int(np.linalg.norm(tl - bl)))
#
#     dst = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype="float32")
#     M = cv2.getPerspectiveTransform(rect, dst)
#     scanned = cv2.warpPerspective(orig, M, (width, height))
#
#     text = pytesseract.image_to_string(cv2.cvtColor(scanned, cv2.COLOR_BGR2GRAY))
#
#     scanned_path = image_path.replace(".png", "_scanned.png")
#     cv2.imwrite(scanned_path, scanned)
#
#     return scanned_path, text
from PIL import Image
import pytesseract

# Update path to Tesseract executable if needed (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def scan_document(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return image_path, text
    except Exception as e:
        print("Error during OCR:", e)
        return None, ""
