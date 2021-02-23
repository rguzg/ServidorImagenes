import cv2
import numpy as np

#REQUIERE DE OPENCV INSTALADO PARA SU CORRECTO FUNCIONAMIENTO
#La función recibe dos imagenes y verifica que sean del mismo tamaño y que sean iguales en el 100% de sus pixeles 
def CompararImagen(img1,img2):
    #Lectura de Imagens
    
    # Imagen que el usuario ingresa al servidor
    Original = cv2.imread(img1)

    #Imagen que regresa el servidor
    Nueva = cv2.imread(img2)
    

    #Verificación de tamaños iguales
    if(Original.shape==Nueva.shape):
        
        #Diferencias entre imagen 1 e imagen 2 
        #La diferencia ente dos imagenes iguales resulta en pixeles negros
        difference = cv2.subtract(Original,Nueva)

        #Se separan en los diversos canales de colores
        b,g,r = cv2.split(difference)
        
        #Se utiliza la funcion countNonZero para contar la cantidades de pixeles que no son negros

        if(cv2.countNonZero(b)<100000 and cv2.countNonZero(g)<100000 and cv2.countNonZero(r)<100000):
            print(" EXITO Las imagenes Son iguales")
            cv2.imshow("Original",Original)
            cv2.imshow("Recibida por el Servidor",Nueva)
            cv2.imshow("differencias",difference)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            
            print(cv2.countNonZero(b))
            print(cv2.countNonZero(g))
            print(cv2.countNonZero(r))
            print("ERROR las imagenes no son iguales")
            cv2.imshow("Original",Original)
            cv2.imshow("Recibida por el Servidor",Nueva)
            cv2.imshow("differencias",difference)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print("ERROR las imagenes no son iguales")
        print("No tienen el mismo tamaño de imagen")


# img1 = r'C:\Users\emili\Desktop\ServidorImagenes\ChecarImagenesFinal\11.png'
# img2 = r'C:\Users\emili\Desktop\ServidorImagenes\ChecarImagenesFinal\22.png'

# CompararImagen(img1,img2)