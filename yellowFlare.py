import sys

import os.path
import cv2
import numpy as np
import time

def emptyFunction(void):
	pass
	
def adjust_gamma(image, gamma=1.0):
	if gamma!=0:
	
		# build a lookup table mapping the pixel values [0, 255] to
		# their adjusted gamma values
		invGamma = 1.0 / gamma
		table = np.array([((i / 255.0) ** invGamma) * 255
			for i in np.arange(0, 256)]).astype("uint8")
		# apply gamma correction using the lookup table
		return cv2.LUT(image, table)
	return img
def main():
	cv2.namedWindow('Gamma Correction',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Correction',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Auto White Balance',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Clahe',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Clahe LAB',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Gaussian',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Anisotropic Diffusion',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Median Blur',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Median Blur 2',cv2.WINDOW_NORMAL)
	cv2.namedWindow('YCrCb Median Blur',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Output',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Thresh Output',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Video',cv2.WINDOW_NORMAL)
	
	cv2.resizeWindow('Video',500,500)
	cv2.resizeWindow('Clahe',500,500)
	cv2.resizeWindow('Clahe LAB',500,500)
	cv2.resizeWindow('Gaussian',500,500)
	cv2.resizeWindow('Anisotropic Diffusion',500,500)
	cv2.resizeWindow('Median Blur',500,500)
	cv2.resizeWindow('Median Blur 2',500,500)
	cv2.resizeWindow('YCrCb Median Blur',500,500)
	cv2.resizeWindow('Output',500,500)
	cv2.resizeWindow('Thresh Output',500,500)
	
	imgpath = "/home/charmi/Desktop/Trident_Work/OpenCV/Output/SavedVideos2/Output15.avi"
	'''
	a ='/home/charmi/Desktop/Trident_Work/OpenCV/Output/SavedVideos/OutputThresh'
	b =1
	c = '.avi'
	filename = a+str(b)+c
	#d ='/home/charmi/Desktop/Trident_Work/OpenCV/Output/SavedVideos/Output'
	#filename2=d+str(b)+c
	while(os.path.exists(filename)):
		b+=1
		filename = a+str(b)+c
		#filename2=d+str(b)+c
	codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
	framerate = 10
	resolution = (640, 480)
	VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)
	#VideoFileOutput2 = cv2.VideoWriter(filename2, codec, framerate, resolution)
	'''
	
	cv2.createTrackbar('+ve Gamma','Gamma Correction',1,20,emptyFunction)
	cv2.createTrackbar('-ve Gamma','Gamma Correction',0,20,emptyFunction)
	cv2.createTrackbar('Hue','Correction',1,200,emptyFunction)
	cv2.createTrackbar('Saturation','Correction',1,200,emptyFunction)
	cv2.createTrackbar('Value','Correction',1,200,emptyFunction)
	cv2.createTrackbar('Low H','Thresh Output',0,180,emptyFunction)
	cv2.createTrackbar('Low S','Thresh Output',0,255,emptyFunction)
	cv2.createTrackbar('Low V','Thresh Output',0,255,emptyFunction)
	cv2.createTrackbar('High H','Thresh Output',0,360,emptyFunction)
	cv2.createTrackbar('High S','Thresh Output',0,255,emptyFunction)
	cv2.createTrackbar('High V','Thresh Output',0,255,emptyFunction)
	cv2.createTrackbar('Kernel Size','YCrCb Median Blur',3,15,emptyFunction)
	cv2.createTrackbar('Laplacian ksize','Output',3,15,emptyFunction)
	cv2.createTrackbar('Clip Limit (Blue)','Clahe',0,100,emptyFunction)
	cv2.createTrackbar('Tile Grid Size (Blue)','Clahe',1,20,emptyFunction)
	cv2.createTrackbar('Clip Limit (Green)','Clahe',0,100,emptyFunction)
	cv2.createTrackbar('Tile Grid Size (Green)','Clahe',1,20,emptyFunction)
	cv2.createTrackbar('Clip Limit (Red)','Clahe',0,100,emptyFunction)
	cv2.createTrackbar('Tile Grid Size (Red)','Clahe',1,20,emptyFunction)
	cv2.createTrackbar('Pair','Clahe',0,1,emptyFunction)
	cv2.createTrackbar('Kernel Size','Gaussian',3,15,emptyFunction)
	cv2.createTrackbar('Standard Deviation','Gaussian',0,50,emptyFunction)
	cv2.createTrackbar('+ve Alpha','Gaussian',0,20,emptyFunction)
	cv2.createTrackbar('+ve Beta','Gaussian',0,20,emptyFunction)
	cv2.createTrackbar('-ve Alpha','Gaussian',0,20,emptyFunction)
	cv2.createTrackbar('-ve Beta','Gaussian',0,20,emptyFunction)
	cv2.createTrackbar('Alpha','Anisotropic Diffusion',0,10,emptyFunction)
	cv2.createTrackbar('Sensitivity','Anisotropic Diffusion',0,500,emptyFunction)
	cv2.createTrackbar('Iterations','Anisotropic Diffusion',1,500,emptyFunction)
	cv2.createTrackbar('Kernel','Median Blur',3,15,emptyFunction)
	cv2.createTrackbar('Kernel','Median Blur 2',3,25,emptyFunction)
	cv2.createTrackbar('FGauss','Gaussian',0,1,emptyFunction)
	cv2.createTrackbar('FGamma','Gamma Correction',0,1,emptyFunction)
	cv2.createTrackbar('FAWBal','Auto White Balance',0,1,emptyFunction)
	cv2.createTrackbar('FAni','Anisotropic Diffusion',0,1,emptyFunction)
	cv2.createTrackbar('FB','Median Blur',0,1,emptyFunction)
	cv2.createTrackbar('FG','Median Blur',0,1,emptyFunction)
	cv2.createTrackbar('FR','Median Blur',0,1,emptyFunction)
	cv2.createTrackbar('FMed','Median Blur 2',0,1,emptyFunction)
	cv2.createTrackbar('FL','Clahe LAB',0,1,emptyFunction)
	cv2.createTrackbar('FA','Clahe LAB',0,1,emptyFunction)
	cv2.createTrackbar('FB','Clahe LAB',0,1,emptyFunction)
	cv2.createTrackbar('FB','Clahe',0,1,emptyFunction)
	cv2.createTrackbar('FG','Clahe',0,1,emptyFunction)
	cv2.createTrackbar('FR','Clahe',0,1,emptyFunction)
	cv2.createTrackbar('FL','Output',0,1,emptyFunction)
	cv2.createTrackbar('FM','YCrCb Median Blur',0,1,emptyFunction)
	
	cap = cv2.VideoCapture(imgpath)
	ret, image=cap.read()
	(h, w, c) = image.shape
	cv2.circle(image, (w//2, h//2), 7, (255, 255, 255), -1) 
	width2 = float(w)/2
	
	cv2.setTrackbarPos('+ve Gamma','Gamma Correction',16)
	cv2.setTrackbarPos('-ve Gamma','Gamma Correction',0)
	cv2.setTrackbarPos('Hue','Correction',100)
	cv2.setTrackbarPos('Saturation','Correction',100)
	cv2.setTrackbarPos('Value','Correction',100)
	cv2.setTrackbarPos('Low H','Thresh Output',8)
	cv2.setTrackbarPos('Low S','Thresh Output',149)
	cv2.setTrackbarPos('Low V','Thresh Output',170)
	cv2.setTrackbarPos('High H','Thresh Output',34)
	cv2.setTrackbarPos('High S','Thresh Output',255)
	cv2.setTrackbarPos('High V','Thresh Output',255)
	
	cv2.setTrackbarPos('Kernel Size','YCrCb Median Blur',3)
	cv2.setTrackbarPos('Laplacian ksize','Output',3)
	
	cv2.setTrackbarPos('Clip Limit (Blue)','Clahe',0)
	cv2.setTrackbarPos('Tile Grid Size (Blue)','Clahe',4)
	cv2.setTrackbarPos('Clip Limit (Green)','Clahe',0)
	cv2.setTrackbarPos('Tile Grid Size (Green)','Clahe',4)
	cv2.setTrackbarPos('Clip Limit (Red)','Clahe',0)
	cv2.setTrackbarPos('Tile Grid Size (Red)','Clahe',4)
	cv2.setTrackbarPos('Pair','Clahe',1)
	
	cv2.setTrackbarPos('Kernel Size','Gaussian',3)
	cv2.setTrackbarPos('Standard Deviation','Gaussian',5)
	cv2.setTrackbarPos('+ve Alpha','Gaussian',11)
	cv2.setTrackbarPos('+ve Beta','Gaussian',2)
	cv2.setTrackbarPos('-ve Alpha','Gaussian',2)
	cv2.setTrackbarPos('-ve Beta','Gaussian',0)
	cv2.setTrackbarPos('Alpha','Anisotropic Diffusion',1)
	cv2.setTrackbarPos('Sensitivity','Anisotropic Diffusion',20)
	cv2.setTrackbarPos('Iterations','Anisotropic Diffusion',2)
	cv2.setTrackbarPos('Kernel','Median Blur',5)
	cv2.setTrackbarPos('Kernel','Median Blur 2',3)
	cv2.setTrackbarPos('FGauss','Gaussian',0)
	cv2.setTrackbarPos('FGamma','Gamma Correction',1)
	cv2.setTrackbarPos('FAWBal','Auto White Balance',0)
	cv2.setTrackbarPos('FAni','Anisotropic Diffusion',1)
	cv2.setTrackbarPos('FB','Median Blur',1)
	cv2.setTrackbarPos('FG','Median Blur',1)
	cv2.setTrackbarPos('FR','Median Blur',1)
	cv2.setTrackbarPos('FMed','Median Blur 2',0)
	cv2.setTrackbarPos('FL','Clahe LAB',0)
	cv2.setTrackbarPos('FA','Clahe LAB',0)
	cv2.setTrackbarPos('FB','Clahe LAB',0)
	
	cv2.setTrackbarPos('FB','Clahe',1)
	cv2.setTrackbarPos('FG','Clahe',1)
	cv2.setTrackbarPos('FR','Clahe',1)
	
	cv2.setTrackbarPos('FL','Output',0)
	cv2.setTrackbarPos('FM','YCrCb Median Blur',0)
	
	
	ret = True
	flag=1
	xdiff=0
	txdiff=0
	cX=0
	cY=0
	maxArea=0
	while (1):
		maxArea=0
		if flag==1:
			ret,img = cap.read()
		
		fgs = cv2.getTrackbarPos('FGauss','Gaussian')
		fgm = cv2.getTrackbarPos('FGamma','Gamma Correction')
		fab = cv2.getTrackbarPos('FAWBal', 'Auto White Balance')
		fad = cv2.getTrackbarPos('FAni','Anisotropic Diffusion')
		fmb = cv2.getTrackbarPos('FB','Median Blur')
		fmg = cv2.getTrackbarPos('FG','Median Blur')
		fmr = cv2.getTrackbarPos('FR','Median Blur')
		fmed = cv2.getTrackbarPos('FMed','Median Blur 2')
		fcll = cv2.getTrackbarPos('FL','Clahe LAB')
		fcla = cv2.getTrackbarPos('FA','Clahe LAB')
		fclb = cv2.getTrackbarPos('FB','Clahe LAB')
		
		fcb = cv2.getTrackbarPos('FB','Clahe')
		fcg = cv2.getTrackbarPos('FG','Clahe')
		fcr = cv2.getTrackbarPos('FR','Clahe')
		
		fyl = cv2.getTrackbarPos('FL','Output')
		fym = cv2.getTrackbarPos('FM','YCrCb Median Blur')
		
		hl = cv2.getTrackbarPos('Low H','Thresh Output')
		hh = cv2.getTrackbarPos('High H','Thresh Output')
		sl = cv2.getTrackbarPos('Low S','Thresh Output')
		sh = cv2.getTrackbarPos('High S','Thresh Output')
		vl = cv2.getTrackbarPos('Low V','Thresh Output')
		vh = cv2.getTrackbarPos('High V','Thresh Output')
		clipLim1=(cv2.getTrackbarPos('Clip Limit (Blue)','Clahe'))
		clipLim1=float(clipLim1)/1000
		tgs1=cv2.getTrackbarPos('Tile Grid Size (Blue)','Clahe')
		clipLim2=(cv2.getTrackbarPos('Clip Limit (Green)','Clahe'))
		clipLim2=float(clipLim2)/1000
		tgs2=cv2.getTrackbarPos('Tile Grid Size (Green)','Clahe')
		clipLim3=(cv2.getTrackbarPos('Clip Limit (Red)','Clahe'))
		clipLim3=float(clipLim3)/1000
		tgs3=cv2.getTrackbarPos('Tile Grid Size (Red)','Clahe')
		
		pgamma=cv2.getTrackbarPos('+ve Gamma','Gamma Correction')
		ngamma=cv2.getTrackbarPos('-ve Gamma','Gamma Correction')
		hc=cv2.getTrackbarPos('Hue','Correction')
		sc=cv2.getTrackbarPos('Saturation','Correction')
		vc=cv2.getTrackbarPos('Value','Correction')
		pgamma=float(pgamma)/10
		ngamma=float(ngamma)/10
		hc=float(hc)/100
		sc=float(sc)/100
		vc=float(vc)/100
		ks=cv2.getTrackbarPos('Kernel Size','Gaussian')
		sd=(cv2.getTrackbarPos('Standard Deviation','Gaussian'))
		sd=float(sd)/10
		alpha=(cv2.getTrackbarPos('+ve Alpha','Gaussian'))
		beta=(cv2.getTrackbarPos('+ve Beta','Gaussian'))
		nalpha=(cv2.getTrackbarPos('-ve Alpha','Gaussian'))
		nbeta=(cv2.getTrackbarPos('-ve Beta','Gaussian'))
		alpha=float(alpha)/10
		beta=float(beta)/10
		nalpha=float(nalpha)/10
		nbeta=float(nbeta)/10
		alph=(cv2.getTrackbarPos('Alpha','Anisotropic Diffusion'))
		alph=float(alph)/10
		sens=cv2.getTrackbarPos('Alpha','Anisotropic Diffusion')
		itern=cv2.getTrackbarPos('Alpha','Anisotropic Diffusion')
		mker=cv2.getTrackbarPos('Kernel','Median Blur')
		medker=cv2.getTrackbarPos('Kernel','Median Blur 2')
		ymker=cv2.getTrackbarPos('Kernel Size','YCrCb Median Blur')
		ylksize=cv2.getTrackbarPos('Laplacian ksize','Output')
		
		
		if ks%2==0:
			ks+=1
		if mker%2==0:
			mker+=1
		if medker%2==0:
			medker+=1
		if ymker%2==0:
			ymker+=1
		if ylksize%2==0:
			ylksize+=1
		
		fg=cv2.getTrackbarPos('Pair','Clahe')
		if ret:
			if cv2.waitKey(2) == 27:
				break
			if cv2.waitKey(2) == 97:
				flag = 1
			if cv2.waitKey(2) == 32:
				flag=0
			low = np.array([hl,sl,vl])
			high = np.array([hh,sh,vh])
			
			#Gamma Correction
			t1=time.time()
			gc=adjust_gamma(img,pgamma-ngamma)
			t2=time.time()-t1
			#print(t2)
			cv2.imshow('Gamma Correction',gc)
			if(fgm==0):
				gc=img
			
			
			#Gaussian
			gaussian = cv2.GaussianBlur(gc ,(ks,ks), sd)
			gauss = cv2.addWeighted(img, alpha-nalpha, gaussian, beta-nbeta, 0)
			cv2.imshow('Gaussian',gauss)
			if(fgs==0):
				gauss=gc
			
			
			#Correcting HSV Values
			st1=cv2.cvtColor(gauss,cv2.COLOR_BGR2HSV)
			st1[:, :, 0]=st1[:, :, 0]*hc
			st1[:, :, 1]=st1[:, :, 1]*sc
			st1[:, :, 2]=st1[:, :, 2]*vc
			st3=cv2.cvtColor(st1,cv2.COLOR_HSV2BGR)
			cv2.imshow('Correction',st3)
			
			
			#Auto White Balance
			result1 = cv2.cvtColor(st3, cv2.COLOR_BGR2LAB)
			avg_a = np.average(result1[:, :, 1])
			avg_b = np.average(result1[:, :, 2])
			result1[:, :, 1] = result1[:, :, 1] - ((avg_a - 128) * (result1[:, :, 0] / 255.0) * 1.5)
			result1[:, :, 2] = result1[:, :, 2] - ((avg_b - 128) * (result1[:, :, 0] / 255.0) * 1.5)
			result1 = cv2.cvtColor(result1, cv2.COLOR_LAB2BGR)
			cv2.imshow('Auto White Balance',result1)
			if (fab==0):
				result1=st3
			
			#Anisotropic Diffusion
			adf = cv2.ximgproc.anisotropicDiffusion(result1, alph, sens, itern)
			cv2.imshow('Anisotropic Diffusion',adf)
			if(fad==0):
				adf=result1
				
			#Median Blur
			b, g, r = cv2.split(adf)
			b1 = cv2.medianBlur(b,mker)
			if(fmb==0):
				b1=b
			g1 = cv2.medianBlur(g,mker)
			if(fmg==0):
				g1=g
			r1 = cv2.medianBlur(r,mker)
			if(fmr==0):
				r1=r
			medfil = cv2.merge((b1, g1, r1))
			cv2.imshow('Median Blur',medfil)
			
			#Clahe LAB
			clahe1 = cv2.createCLAHE(clipLimit=clipLim1,tileGridSize=(tgs1,tgs1))
			clahe2 = cv2.createCLAHE(clipLimit=clipLim2,tileGridSize=(tgs2,tgs2))
			clahe3 = cv2.createCLAHE(clipLimit=clipLim3,tileGridSize=(tgs3,tgs3))
			lab=cv2.cvtColor(medfil,cv2.COLOR_BGR2LAB)
			l, a, b = cv2.split(lab)
			l1 = clahe1.apply(l)
			if(fcll==0):
				l1=l
			a1 = clahe2.apply(a)
			if(fcla==0):
				a1=a
			b1 = clahe3.apply(b)
			if(fclb==0):
				b1=b
			cmer=cv2.merge((l1,a1,b1))
			cllab=cv2.cvtColor(cmer,cv2.COLOR_LAB2BGR)
			cv2.imshow('Clahe LAB',cllab)
			
			#Clahe BGR
			if(fg==1):
				cv2.setTrackbarPos('Clip Limit (Green)','Clahe',int(clipLim1*1000))
				cv2.setTrackbarPos('Tile Grid Size (Green)','Clahe',tgs1)
				cv2.setTrackbarPos('Clip Limit (Red)','Clahe',int(clipLim1*1000))
				cv2.setTrackbarPos('Tile Grid Size (Red)','Clahe',tgs1)
			clahe1 = cv2.createCLAHE(clipLimit=clipLim1,tileGridSize=(tgs1,tgs1))
			clahe2 = cv2.createCLAHE(clipLimit=clipLim2,tileGridSize=(tgs2,tgs2))
			clahe3 = cv2.createCLAHE(clipLimit=clipLim3,tileGridSize=(tgs3,tgs3))
			b, g, r = cv2.split(cllab)
			b1 = clahe1.apply(b)
			if(fcb==0):
				b1=b
			g1 = clahe2.apply(g)
			if(fcg==0):
				g1=g
			r1 = clahe3.apply(r)
			if(fcr==0):
				r1=r
			cl=cv2.merge((b1,g1,r1))
			cv2.imshow('Clahe',cl)
			
			#Median Blur
			medblur = cv2.medianBlur(cl,medker)
			cv2.imshow('Median Blur 2',medblur)
			if(fmed==0):
				medblur=cl
				
			#YCrCb  Laplacian
			ycrcb=cv2.cvtColor(medblur, cv2.COLOR_BGR2YCR_CB)
			y,cr,cb=cv2.split(ycrcb)
			dst = cv2.Laplacian( y, cv2.CV_16S, ksize=ylksize)
			absDst = cv2.convertScaleAbs( dst )
			out=cv2.merge((absDst,cr,cb))
			output=cv2.cvtColor(out, cv2.COLOR_YCR_CB2BGR)
			cv2.imshow('Output',output)
			if(fyl==0):
				output=medblur
				
			#YCrCb Median 
			med=cv2.medianBlur(absDst,ymker)
			tempOut=cv2.merge((med,cr,cb))
			tempOutput=cv2.cvtColor(tempOut, cv2.COLOR_YCR_CB2BGR)
			cv2.imshow('YCrCb Median Blur',tempOutput)
			if(fym==0):
				tempOutput=output
			
			
			
			#Masking
			hsv1= cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
			obj1 = cv2.inRange(hsv1, low, high)
			res1 = cv2.bitwise_and(output, output, mask=obj1)
			
			#DETECTION
			gray=cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
			ret1,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
			(contours,hierarchy) = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
			for pic, contour in enumerate(contours):
				area1 = cv2.contourArea(contour)
				if(area1>700):
					x,y,w,h = cv2.boundingRect(contour)
					if(w*1.5<h and h>120):
						cv2.rectangle(res1,(x,y),(x+w,y+h),(0,165,255),2)
						M = cv2.moments(contour)
						cX = int(M["m10"] / M["m00"])
						cY = int(M["m01"] / M["m00"])
						cv2.circle(res1, (cX, cY), 7, (255, 255, 255), -1)
						if(area1>maxArea):
							maxArea=area1
							txdiff=width2-cX
			if(txdiff!=xdiff):
				xdiff=txdiff
				print('Pixel Difference:', xdiff)	
			#Display
			cv2.imshow('Thresh Output',res1)
			cv2.imshow('Video',img)	
			#VideoFileOutput.write(res1)
			#VideoFileOutput2.write(img)
			
		else:
			break
	cv2.destroyAllWindows()
	#VideoFileOutput.release()
	#VideoFileOutput2.release()
	cap.release()
if __name__ == "__main__":
	main()
