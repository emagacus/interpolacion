from django.shortcuts import render
from django.http import HttpResponse
from . import interpolar as dd
# Create your views here.
def index(request):
	return render(request,'webapp/home.html')


def submit(request):
    info=request.POST['info']
    # do something with info

    try: 
    	float(info)
    except:
    	return render(request,'webapp/home.html',{'valuestotal':'entrada invalida'})
    		


    if(float(info)<1950 or float(info)>2010):
    	return render(request,'webapp/home.html',{'valuestotal':'No se puede interpolar:c'})
    else:	
    	#harcodeado por que ya me quiero dormir 
    	arr_anios = [1950,1960,1970,1990,1995,2000,2005,2010]
    	pob_total = [25791017,34923129,48225238,81249645,91158290,97483412,103263388,112336538]
    	pob_mujeres = [13094082,17507809,24159624,41355676,46257791,49891159,53013433,57481307]
    	pob_hombres = [12696935,17415320,24065614,39893969,44900499,47592253,50249955,54855231]

    	intTotal =  int (dd.interpolaX(arr_anios,pob_total,float(info)))
    	intMujeres = int(dd.interpolaX(arr_anios,pob_mujeres,float(info)))
    	intHombres = int(dd.interpolaX(arr_anios,pob_hombres,float(info)))
    	arr_anios.append(int(info))
    	arr_anios.sort()
    	arrLabels = arr_anios

    	return render(request,'webapp/home.html',{'valuestotal':intTotal,'valuesmujeres':intMujeres,'valueshombres':intHombres,'anioactual':info,'arraylabels':arrLabels})
