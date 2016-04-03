from django.shortcuts import render_to_response, render
from blog.models import posts
from .forms import CommentForm
import json
from django import forms
from math import sqrt, acos, log

	 
def QSK19(flowpaths ):
	Qout= 27273/flowpaths #heat dissipation per flow path BTU/min 
	Tin=120 #temperature of coolant into keel cooler in deg False
	Volume_rate=82/448.833/flowpaths #volumetric flow rate in ft^3/s
	QSK19_results=[Qout,Tin,Volume_rate]
	return(QSK19_results) 
	

	
def Resistance1(area,bf,tw,tf,d,L,Tin,Volume_rate):
	a1=(bf-tw)/12#inside height in feet
	b1=(d-2*tf)/12#inside width in feet
	Dh=4*(a1*b1)/(2*a1+b1)
	As1=(2*a1+b1)*L #inside surface area in ft^2
	Ac=(d*bf-area)
	k1=-0.000002*Tin**2+0.0009*Tin+0.2935#thermal conductivity of water in BTU/hr-F-ft-F
	p1=(-0.00007*Tin**2+0.0009*Tin+62.557)#density in lbm/ft^3
	u1=(0.00002*Tin**2-0.0088*Tin+1.1442)*0.001#absolute viscosity in lbm/ft sec
	v1=u1/p1#kinematic viscosity in ft^2/sec
	Cp1=1 #Specific Heat in Btu/lbmF
	Pr1= Cp1*u1/(k1/60**2) #Prandtl number
	V=Volume_rate/(a1*b1)#fluid velocity in ft/s
	Re1=V*L/v1 #Reynolds Number
	Nu1=0.036*Re1**0.8*Pr1**(1/3)
	hc=0.023*k1*(V**0.8)*((u1/p1)**-0.8)*(Dh**(-0.2))	
	d_eqo=(4*Ac/acos(-1))**0.5
	d_eqi=d_eqo-2*tw
	R1=d_eqo/d_eqi*0.0005+1/hc
	Resistance1_results=[R1,hc,k1,d_eqo,d_eqi]
	return(Resistance1_results)
	
def Resistance2(k_material,L, tw):
	R2=tw/12/(k_material)
	return(R2)
	
def Resistance3(L,vessel_speed,tw):
	Tw=85#Degrees Farenheit of water
	k2=-0.000002*Tw**2+0.0009*Tw+0.2935#thermal conductivity of water in BTU/hr-F-ft-F
	p2=(-0.00007*Tw**2+0.0009*Tw+62.557)#density in lbm/ft^3
	u2=(0.00002*Tw**2-0.0088*Tw+1.1442)*0.001#absolute viscosity in lbm/ft sec
	k2=-0.000002*Tw**2+0.0009*Tw+0.2935#thermal conductivity of water in BTU/hr-F-ft-F
	v2=u2/p2
	Cp2=1 #Specific Heat in Btu/lbmF
	Pr2= Cp2*u2/(k2/60**2) #Prandtl number
	ReL=0.65*vessel_speed*1.68*L/v2
	Nu2=0.036*ReL**0.8*Pr2**(1/3)
	ho=k2*Nu2/L
	R3=1/ho
	Resistance3_results=[R3,ho]
	return(Resistance3_results)
	
	
