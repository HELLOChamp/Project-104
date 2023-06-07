import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, 
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1.0,
            (255,255,255)
            )
cv2.putText(img, 
            "Mercury",
            (100,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.7,
            (255,255,255)
            )
cv2.putText(img, 
            "Venus",
            (170,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255)
            )
cv2.putText(img, 
            "Earth",
            (280,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255)
            )
cv2.putText(img, 
            "Mars",
            (380,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255)
            )
cv2.putText(img, 
            "Jupiter",
            (480,370),
            cv2.FONT_HERSHEY_COMPLEX,
            1.0,
            (255,255,255)
            )
cv2.putText(img, 
            "Saturn",
            (740,310),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255)
            )
cv2.putText(img, 
            "Uranus",
            (950,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255)
            )
cv2.putText(img, 
            "Neptune",
            (1100,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255)
            )

cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)