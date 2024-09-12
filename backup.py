# cv2.imwrite('thermos_white_224x224.jpg',img_resize)
#  # 이미지 불러오기

   
   
# img1 = cv2.imread('dataArg/ex_1/thermos_wood.jpg')
# height, width = img.shape[:2]
# if img1 is None:
#    sys.exit('Image load failed')

# x = width  # 가로 중앙에서 좌우 100씩
# y = height  # 세로 중앙에서 위아래 100씩
# w = 200  # 자를 가로 길이
# h = 200  # 자를 세로 길이



# cropped_img = img1[y:y+h, x:x+w]
# # cv2.imwrite('cropped_image.jpg', cropped_img)
# cv2.imshow('Cropped Image', cropped_img)

# dataPath = os.path(os.getcwd(),'DataAug')
# dataOrg = os.path.join(dataPath,'org')
# fileName = os.path.join(dataOrg,'carkey_white.jpg')
# # print(fileName)
# img = cv2.imread(fileName)
# img_resize = cv2.resize(img,(224,224))
# cv2.imshow('resize',img_resize)
# cv2.waitKey()
# cv2.destroyAllWindows()