def channel(Channelsize):
	channel_area=[14.7,11.8,9.96,8.82,7.35,6.09,8.82,7.35,5.88,4.49,5.88,4.41,3.94,5.51,4.04,3.38,4.33,3.6,2.87,3.83,3.09,2.4,2.64,1.97,2.13,1.59,1.76,1.47,1.21,10.053,7.036,7.109,5.218,5.927,4.237,4.923,3.526,4.009,2.725,3.427,2.41,2.627,1.881,1.982,1.478,1.358,0.965,0.911,0.491]
	channel_area=channel_area[Channelsize]
	channel_depth=[15.000,15.000,15.000,12.000,12.000,12.000,10.000,10.000,10.000,10.000,9.000,9.000,9.000,8.000,8.000,8.000,7.000,7.000,7.000,6.000,6.000,6.000,5.000,5.000,4.000,4.000,3.000,3.000,3.000,12.000,12.000,10.000,10.000,9.000,9.000,8.000,8.000,7.000,7.000,6.000,6.000,5.000,5.000,4.000,4.000,3.000,3.000,2.000,2.000]
	channel_depth=channel_depth[Channelsize]	
	channel_bf= [3.716,3.520,3.400,3.170,3.047,2.942,3.033,2.886,2.739,2.600,2.648,2.485,2.433,2.527,2.343,2.260,2.299,2.194,2.090,2.157,2.034,1.920,1.885,1.750,1.721,1.584,1.596,1.498,1.410,5.000,4.000,4.250,3.500,4.000,3.250,3.750,3.000,3.500,2.750,3.250,2.500,2.750,2.250,2.250,2.000,1.750,1.500,1.250,1.000]
	channel_bf=channel_bf[Channelsize]
	channel_tf=[0.650,0.650,0.650,0.501,0.501,0.501,0.436,0.436,0.436,0.436,0.413,0.413,0.413,0.390,0.390,0.390,0.366,0.366,0.366,0.343,0.343,0.343,0.320,0.320,0.296,0.296,0.273,0.273,0.273,0.620,0.470,0.500,0.410,0.440,0.350,0.410,0.350,0.380,0.290,0.350,0.290,0.320,0.260,0.290,0.230,0.260,0.200,0.260,0.130]
	channel_tf=channel_tf[Channelsize]
	channel_tw=[0.716,0.520,0.400,0.510,0.387,0.282,0.673,0.526,0.379,0.240,0.448,0.285,0.233,0.487,0.303,0.220,0.419,0.314,0.210,0.437,0.314,0.200,0.325,0.190,0.321,0.184,0.356,0.258,0.170,0.350,0.290,0.310,0.250,0.290,0.230,0.250,0.190,0.210,0.170,0.210,0.170,0.190,0.150,0.190,0.150,0.170,0.130,0.170,0.130]
	channel_tw=channel_tw[Channelsize]
	if Channelsize<29:
		k_material=26.5 #thermal conductivity of Steel BTU/hr-ft-F
	else:
		k_material=118.0 #thermal conductivity of Aluminum BTU/hr-ft-F
	channel_results=[channel_area,channel_depth,channel_tf,channel_bf,channel_tw,k_material]

	return (channel_results)

	
class MyForm(forms.Form):
	Coolant = forms.DecimalField(initial = 1.00)
	Material = forms.DecimalField(initial = 1.00)
	Engineselect = forms.DecimalField(initial = 0.00)
	Channelsize = forms.IntegerField(initial = 1.00)
	flowpaths = forms.IntegerField(initial = 1.00)
	kclength = forms.FloatField(initial = 0.00)
	vessel_speed = forms.FloatField(initial = 0.00)



	
def home(request): 
	return render_to_response( "index.html")
stankogut = "0"
	
	
def index(request):
	template = "index.html"
	content= {'stankogut' : '0'}
	return render_to_response(template, content)
	
def contributors(request):
	entries = posts.objects.all()[:10]
	return render_to_response('contributors.html', {'posts' : entries})

def docs(request):
	entries = posts.objects.all()[:10]
	return render_to_response('documents.html', {'posts' : entries})
	
def contact(request):
	entries = posts.objects.all()[:10]
	return render_to_response('contact.html', {'posts' : entries})


# def keelcooler(request):
	# print(request.POST)
	# form = CommentForm()
	# code1 = form.cleaned_data['code1']
	# context = {"form": form, "xy" : result}
	# template = "keelcooler.html"
	# return render(request, template, context)

# Create your views here.

def keelcooler(request): 
	return render(request, 'keelcooler.html')
	

def formview(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			Coolant = form.cleaned_data['Coolant']
			Material = form.cleaned_data['Material']
			Engineselect = form.cleaned_data['Engineselect']
			Channelsize = form.cleaned_data['Channelsize']
			flowpaths = form.cleaned_data['flowpaths']
			kclength = form.cleaned_data['kclength']
			vessel_speed = form.cleaned_data['vessel_speed']
			
			if Engineselect==1:
				QSK19_results=QSK19(flowpaths)
				Qout=QSK19_results[0]
				Tin=QSK19_results[1]
				Volume_rate=QSK19_results[2]
			
			channel_results=channel(Channelsize-1)
			
			L=kclength
			
			
			area=channel_results[0]
			d= channel_results[1]
			bf= channel_results[3]
			tf= channel_results[2]
			tw= channel_results[4]
			k_material= channel_results[5]
			R2=Resistance2(k_material,kclength, tw)
			
			
			Resistance1_results=Resistance1(area,bf,tw,tf,d,kclength,Tin,Volume_rate)
			R1=Resistance1_results[0]
			hi=Resistance1_results[1]
			kw=Resistance1_results[2]
			do_eq=Resistance1_results[3]
			di_eq=Resistance1_results[4]
			
			Resistance3_results=Resistance3(L,vessel_speed,tw)
			R3=Resistance3_results[0]
			ho=Resistance3_results[1]
			
			Rf_seawater=0.0005
			Rf_coolant=0.001
			Cp_eg=-0.0000003*(Tin**2) + 0.0005*(Tin) + 0.7762
			U_overall=1/(R3+Rf_seawater+R2+Rf_coolant+R1)
			
			dT_required= Qout*flowpaths/(Volume_rate*448.833*flowpaths*.1337*64*Cp_eg)
			Th=Tin+dT_required
			Tc=85#Degrees
			
			dTA=Th-Tc
			dTB=Tin-Tc
			LMTD=(dTA-dTB)/log(dTA/dTB)
			A_required=(Qout*flowpaths*60)/(U_overall*LMTD)
			perimeter=(2*bf+d)/12
			A_actual=(perimeter)*L*flowpaths
			
			if(A_actual<A_required):
				KCRESULT="FAIL"
				Lnew=A_required/perimeter/flowpaths
				fpnew=A_required/(perimeter*L)
				if((fpnew-int(fpnew))>0):
					fpnew=int(fpnew)+1
				
				NOTE1="AT THE SAME NUMBER OF FLOW PATHS, THE REQUIRED KEEL COOLER LENGTH IS %.2f ft." %Lnew
				NOTE2="AT THE SAME LENGTH, THE REQUIRED NUMBER OF FLOW PATHS IS %.0f" %fpnew

			else:
				KCRESULT="PASS"
				NOTE1=" "
				NOTE2=" "
			template = "keelcooler.html"
#------------------VARIABLE DEFINITION------------------------------------------------------
			content={
			'Coolant' : Coolant,
			'Material' : Material,
			'Engineselect' : Engineselect,
			'Channelsize' : Channelsize,			
			'flowpaths' : flowpaths,
			'kclength' : kclength,
			'Qout' : Qout,
			'area' : channel_results[0],
			'depth' : channel_results[1],
			'bf' : channel_results[3],
			'tf' : channel_results[2],
			'tw' : channel_results[4],
			'k_material' : channel_results[5], 
			'R1' : R1,
			'hi' : hi,
			'kw' : kw,
			'do_eq' : do_eq,
			'di_eq' : di_eq,
			'R2' : R2,
			'R3' : R3,
			'ho' : ho,
			'U_overall' : U_overall,
			'Temp_increment' : dT_required,
			'LMTD' : LMTD,
			'A_required' : A_required,
			'A_actual' : A_actual,
			'NOTE1' : NOTE1,
			'NOTE2' : NOTE2,
			'KCRESULT' : KCRESULT,
			}
#-------------------------------------------------------------------------------------------
			
			
			
			
#-------------------CALCULATIONS-----------------------

#------------------------------------------------------			

		else:
			template = "keelcooler.html"
			content={
			'message': "[error]"
			}
	return render(request, template, content)
	






