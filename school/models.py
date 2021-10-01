from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import date
import twilio
import random
from twilio.rest import Client
from django.utils import timezone

# EMS Masters - PlantType 702 - 712
## Revenue Simulation 745 - 782
## Revenue Simulation Summary 848 - 883
### EMS Project 670 - 

# Create your models here.

heads = (
('Salary', 'Salary'),
('Fee Collection', 'Fee Collection'),
('Current Bill', 'Current Bill'),
('Telephone Bills', 'Telephone Bills'),
('Misllanious', 'Misllanious'),
('Rent', 'Rent'),
('Transportation', 'Transportation'),
('Capitals', 'Capitals'),
('Loans', 'Loans'),
('Advances', 'Advances'),
)


class Usersdata(models.Model):
    username=models.CharField(max_length=255,blank=True)
    email=models.CharField(max_length=255,blank=True)
    gname=models.CharField(max_length=255,blank=True)
    role=models.CharField(max_length=255,blank=True)
    isactive=models.BooleanField(default=True)
    lastlogin=models.CharField(max_length=255,null=True,blank=True)
    datejoined=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.username

class Groupsdata(models.Model):
    gname=models.CharField(max_length=255,blank=True)
    pername=models.CharField(max_length=255,blank=True)   
    
    def __str__(self):
        return self.gname
# For Sign_Up First Level Validation process 
class Rfr(models.Model):
    refcode=models.CharField(max_length=255,blank=True)
    def __str__(self):
        return self.refcode

# While Sign_Up process Extended User 
class Referral(models.Model):
    referralcode=models.CharField(max_length=255,blank=True)
    def __str__(self):
        return self.referralcode

class Signup(models.Model):
    first_name=models.CharField(max_length=255, blank=True)
    last_name=models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255,unique=False, blank=True)
    email=models.CharField(max_length=255,unique=False, blank=True)
    password = models.CharField(max_length=255,  blank=True, null=True)
    role = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    graceperiod = models.CharField(max_length=255, blank=True, null=True)
    mobileno = models.BigIntegerField(blank=True, null=True)
    active = models.BooleanField(default=True) 

    def __str__(self):
        return self.username
    def __str__(self):
        return self.username

class rpt_bankwise(models.Model):
    #date = models.DateField(null=True,blank=True)
    route_number  = models.CharField(max_length=255,null=True,blank=True)
    supervisor = models.CharField(max_length=255,null=True,blank=True)
    centre_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255,null=True,blank=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    bankname = models.CharField(max_length=255,null=True,blank=True)
    BankBranch = models.CharField(max_length=255,null=True,blank=True)
    ifsc=models.CharField(max_length=255,null=True,blank=True)
    amount  = models.FloatField(default=0.00)
    mobile = models.CharField(max_length=255,null=True,blank=True)
    total =     models.FloatField(default=0.00)
    ddate = models.DateField(null=True,blank=True)
    net = models.FloatField(default=0.00)
    NetAmt = models.FloatField(default=0.00,null=True,blank=True)
    #cid = models.CharField(max_length=255,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. centercode
##ver 07071212AM Version line- 649-658
##Created by Mamatha 01-07-2021
class Version(models.Model):
    vercode = models.CharField(unique = True,max_length=255,null=True,blank=True)
    vername = models.CharField(max_length=255,null=True,blank=True)
    effectedfromdate = models.DateField(null=True,blank=True)
    effectedtodate = models.DateField(null=True,blank=True)
    createdby = models.CharField(max_length=255,null=True,blank=True)
    editedby = models.CharField(max_length=255,null=True,blank=True)
    remarks = models.CharField(max_length=255,null=True,blank=True)
    def _str_(self):
        #name column is not defined so its giving an error
        return self.vercode
        # return self.name
##END##

## EMS Summary report table
## Sireesha 02-July-2021 
class rpt_emsDeDSumbyAnB(models.Model):
    #date = models.DateField(null=True,blank=True)
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)    
    DedCnt = models.IntegerField(default=0.00,null=True,blank=True)
    #cid = models.CharField(max_length=255,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. areaCode

## EMS Summary by Hybrid report table
## Sireesha 14-Sept-2021 
class rpt_emsSumbyH(models.Model):
    #date = models.DateField(null=True,blank=True)
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)
    #treeNo = models.IntegerField(default=0.00,null=True,blank=True)
    #plantDate = models.DateField(null=True,blank=True)
    plantType = models.CharField(max_length=10,null= True,blank=True)
    #height=models.FloatField(default=0.00,null=True, blank=True)
    TotCnt = models.IntegerField(default=0.00,null=True,blank=True)
    DedCnt = models.IntegerField(default=0.00,null=True,blank=True)
    LivCnt = models.IntegerField(default=0.00,null=True,blank=True)
    TeraceCnt = models.IntegerField(default=0.00,null=True,blank=True)    
    eid = models.IntegerField(default=0.00,null=True,blank=True)
    cid = models.IntegerField(default=0,null=True,blank=True)
    LivSum = models.IntegerField(default=0.00,null=True,blank=True)
    hybridCnt = models.IntegerField(default=0.00,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. areaCode
        

## EMS Summary report table
## Sireesha 02-July-2021 
class rpt_emsSumbyAnB(models.Model):
    #date = models.DateField(null=True,blank=True)
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)
    #treeNo = models.IntegerField(default=0.00,null=True,blank=True)
    #plantDate = models.DateField(null=True,blank=True)
    #plantType = models.CharField(max_length=10,null= True,blank=True)
    #height=models.FloatField(default=0.00,null=True, blank=True)
    TotCnt = models.IntegerField(default=0.00,null=True,blank=True)
    DedCnt = models.IntegerField(default=0.00,null=True,blank=True)
    LivCnt = models.IntegerField(default=0.00,null=True,blank=True)
    TeraceCnt = models.IntegerField(default=0.00,null=True,blank=True)    
    eid = models.IntegerField(default=0.00,null=True,blank=True)
    cid = models.IntegerField(default=0,null=True,blank=True)
    LivSum = models.IntegerField(default=0.00,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. areaCode

## EMS Summary report table
## Sireesha 02-July-2021 
class rpt_emsSumbyAnBOnly(models.Model):
    #date = models.DateField(null=True,blank=True)
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)    
    teraceNo = models.IntegerField(default=0.00,null=True,blank=True)
    #plantDate = models.DateField(null=True,blank=True)
    #plantType = models.CharField(max_length=10,null= True,blank=True)
    #height=models.FloatField(default=0.00,null=True, blank=True)
    TotCnt = models.IntegerField(default=0.00,null=True,blank=True)
    DedCnt = models.IntegerField(default=0.00,null=True,blank=True)
    LivCnt = models.IntegerField(default=0.00,null=True,blank=True)
    eid = models.IntegerField(default=0.00,null=True,blank=True)
    #cid = models.CharField(max_length=255,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. areaCode

## EMS Summary report table
## Sireesha 02-July-2021 
class rpt_emsSumbyAOnly(models.Model):
    #date = models.DateField(null=True,blank=True)
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCnt = models.IntegerField(default=0.00,null=True,blank=True)    
    teraceNo = models.IntegerField(default=0.00,null=True,blank=True)
    #plantDate = models.DateField(null=True,blank=True)
    #plantType = models.CharField(max_length=10,null= True,blank=True)
    #height=models.FloatField(default=0.00,null=True, blank=True)
    TotCnt = models.IntegerField(default=0.00,null=True,blank=True)
    DedCnt = models.IntegerField(default=0.00,null=True,blank=True)
    LivCnt = models.IntegerField(default=0.00,null=True,blank=True)
    eid = models.IntegerField(default=0.00,null=True,blank=True)
    #cid = models.CharField(max_length=255,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. areaCode

## EMS Summary report table


class Rpt_ExtractPlantTHAgData(models.Model):
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)
    treeNo = models.IntegerField(null=True,blank=True)
    plantDate = models.DateField(null=True,blank=True)
    plantType = models.CharField(max_length=10,null= True,blank=True)
    height=models.FloatField(default=0.00,null=True, blank=True)
    girth=models.FloatField(default=0.00,null=True, blank=True)
    leaveCnt = models.IntegerField(null=True,blank=True)
    #tcWeeType = models.CharField(max_length=10,null= True,blank=True)
    #tcWaterlog = models.CharField(max_length=10,null= True,blank=True)
    #tcMud = models.CharField(max_length=10,null= True,blank=True)
    #TCNet = models.CharField(max_length=10,null= True,blank=True)
    #WTRing = models.CharField(max_length=10,null= True,blank=True)
    #Waterpipe = models.CharField(max_length=10,null= True,blank=True)
    #PnDFung = models.CharField(max_length=10,null= True,blank=True)
    #PNDTermite = models.CharField(max_length=10,null= True,blank=True)
    #PNDChType = models.CharField(max_length=10,null= True,blank=True)
    #PNDDate = models.DateField(null=True,blank=True)
    #manurFType = models.CharField(max_length=10,null= True,blank=True)
    #ManureRate=models.FloatField(default=0.00,null=True, blank=True)
    #ManureDate = models.DateField(null=True,blank=True)
    Remarks = models.CharField(max_length=100,null= True,blank=True)
    extdate = models.DateField(null=True,blank=True)
    #extUser = models.CharField(max_length=255,blank=True)
    fileName = models.CharField(max_length=50,null= True,blank=True)
    censusdate= models.DateField(null=True,blank=True) 
    #remove = models.CharField(max_length=255, null=True, blank=True)
    TreeAge = models.FloatField(default=0.00,null=True, blank=True)
    blkCnt = models.IntegerField(null=True,blank=True) 
    TeraceCnt = models.IntegerField(null=True,blank=True) 
    LivSum = models.IntegerField(null=True,blank=True) 
    eid = models.IntegerField(default=0.00,null=True,blank=True)
    cidH = models.IntegerField(default=0.00,null=True,blank=True)
    cid = models.IntegerField(default=0,null=True,blank=True)
    aHeight = models.FloatField(default=0.00,null=True,blank=True)
    aGirth = models.FloatField(default=0.00,null=True,blank=True)
    aLeaves = models.FloatField(default=0.00,null=True,blank=True) 
    
    def __str__(self):
        return self.blkCode

## EMS Tree Health report table
## Sireesha 05-July-2021 
#Table - rpt_emsSumTH - areaCode,blkCode,treeCnt,aHeight,aGirth,aLeaves
class rpt_emsSumTH(models.Model):
    #date = models.DateField(null=True,blank=True)
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)
    #treeNo = models.IntegerField(default=0.00,null=True,blank=True)
    #plantDate = models.DateField(null=True,blank=True)
    #plantType = models.CharField(max_length=10,null= True,blank=True)
    #height=models.FloatField(default=0.00,null=True, blank=True)
    treeCnt = models.IntegerField(default=0.00,null=True,blank=True)
    aHeight = models.FloatField(default=0.00,null=True,blank=True)
    aGirth = models.FloatField(default=0.00,null=True,blank=True)
    aLeaves = models.FloatField(default=0.00,null=True,blank=True)
    eid = models.IntegerField(default=0.00,null=True,blank=True)
    cid = models.IntegerField(default=0,null=True,blank=True)
    teraceCnt = models.IntegerField(default=0.00,null=True,blank=True)
    height = models.FloatField(default=0.00,null=True,blank=True)
    girth = models.FloatField(default=0.00,null=True,blank=True)
    leaves = models.FloatField(default=0.00,null=True,blank=True)
    terace = models.CharField(max_length=10,null= True,blank=True)
    
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. areaCode
class rpt_emsSumTHOnly(models.Model):
    #date = models.DateField(null=True,blank=True)
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)
    #treeNo = models.IntegerField(default=0.00,null=True,blank=True)
    #plantDate = models.DateField(null=True,blank=True)
    #plantType = models.CharField(max_length=10,null= True,blank=True)
    #height=models.FloatField(default=0.00,null=True, blank=True)
    treeCnt = models.IntegerField(default=0.00,null=True,blank=True)
    aHeight = models.FloatField(default=0.00,null=True,blank=True)
    aGirth = models.FloatField(default=0.00,null=True,blank=True)
    aLeaves = models.FloatField(default=0.00,null=True,blank=True)
    #cid = models.CharField(max_length=255,null=True,blank=True)
    eid = models.IntegerField(default=0.00,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. areaCode

## EMS Summary report table
## Sireesha 02-July-2021 
class rpt_emsSumTHArOnly(models.Model):
    #date = models.DateField(null=True,blank=True)
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCnt = models.IntegerField(default=0.00,null=True,blank=True)    
    teraceNo = models.IntegerField(default=0.00,null=True,blank=True)
    #plantDate = models.DateField(null=True,blank=True)
    #plantType = models.CharField(max_length=10,null= True,blank=True)
    #height=models.FloatField(default=0.00,null=True, blank=True)
    treeCnt = models.IntegerField(default=0.00,null=True,blank=True)
    aHeight = models.FloatField(default=0.00,null=True,blank=True)
    aGirth = models.FloatField(default=0.00,null=True,blank=True)
    aLeaves = models.FloatField(default=0.00,null=True,blank=True)
    eid = models.IntegerField(default=0.00,null=True,blank=True)
    #cid = models.CharField(max_length=255,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)

    def __str__(self):
        return self. areaCode


## EMS Tree Health report table
## Sireesha 05-July-2021 
#Table - rpt_emsSumTH - areaCode,blkCode,treeCnt,aHeight,aGirth,aLeaves
#class rpt_emsExtSmryLog(models.Model):
    #date = models.DateField(null=True,blank=True)
    #areaCode = models.CharField(max_length=10,null= True,blank=True)
    #blkCode = models.CharField(max_length=10,null= True,blank=True)
    #filename = models.CharField(max_length=255,null=True)
    #extDate = models.DateField(null=True,blank=True)
    #teraceNo = models.CharField(max_length=10,null= True,blank=True)
    #treeNo = models.IntegerField(default=0.00,null=True,blank=True)
    #plantDate = models.DateField(null=True,blank=True)
    #plantType = models.CharField(max_length=10,null= True,blank=True)
    #height=models.FloatField(default=0.00,null=True, blank=True)
    #ErrC1Cnt = models.IntegerField(default=0.00,null=True,blank=True)
    #ErrC1Cnt = models.FloatField(default=0.00,null=True,blank=True)
    #aGirth = models.FloatField(default=0.00,null=True,blank=True)
    #aLeaves = models.FloatField(default=0.00,null=True,blank=True)
    #cid = models.CharField(max_length=255,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)


    #def __str__(self):
        #return self. areaCode

#class RPT_Centerwisesreport(models.Model):
 #   branch =  models.CharField(max_length=255, null=True, blank=True)
 #   routecode = models.CharField(max_length=255, null=True, blank=True)
  #  centercode = models.CharField(max_length=255, null=True, blank=True)
  #  date = models.DateField(null=True,blank=True)
  #  shift = models.CharField(max_length=255,null=True,blank=True)
  #  milk_type = models.CharField(max_length=255, null=True, blank=True)
  #  fat = models.FloatField(default=0.00,null=True, blank=True)
  #  snf = models.FloatField(default=0.00,null=True, blank=True)
  #  routename =  models.CharField(max_length=255, null=True, blank=True)
  #  centername =  models.CharField(max_length=255, null=True, blank=True)
  #  amount  = models.FloatField(default=0.00,null=True, blank=True)
  #  ltrrate  = models.FloatField(default=0.00,null=True, blank=True)

  #  def _str_(self):
  #      return self. centercode
class rpt_excel_bankwise(models.Model):
    #date = models.DateField(null=True,blank=True)
    route_number  = models.CharField(max_length=255,null=True,blank=True)
    supervisor = models.CharField(max_length=255,null=True,blank=True)
    centre_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255,null=True,blank=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    bankname = models.CharField(max_length=255,null=True,blank=True)
    BankBranch = models.CharField(max_length=255,null=True,blank=True)
    ifsc=models.CharField(max_length=255,null=True,blank=True)
    amount  = models.FloatField(default=0.00,null=True,blank=True)
    mobile = models.CharField(max_length=255,null=True,blank=True)
    total = models.FloatField(default=0.00,null=True,blank=True)
    ddate = models.DateField(null=True,blank=True)
    net = models.FloatField(default=0.00,null=True,blank=True)
    #idate =  models.DateField(null=True,blank=True)


    def __str__(self):
        return self. centercode

class extendeduser(models.Model):    
    role = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    #graceperiod = models.CharField(max_length=255, blank=True, null=True)
    referral=models.CharField(max_length=255, blank=True, null=True)    
    mobileno = models.BigIntegerField(blank=True,null=True)
    otp=models.IntegerField(blank=True, unique=True, null=True)
    ver=models.CharField(max_length=25, blank=True, null=True) 
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        #SireeshaMobileno+919676964471 Starts
        #otp=random.randint(100000,999999)
        #account_sid = 'AC96de24b505c2e90d0f1ace3507a0f389'
        #auth_token = '28affb4eba1dccfccd88b0a7100917da'
        #client = Client(account_sid, auth_token)
        #message=client.messages.create(
        #to=self.mobileno,
        #from_="+17205805470",
        #body="Your OTP is "+str(otp),
        #KarthikMobileno+918639911586
        #otp=random.randint(100000,999999)
        #account_sid = 'ACb126d536a892a500164566c41bea712c'
        #auth_token = 'ad46cbb4d2d6a7955817a13f862ebf59'
        #client = Client(account_sid, auth_token)
        #message=client.messages.create(
        #to=self.mobileno,
        #from_="+14234012250",
        #body="Your OTP is "+str(otp),
       # )
        #LalithMobile+917799291899starts
        #account_sid = 'AC789a3cbb5ead7e9f62b1bcb3f0cd2c37'
        #auth_token = '528affa9b67885bb01cf309c31db4386'        
        #from_="+16782937570",             
        #LalithMobileEnds 
        otp=random.randint(100000,999999)
        account_sid = 'AC789a3cbb5ead7e9f62b1bcb3f0cd2c37'
        auth_token = '528affa9b67885bb01cf309c31db4386'
        client = Client(account_sid, auth_token)
        message=client.messages.create(
        to=self.mobileno,
        from_="+15623623940",
        body="Your OTP is "+str(otp),
       )
        self.otp=otp
        ## DivyaMobile
        #otp=random.randint(100000,999999)
        #account_sid = 'AC20bc880dc2dd8b0824c8734b306b098d'
        #auth_token = 'd1b92d0596bdce46f21c7a257ddb2bed'
        #client = Client(account_sid, auth_token)
        #message=client.messages.create(
        #to=self.mobileno,
        #from_="+12016693828",
        #body="Your OTP is "+str(otp),
       #)
        #self.otp=otp
        ## Ends Divya Mobile
        #SireeshanewMobileno+919676964471 Starts
        #otp=random.randint(100000,999999)
       # account_sid = 'AC235d477c55e28891fc505f233fb2ccb8'
        #auth_token = 'a23d1a00ae19a290c1a450f7eb949d61'
       # client = Client(account_sid, auth_token)
        #message=client.messages.create(
        #to=self.mobileno,
        #from_="+17028257703",
       # body="Your OTP is "+str(otp),
       # )
       #self.otp=otp
        return super(extendeduser,self).save(*args, **kwargs)

class Address_Ledger(models.Model):
    ledger_code = models.CharField(max_length=255, blank=True)
    house_number = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    colony = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.IntegerField()

    def __str__(self):
        return self.ledger_code

class Sendsms(models.Model):       
    mobileno = models.BigIntegerField(blank=True,null=True)
    message = models.CharField(max_length=755, blank=True, null=True)
    def __str__(self):
        return self.mobileno
    def save(self, *args, **kwargs):
        #otp=random.randint(100000,999999)
        #account_sid = 'AC96de24b505c2e90d0f1ace3507a0f389'
        #auth_token = '28affb4eba1dccfccd88b0a7100917da'
        #client = Client(account_sid, auth_token)
        #message=client.messages.create(
        #to=self.mobileno,
        #from_="+17205805470",
        #body="Your OTP is "+str(otp),
        #otp=random.randint(100000,999999)
        #account_sid = 'ACb126d536a892a500164566c41bea712c'
        #auth_token = 'ad46cbb4d2d6a7955817a13f862ebf59'
        #client = Client(account_sid, auth_token)
        #print(2.3)
        #message=client.messages.create(
        #to=self.mobileno,
       # from_="+14234012250",
       # body=self.message,

       #)
        #LalithMobile+917799291899starts
        #account_sid = 'AC789a3cbb5ead7e9f62b1bcb3f0cd2c37'
        #auth_token = '528affa9b67885bb01cf309c31db4386'        
        #from_="+16782937570",             
        #LalithMobileEnds 
        #print(message.sid)
        #return self.account_sid
        #SireeshanewMobileno+919676964471 Starts
        account_sid = 'AC235d477c55e28891fc505f233fb2ccb8'
        auth_token = 'a23d1a00ae19a290c1a450f7eb949d61'
        client = Client(account_sid, auth_token)
        message=client.messages.create(
        to=self.mobileno,
        from_="+17028257703",
        body=self.message,

        )
        #print(message.sid)
        return super().save(*args, **kwargs)

class sendanemail(models.Model):  
    to=models.CharField(max_length=255,blank=True)
    content=models.CharField(max_length=255,blank=True)  
    
    def __str__(self):
        return self.gname
class Message(models.Model):       
    mobile = models.BigIntegerField(blank=True,null=True)
    centre_code = models.CharField(max_length=255,null=True)
    centercode = models.CharField(max_length=255,null=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    Email = models.CharField(max_length=225,null=True,blank=True)
    #ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
   #snf = models.FloatField(default=0.00,null=True, blank=True)

class Cloan(models.Model):
    loan_type = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    transaction_type = models.CharField(max_length=255,null=True,blank=True)
    route = models.CharField(max_length=255,null=True,blank=True)
    center = models.CharField(max_length=255,null=True,blank=True)
    loan_no = models.CharField(max_length=255,null=True,blank=True)
    loan_date = models.DateField(null=True,blank=True)
    principal_amt = models.IntegerField(null=True,blank=True)
    interest_rate = models.FloatField(default=0.00)
    flat_deminished = models.CharField(max_length=255,null=True,blank=True)
    loan_duration = models.FloatField(null=True,blank=True)
    interest_amt = models.FloatField(default=0.00,null=True, blank=True)
    noofinstallments = models.IntegerField(null=True,blank=True)
    installment_amt = models.FloatField(default=0.00,null=True, blank=True)
    total = models.FloatField(default=0.00,null=True, blank=True)
    closingdate = models.DateField(null=True,blank=True)
    billperiod = models.FloatField(default=0.00,null=True, blank=True)
   
    def __str__(self):
        return self.loan_no

class Deposit(models.Model):
    date = models.DateField(null=True,blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    issuedto = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    agent_name = models.CharField(max_length=255, null=True, blank=True)
    depositno=models.IntegerField(default=0, null=True, blank=True)
    transporter =  models.CharField(max_length=255, null=True, blank=True)
    modeofdeposit = models.CharField(max_length=255, null=True, blank=True)
    routename = models.CharField(max_length=255, null=True, blank=True)
    checkorddno = models.IntegerField(default=0, null=True, blank=True)
    rtgs = models.CharField(max_length=255, null=True, blank=True)
    amount = models.FloatField(default=0.00)
    remarks =  models.CharField(max_length=255, null=True, blank=True)
    closingdate = models.CharField(max_length=255, null=True, blank=True) 

    def __str__(self): 
        return self.centercode         
        
class Refund(models.Model):
    date = models.DateField(null=True,blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    issuedto = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    agent_name = models.CharField(max_length=255, null=True, blank=True)
    loan_no=models.CharField(max_length=255,null=True,blank=True)
    depositno = models.CharField(max_length=255, null=True, blank=True)
    transporter =  models.CharField(max_length=255, null=True, blank=True)
    modeofreturn = models.CharField(max_length=255, null=True, blank=True)
    routename = models.CharField(max_length=255, null=True, blank=True)
    checkorddno = models.IntegerField(default=0, null=True, blank=True)
    rtgs = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(default=0)
    remarks =  models.CharField(max_length=255, null=True, blank=True)
    issueddate = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.loan_no
class Notice(models.Model):    
    noticecode = models.CharField(unique = True,max_length=25)
    noticename = models.CharField(max_length=256,null=True,blank=True)
    effectedfromdate = models.DateField(null=True,blank=True)
    effectedtodate = models.DateField(null=True,blank=True)
    createdby = models.CharField(max_length=255,null=True,blank=True)
    editedby = models.CharField(max_length=255,null=True,blank=True)
    remarks = models.CharField(max_length=255,null=True,blank=True)
    createdOn = models.DateTimeField(auto_now_add=True, null=False,blank=False)
    editedOn = models.DateTimeField(auto_now_add=True, null=False,blank=False)
    def __str__(self):
        return self.name  
class Additions(models.Model):
    date = models.DateField(null=True,blank=True)
    cartage = models.FloatField(default=0.00,null=True, blank=True)
    cattlefeed = models.FloatField(default=0.00,null=True, blank=True)
    centercode = models.CharField(max_length=255,null=True, blank=True)
    autofine = models.FloatField(default=0.00,null=True, blank=True)
    stores=models.FloatField(default=0.00,null=True, blank=True)
    aarrears = models.FloatField(default=0.00,null=True, blank=True)
    medicine =  models.FloatField(default=0.00,null=True, blank=True)
    aothers = models.FloatField(default=0.00,null=True, blank=True)
    stationary = models.FloatField(default=0.00,null=True, blank=True)
    commission = models.FloatField(default=0.00,null=True, blank=True)
    emtcharges = models.FloatField(default=0.00,null=True, blank=True)
    seed = models.FloatField(default=0.00,null=True, blank=True)
    insurance =  models.FloatField(default=0.00,null=True, blank=True)
    rarrears = models.FloatField(default=0.00,null=True, blank=True)
    rothers = models.FloatField(default=0.00,null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.centercode
        

# Module -Management reports -- DashBoard
# Created by - 2021-04-14 @ Divya
# Modified by - 2020-06-09 @ Divya 

class Dashboard_branch(models.Model):
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    centercode = models.CharField(max_length=255) 
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00,null=True, blank=True)
    Ltrs=models.FloatField(default=0.00,null=True, blank=True)
    afat = models.FloatField(default=0.00,null=True, blank=True)
    asnf = models.FloatField(default=0.00,null=True, blank=True)
    Fat=models.FloatField(default=0.00,null=True, blank=True)
    Snf=models.FloatField(default=0.00,null=True, blank=True)
    RateLTR=models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    gamount  = models.FloatField(default=0.00,null=True, blank=True)
    branch=models.CharField(max_length=255,null=True, blank=True)

    
    def str(self):
        return self. centercode


class Dashboard(models.Model):
    address_detail = models.ForeignKey(Address_Ledger,blank=True, null=True,on_delete=models.CASCADE)
    heads = models.CharField(choices=heads,max_length=255)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='Dashboard',null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    expenses_details = models.CharField(max_length=255)
    receviable = models.FloatField(default=0.0)
    payment = models.FloatField(default=0.0)
    date_year = models.IntegerField(default=0)
    date_month = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.expenses_details
        


class RPT_consolidatedreport(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    routename= models.CharField(max_length=255, null=True, blank=True)
    centername = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00)
    Ltrs=models.FloatField(default=0.00)
    afat = models.FloatField(default=0.00)
    asnf = models.FloatField(default=0.00)
    Fat=models.FloatField(default=0.00)
    Snf=models.FloatField(default=0.00)
    RateLTR=models.FloatField(default=0.00)
    tsrate = models.FloatField(default=0.00)
    pel = models.FloatField(default=0.00)
    gamount  = models.FloatField(default=0.00)
    net  = models.FloatField(default=0.00, null=True, blank=True)
    ltrtsrate= models.FloatField(default=0.00)
    kgtsrate = models.FloatField(default=0.00)
   
    def _str_(self):
        return self. centercode

# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='Dashboard',null=True,blank=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)


class daily_data_excel(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='HDFC',null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    BranchCode=models.CharField(max_length=255)
    date = models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    CenterCode=models.CharField(max_length=255)
    MilkType = models.CharField(max_length=255)
    Good_Sour=models.CharField(max_length=255)
    SampleNo=models.FloatField(default=0.0)
    Cans=models.FloatField(default=0.0)
    Kgs=models.FloatField(default=0.0)
    Fat=models.FloatField(default=0.0)
    SNF=models.FloatField(default=0.0)
    CLR=models.FloatField(default=0.0)
    TSRATE=models.FloatField(default=0.0)
    Rate = models.FloatField(default=0.0)
    Comm = models.FloatField(default=0.0)
    Amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.CenterCode

class centerdata(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
  
    CCode=models.CharField(max_length=255)
    CenterName = models.CharField(max_length=255)
    AgentName=models.CharField(max_length=255)
    RName=models.CharField(max_length=255)
    BC=models.CharField(max_length=255)
    ContactNo=models.CharField(max_length=255,null=True,blank=True)
    

    def __str__(self):
        return self.CCode

class  RPT_Milkbilldate(models.Model):
    datefrom = models.DateField(null=True,blank=True)
    dateto = models.DateField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    

    def _str_(self):
        return self. datefrom


class milkdata(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
  
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00)
    Ltrs=models.FloatField(default=0.00)
    Fat=models.FloatField(default=0.00)
    Snf=models.FloatField(default=0.00)
    RateLTR=models.FloatField(default=0.00)
    Netamount=models.FloatField(default=0.00)
    PiExp=models.FloatField(default=0.00,null=True)
    Total=models.FloatField(default=0.00)
    centercode = models.CharField(max_length=255,null=True,blank=True) 
    accholdername = models.CharField(max_length=255,null=True,blank=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    routename = models.CharField(max_length=255,null=True,blank=True)
    branch = models.CharField(max_length=255,null=True,blank=True)

    def _str_(self):
        return self.Shift

class centerbank(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
  
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    centercode = models.CharField(max_length=255) 
    accholdername = models.CharField(max_length=255,null=True,blank=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    routename = models.CharField(max_length=255,null=True,blank=True)
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00)
    Ltrs=models.FloatField(default=0.00)
    Fat=models.FloatField(default=0.00)
    Snf=models.FloatField(default=0.00)
    RateLTR=models.FloatField(default=0.00)
    Netamount=models.FloatField(default=0.00)
    PiExp=models.FloatField(default=0.00)
    Total=models.FloatField(default=0.00)

    def __str__(self):
        return self.bankno 

class Excelupload(models.Model):
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255,null=True)
    Milktype=models.CharField(max_length=255,null=True)
    kgs=models.FloatField(default=0.00,null=True)
    Ltrs=models.FloatField(default=0.00,null=True)
    Fat=models.FloatField(default=0.00,null=True)
    Snf=models.FloatField(default=0.00,null=True)
    RateLTR=models.FloatField(default=0.00,null=True)
    Netamount=models.FloatField(default=0.00,null=True)
    PiExp=models.FloatField(default=0.00,null=True)
    Total=models.FloatField(default=0.00,null=True)
    center = models.CharField(max_length=255,null=True,blank=True) 
    bank = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    accholdername = models.CharField(max_length=255,null=True,blank=True)
    routename = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self. date

class dailydataExcelupload(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255,null=True)
    CenterCode = models.CharField(max_length=255, null=True, blank=True)
    MilkType= models.CharField(max_length=255, null=True)
    Good_Sour = models.CharField(max_length=255, null=True, blank=True)
    SampleNo = models.FloatField(default=0.00,null=True, blank=True)
    Cans  = models.FloatField(default=0.00,null=True, blank=True)
    Kgs = models.FloatField(default=0.00,null=True)
    Fat = models.FloatField(default=0.00,null=True)
    SNF = models.FloatField(default=0.00,null=True)
    CLR  = models.FloatField(default=0.00,null=True)
    TSRATE = models.FloatField(default=0.00,null=True, blank=True)
    Rate =  models.FloatField(default=0.00,null=True, blank=True)
    comm  = models.FloatField(default=0.00,null=True, blank=True)
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    file_name = models.CharField(max_length=12)
   # active = models.BooleanField(default=True)

    def __str__(self):
        return self.branch


class Proc_Data_EE(models.Model):
    RecNo =  models.FloatField(default=0.00,null=True, blank=True)
    PDate = models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255,null=True)
    MilkType = models.CharField(max_length=255, null=True)
    CenterCode = models.CharField(max_length=255, null=True, blank=True)
    Kgs = models.FloatField(default=0.00,null=True)
    Fat = models.FloatField(default=0.00,null=True)
    CLR  = models.FloatField(default=0.00,null=True)
    SNF = models.FloatField(default=0.00,null=True)
    Cans  = models.FloatField(default=0.00,null=True, blank=True)
    Filename = models.CharField(max_length=255,null=True)
    ExtUser = models.CharField(max_length=255, null=True, blank=True)
    ExtDate = models.DateField(null=True,blank=True)
    ValidData = models.BooleanField(default=True)

    def __str__(self):
        return self.RecNo

##ver 15071012AM Ifscexcelupload line- 676-687
##Created by Mamatha 12-07-2021        

class Ifscexcelupload(models.Model):
    SNO =  models.FloatField(max_length=255, null=True, blank=True)
    BKCODE = models.CharField(max_length=255,null=True,blank=True)
    IFSC  = models.CharField(max_length=255,null=False,blank=True)
    BKNAME = models.CharField(max_length=255, null=True, blank=True)
    CITY = models.CharField(max_length=255, null=True)
    ADDRESS = models.CharField(max_length=255,null=True,blank=True)
    FILE_NAME = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.BKCODE
## End of Table definition Ifscexcelupload

## Start of Table definition 
##ver 15071020AM Centermasterdataexcelupload line- 693-710
##Created by Mamatha 14-07-2021

class Centermasterdataexcelupload(models.Model):
    cCode = models.CharField(max_length=255, null=True, blank=True)
    rCODE = models.CharField(max_length=255, null=True, blank=True)
    branch = models.CharField(max_length=255, null=True, blank=True)
    cName = models.CharField(max_length=255, null=True, blank=True)
    aName = models.CharField(max_length=255, null=True, blank=True)
    vName = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    bankno = models.CharField(max_length=255, null=True, blank=True)
    bkCode = models.IntegerField(null=True, blank=True)
    #extdate = models.DateField(null=True, blank=True)
    #extUser = models.CharField(max_length=255, blank=True)
    file_name = models.CharField(max_length=12)
     
    def __str__(self):
        return self.ANAME

##END
##ver 15071012AM tsratesexcelupload line- 713-730
##Created by Mamatha  13-07-2021
class tsratesexcelupload(models.Model):
    Date_From =  models.DateField(max_length=255, null=True, blank=True)
    Date_To = models.DateField(max_length=255,null=True,blank=True)
    Min_Fat  = models.FloatField(max_length=255,null=True,blank=True)
    Max_Fat = models.FloatField(max_length=255, null=True, blank=True)
    Min_SNF = models.FloatField(max_length=255, null=True)
    Max_SNF = models.FloatField(max_length=255,null=True,blank=True)
    Unit = models.CharField(max_length=255,null=True,blank=True)
    TSRATE = models.FloatField(max_length=255,null=True,blank=True)
    FILE_NAME = models.CharField(max_length=255,null=True)
    # ExtBy= models.CharField(max_length=255,null=True,blank=True)
    # ExtDate= models.DateField(max_length=255,null=True,blank=True)
    # Remarks= models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.Date_From)
## End of Table definition tsratesexcelupload
### EMS Project 670 - 
#AREA - MATAG, DJ, VEG

#HYBRID TYPE - TYPE, HYBRID, HARVEST PERIOD, NO OF NUTS (BY AGE), COPRA CONTENT, VCO CONTENT, WATER CONTENT, TENDER COCONUT PRICE, MATURED COCONUT PRICE, VCO PRICE
#PND TYPE - NAME, TYPE, COST, QTY PER TREE, SPRAYING TIME PER TREE
#FERTILISER - TYPE, NAME, COST, QTY PER TREE(BASED ON AGE), APPLICATION TIME PER TREE
#IRRIGATION - BLOCK, PUMP, DURATION, QTY/TREE, FUEL COST/HOUR
#GRASS CUTTING - TYPE, TIME PER TREE/WORKER, TIME PER ACRE/WORKER, MANPOWER COST
#HARVESTING - TREE HEIGHT, TIME TAKEN PER TREE, NO OF NUTS/WORKER
#WORKERS - NAME, SEX, NATIONALITY, JOB DESIGNATION

# EMS Masters - PlantType 702 - 712
#EMSArea - 683 -
class EMSArea(models.Model):
    areaCode = models.CharField(max_length=10,unique=True)
    areaName = models.CharField(max_length=100,unique=True)
    startDate = models.DateField(null=True,blank=True)
    endDate = models.DateField(null=True,blank=True)
    remove = models.CharField(max_length=5,null=True,blank=True)   
    

    def __str__(self):
        return self.areaCode
#EMSArea - 683 -
#BLOCK - BLOCK NAME, NO OF TERRACES, NO OF TREES, GPS COOD, SIZE
#EMSArea - 683 -
class EMSBlock(models.Model):
    blkCode = models.CharField(max_length=10,unique=True)
    BlkName = models.CharField(max_length=100,unique=True)
    noOfTeraces = models.IntegerField(null=True,blank=True)
    noOfTrees = models.IntegerField(null=True,blank=True)
    gpdCoOd = models.CharField(max_length=10,null=True,blank=True)
    size=models.FloatField(default=0.00,null=True, blank=True)   
    startDate = models.DateField(null=True,blank=True)
    endDate = models.DateField(null=True,blank=True)
    remove = models.CharField(max_length=5,null=True,blank=True)    

    def __str__(self):
        return self.blkCode
#EMSArea - 683 -


### EMS Project Ends here
#areaCode,blkCode,teraceNo
#areaCode,blkCode,teraceNo,treeNo,plantDate,plantType,height,girth,leaveCnt
#tcWeeType,tcWaterlog,tcMud,TCNet,WTRing,Waterpipe,PnDFung,PNDTermite,PNDChType,
#ManureRate,ManureDate,Remarks,extdate,extUser
class ExtractPlantData(models.Model):
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)
    treeNo = models.IntegerField(null=True,blank=True)
    plantDate = models.DateField(null=True,blank=True)
    plantType = models.CharField(max_length=10,null= True,blank=True)
    height=models.FloatField(default=0.00,null=True, blank=True)
    girth=models.FloatField(default=0.00,null=True, blank=True)
    leaveCnt = models.IntegerField(null=True,blank=True)
    tcWeeType = models.CharField(max_length=10,null= True,blank=True)
    tcWaterlog = models.CharField(max_length=10,null= True,blank=True)
    tcMud = models.CharField(max_length=10,null= True,blank=True)
    TCNet = models.CharField(max_length=10,null= True,blank=True)
    WTRing = models.CharField(max_length=10,null= True,blank=True)
    Waterpipe = models.CharField(max_length=10,null= True,blank=True)
    PnDFung = models.CharField(max_length=10,null= True,blank=True)
    PNDTermite = models.CharField(max_length=10,null= True,blank=True)
    PNDChType = models.CharField(max_length=10,null= True,blank=True)
    PNDDate = models.DateField(null=True,blank=True)
    manurFType = models.CharField(max_length=10,null= True,blank=True)
    ManureRate=models.FloatField(default=0.00,null=True, blank=True)
    ManureDate = models.DateField(null=True,blank=True)
    Remarks = models.CharField(max_length=100,null= True,blank=True)
    extdate = models.DateField(null=True,blank=True)
    extUser = models.CharField(max_length=255,blank=True)
    fileName = models.CharField(max_length=50,null= True,blank=True)
    censusdate= models.DateField(null=True,blank=True) 
    remove = models.CharField(max_length=255, null=True, blank=True)
    TreeAge = models.FloatField(default=0.00,null=True, blank=True) 
    
    def __str__(self):
        return self.blkCode


### EMS Project Ends here
#areaCode,blkCode,teraceNo
#areaCode,blkCode,teraceNo,treeNo,plantDate,plantType,height,girth,leaveCnt,Remarks,extdate,fileName,censusdate,TreeAge
#tcWeeType,tcWaterlog,tcMud,TCNet,WTRing,Waterpipe,PnDFung,PNDTermite,PNDChType,
#PNDDate,manurFType,
#ManureRate,ManureDate,Remarks,extdate,extUser,fileName,censusdate,TreeAge
class Rpt_ExtractPlantAgData(models.Model):
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)
    treeNo = models.IntegerField(null=True,blank=True)
    plantDate = models.DateField(null=True,blank=True)
    plantType = models.CharField(max_length=10,null= True,blank=True)
    height= models.FloatField(default=0.00,null=True, blank=True)
    girth=models.FloatField(default=0.00,null=True, blank=True)
    leaveCnt = models.IntegerField(null=True,blank=True)
    #tcWeeType = models.CharField(max_length=10,null= True,blank=True)
    #tcWaterlog = models.CharField(max_length=10,null= True,blank=True)
    #tcMud = models.CharField(max_length=10,null= True,blank=True)
    #TCNet = models.CharField(max_length=10,null= True,blank=True)
    #WTRing = models.CharField(max_length=10,null= True,blank=True)
    #Waterpipe = models.CharField(max_length=10,null= True,blank=True)
    #PnDFung = models.CharField(max_length=10,null= True,blank=True)
    #PNDTermite = models.CharField(max_length=10,null= True,blank=True)
    #PNDChType = models.CharField(max_length=10,null= True,blank=True)
    #PNDDate = models.DateField(null=True,blank=True)
    #manurFType = models.CharField(max_length=10,null= True,blank=True)
    #ManureRate=models.FloatField(default=0.00,null=True, blank=True)
    #ManureDate = models.DateField(null=True,blank=True)
    Remarks = models.CharField(max_length=100,null= True,blank=True)
    extdate = models.DateField(null=True,blank=True)
    #extUser = models.CharField(max_length=255,blank=True)
    fileName = models.CharField(max_length=50,null= True,blank=True)
    censusdate= models.DateField(null=True,blank=True) 
    #remove = models.CharField(max_length=255, null=True, blank=True)
    TreeAge = models.FloatField(default=0.00,null=True, blank=True)
    blkCnt = models.IntegerField(null=True,blank=True) 
    TeraceCnt = models.IntegerField(null=True,blank=True)
    hybridCnt = models.IntegerField(default=0.00,null=True,blank=True)  
    LivSum = models.IntegerField(null=True,blank=True) 
    eid = models.IntegerField(default=0.00,null=True,blank=True)
    cid = models.IntegerField(default=0,null=True,blank=True)
    cidH = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.blkCode

        
        

class EMSRFCEE(models.Model):
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)
    treeCnt = models.IntegerField(null=True,blank=True)
    plantDate = models.DateField(null=True,blank=True)
    plantType = models.CharField(max_length=10,null= True,blank=True)
    YieldStAge = models.IntegerField(default=48,null=True,blank=True)
    YieldEndAge = models.IntegerField(default=48,null=True,blank=True)    
    NutsEst = models.IntegerField(default=48,null=True,blank=True)
    NutFrCost=models.FloatField(default=0.00,null=True, blank=True)
    NutVcoCost=models.FloatField(default=0.00,null=True, blank=True)
    NutMatrCost=models.FloatField(default=0.00,null=True, blank=True)
    YieldIncrPer=models.FloatField(default=0.00,null=True, blank=True)    
    Remarks = models.CharField(max_length=100,null= True,blank=True)
    extdate = models.DateField(null=True,blank=True)
    extUser = models.CharField(max_length=255,blank=True)
    fileName = models.CharField(max_length=50,null= True,blank=True)

    def __str__(self):
        return self.plantDate



## Revenue Simulation 745 - 782

##  areaCode,blkCode,teraceNo,treeNo,plantDate,plantType,
##  NutFrCost,NutVcoCost,NutMatrCost,
##  YieldStAge,YieldEndAge,
##  NutsEst,YieldIncrPer
##  YMth1,YProd1,YAmt1
##  Remarks,extdate,extUser,fileName
class Rpt_EMSRevSim(models.Model):
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)
    treeNo = models.IntegerField(null=True,blank=True)
    plantDate = models.DateField(null=True,blank=True)
    plantType = models.CharField(max_length=10,null= True,blank=True)
    NutFrCost=models.FloatField(default=0.00,null=True, blank=True)
    NutVcoCost=models.FloatField(default=0.00,null=True, blank=True)
    NutMatrCost=models.FloatField(default=0.00,null=True, blank=True)
    YieldStAge = models.IntegerField(default=48,null=True,blank=True)
    YieldEndAge = models.IntegerField(default=48,null=True,blank=True)    
    NutsEst = models.IntegerField(default=48,null=True,blank=True)
    YieldIncrPer=models.FloatField(default=0.00,null=True, blank=True)    
    YMth1 = models.DateField(null=True,blank=True)
    YProd1 = models.FloatField(default=0.00,null=True, blank=True)
    YAmt1 = models.FloatField(default=0.00,null=True, blank=True)        
    Remarks = models.CharField(max_length=100,null= True,blank=True)
    extdate = models.DateField(null=True,blank=True)
    extUser = models.CharField(max_length=255,blank=True)
    fileName = models.CharField(max_length=50,null= True,blank=True)
    YMthNo = models.IntegerField(default=48,null=True,blank=True)
        
    
    def __str__(self):
        return self.blkCode

## Revenue Simulation 745 - 782


## Revenue Simulation Summary 848 - 883

##  areaCode,blkCode,teraceNo,treeNo,plantDate,plantType,
##  NutFrCost,NutVcoCost,NutMatrCost,
##  YieldStAge,YieldEndAge,
##  NutsEst,YieldIncrPer
##  YMth1,YProd1,YAmt1
##  Remarks,extdate,extUser,fileName
class Rpt_EMSRevSum(models.Model):
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)    
    plantDate = models.DateField(null=True,blank=True)
    plantType = models.CharField(max_length=10,null= True,blank=True)
    TreesCnt = models.IntegerField(null=True,blank=True)
    YNuts=models.FloatField(default=0.00,null=True, blank=True)
    YYear = models.IntegerField(default=48,null=True,blank=True)
    YMth = models.CharField(max_length=15,null= True,blank=True)        
    YAmt = models.FloatField(default=0.00,null=True, blank=True)        
    Remarks = models.CharField(max_length=100,null= True,blank=True)
    
    def __str__(self):
        return self.blkCode

## Revenue Simulation Summary 848 - 883

## Revenue Simulation Summary Only 946 - 963

class Rpt_EMSRevSumO(models.Model):
    #areaCode = models.CharField(max_length=10,null= True,blank=True)
    #blkCode = models.CharField(max_length=10,null= True,blank=True)
    #teraceNo = models.CharField(max_length=10,null= True,blank=True)    
    plantDate = models.DateField(null=True,blank=True)
    #plantType = models.CharField(max_length=10,null= True,blank=True)
    TreesCnt = models.IntegerField(null=True,blank=True)
    YNuts=models.FloatField(default=0.00,null=True, blank=True)
    YYear = models.IntegerField(default=48,null=True,blank=True)
    YMth = models.CharField(max_length=15,null= True,blank=True)        
    YAmt = models.FloatField(default=0.00,null=True, blank=True) 
    YPer = models.CharField(max_length=15,null= True,blank=True)            
           
    #Remarks = models.CharField(max_length=100,null= True,blank=True)
    
    def __str__(self):
        return self.plantDate

class EMSPlantTypeT(models.Model):
    PlantType = models.CharField(max_length=10,unique=True)
    Description = models.CharField(max_length=100,unique=True)
    # remove = models.CharField(max_length=5,null=True,blank=True)   
    FreshnutCost = models.FloatField(default=0.00,null=True, blank=True)
    MatrednutCost = models.FloatField(default=0.00,null=True, blank=True)
    EstNuts = models.IntegerField(default=5,null=True,blank=True)
    VCOcost = models.FloatField(default=0.00,null=True, blank=True)
    YieldStartAge = models.IntegerField(default=48,null=True,blank=True)
    YieldEndAge = models.IntegerField(default=180,null=True,blank=True)
    Increment=models.FloatField(default=20,null=True, blank=True)
    Remarks = models.CharField(max_length=255,null=True,blank=True)
    remove = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.PType
                

# EMS Masters - PlantType 702 - 712
#EMSPlantType - PType,Descr,remove
#NutFrCost,nutvcocost,NutMatrCost,YieldStAge,YieldEndAge,YieldIncrPer
class EMSPlantType(models.Model):
    PType = models.CharField(max_length=10,unique=True)
    Descr = models.CharField(max_length=100,unique=True)
    remove = models.CharField(max_length=5,null=True,blank=True)   
    NutFrCost = models.FloatField(default=0.00,null=True, blank=True)
    nutvcocost = models.FloatField(default=0.00,null=True, blank=True)
    NutMatrCost = models.FloatField(default=0.00,null=True, blank=True)
    YieldStAge = models.IntegerField(default=48,null=True,blank=True)
    YieldEndAge = models.IntegerField(default=180,null=True,blank=True)
    EstNuts = models.IntegerField(default=5,null=True,blank=True)
    YieldIncrPer=models.FloatField(default=20,null=True, blank=True)

    def __str__(self):
        return self.PType
# EMS Masters - PlantType 702 - 712
#TYPE, HYBRID, HARVEST PERIOD, NO OF NUTS (BY AGE), COPRA CONTENT, VCO CONTENT, WATER CONTENT, TENDER COCONUT PRICE, MATURED COCONUT PRICE, VCO PRICE

#class EMSHybrid(models.Model):
#    HType = models.CharField(max_length=10,unique=True)
#    HYBRID = models.CharField(max_length=100,unique=True)
#    HarPeriod = models.CharField(max_length=5,null=True,blank=True)

    

 #   def __str__(self):
 #       return self.HType

#areaCode,blkCode,teraceNo
#areaCode,blkCode,teraceNo,treeNo,plantDate,plantType,height,girth,leaveCnt
#tcWeeType,tcWaterlog,tcMud,TCNet,WTRing,Waterpipe,PnDFung,PNDTermite,PNDChType,
#ManureRate,ManureDate,Remarks,extdate,extUser,fileName
class ExtractEMSData(models.Model):
    areaCode = models.CharField(max_length=10,null= True,blank=True)
    blkCode = models.CharField(max_length=10,null= True,blank=True)
    teraceNo = models.CharField(max_length=10,null= True,blank=True)
    treeNo = models.IntegerField(null=True,blank=True)
    plantDate = models.DateField(null=True,blank=True)
    plantType = models.CharField(max_length=10,null= True,blank=True)
    height=models.FloatField(default=0.00,null=True, blank=True)
    girth=models.FloatField(default=0.00,null=True, blank=True)
    leaveCnt = models.IntegerField(null=True,blank=True)
    tcWeeType = models.CharField(max_length=10,null= True,blank=True)
    tcWaterlog = models.CharField(max_length=10,null= True,blank=True)
    tcMud = models.CharField(max_length=10,null= True,blank=True)
    TCNet = models.CharField(max_length=10,null= True,blank=True)
    WTRing = models.CharField(max_length=10,null= True,blank=True)
    Waterpipe = models.CharField(max_length=10,null= True,blank=True)
    PnDFung = models.CharField(max_length=10,null= True,blank=True)
    PNDTermite = models.CharField(max_length=10,null= True,blank=True)
    PNDChType = models.CharField(max_length=10,null= True,blank=True)
    PNDDate = models.DateField(null=True,blank=True)
    manurFType = models.CharField(max_length=10,null= True,blank=True)
    ManureRate=models.FloatField(default=0.00,null=True, blank=True)
    ManureDate = models.DateField(null=True,blank=True)
    Remarks = models.CharField(max_length=100,null= True,blank=True)
    extdate = models.DateField(null=True,blank=True)
    extUser = models.CharField(max_length=255,blank=True)
    fileName = models.CharField(max_length=50,null= True,blank=True)        
    validRec = models.BooleanField(default=True)
    PrDUP  = models.BooleanField(default=False)
    FrDUP  = models.BooleanField(default=False)     
    IVDate = models.BooleanField(default=False)
    IVType = models.BooleanField(default=False)
    IVHeight = models.BooleanField(default=False)
    IVGirth = models.BooleanField(default=False)
    IVLeave = models.BooleanField(default=False)       

    def __str__(self):
        return self.treeNo           
class Harvesting(models.Model):
    HCode = models.CharField(unique = True,max_length=255)
    TreeHeight = models.FloatField(max_length=255,null=True,blank=True)
    Duration = models.FloatField(max_length=255,null=True,blank=True)
    TimePerTree = models.FloatField(max_length=255,null=True,blank=True)
    NoOfNuts = models.FloatField(max_length=255,null=True,blank=True)
    IncrPer = models.FloatField(max_length=255,null=True,blank=True)
    HStAge = models.IntegerField(default=200,null=True,blank=True)
    HEndAge = models.IntegerField(default=200,null=True,blank=True)

    def __str__(self):
        return str(self.Duration)

class EMSFertiliser(models.Model):
    FType = models.CharField(max_length=10,unique=True)
    FName = models.CharField(max_length=100,unique=True)
    remove = models.CharField(max_length=5,null=True,blank=True)
    FCost = models.FloatField(default=0.00,null=True, blank=True)
    QtyPerTree = models.FloatField(default=20,null=True, blank=True)
    FreqPerTree = models.FloatField(default=0.00,null=True, blank=True)
    IncrPer = models.IntegerField(default=20,null=True,blank=True)
    FStAge = models.IntegerField(default=48,null=True,blank=True)
    FEndAge = models.IntegerField(default=5,null=True,blank=True)
    def _str_(self):
        return self.FType

class Irrigation(models.Model):
    Icode = models.CharField(max_length=255,unique=True)
    Block = models.CharField(max_length=255,unique=True)
    Pump = models.CharField(max_length=255,null=True,blank=True)  
    Duration = models.FloatField(max_length=255,null=True,blank=True)
    Qtypertree = models.FloatField(max_length=255,null=True,blank=True)
    Freqofpumping = models.FloatField(max_length=255,null=True,blank=True)
    Fuelcostperhour = models.FloatField(max_length=255,null=True,blank=True)
    Incrper = models.FloatField(max_length=255,null=True,blank=True)
    Istage = models.IntegerField(default=100,null=True,blank=True)
    Iendage = models.IntegerField(default=180,null=True,blank=True)

    def __str__(self):
        return str(self.Duration)


class EMSPND(models.Model):
    PType = models.CharField(max_length=10,unique=True)
    PName = models.CharField(max_length=100,unique=True)
    remove = models.CharField(max_length=5,null=True,blank=True)   
    PCost = models.FloatField(default=0.00,null=True, blank=True)
    QtyPerTree = models.FloatField(default=20,null=True, blank=True)
    FreqOfSpray= models.FloatField(default=0.00,null=True, blank=True)
    IncrPer= models.FloatField(default=20,null=True, blank=True)
    PStAge = models.IntegerField(default=48,null=True,blank=True)
    PEndAge = models.IntegerField(default=180,null=True,blank=True)
      
    def __str__(self):
        return self.PType 
class Person(models.Model):
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255,null=True)
    Milktype=models.CharField(max_length=255,null=True)
    kgs=models.FloatField(default=0.0,null=True)
    Ltrs=models.FloatField(default=0.0,null=True)
    Fat=models.FloatField(default=0.0,null=True)
    Snf=models.FloatField(default=0.0,null=True)
    RateLTR=models.FloatField(default=0.0,null=True)
    Netamount=models.FloatField(default=0.0,null=True)
    PiExp=models.FloatField(default=0.0,null=True)
    Total=models.FloatField(default=0.0,null=True)
    center = models.CharField(max_length=255,null=True,blank=True) 
    bank = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    accholdername = models.CharField(max_length=255,null=True,blank=True)
    routename = models.CharField(max_length=255,null=True,blank=True)

class Route(models.Model):
    Route_number = models.CharField(unique = True,max_length=255)
    Route_name = models.CharField(max_length=255)
    date_from = models.DateField(null=True,blank=True)
    date_to = models.DateField(null=True,blank=True)
    active = models.BooleanField(default=True) 
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.Route_name

class Route1(models.Model):
    Route_number = models.CharField(unique = True,max_length=255)
    Route_name = models.CharField(max_length=255)
    date_from = models.DateField(null=True,blank=True)
    date_to = models.DateField(null=True,blank=True)
    active = models.BooleanField(default=True) 

    def __str__(self):
        return self.Route_name

class Supervisor(models.Model):
    code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    datefrom = models.CharField(max_length=255,null=True,blank=True)
    dateto = models.CharField(max_length=255,null=True,blank=True)
    Route_attached = models.CharField(max_length=255)
    Route_attached1 = models.CharField(max_length=255)
    Route_attached2 = models.CharField(max_length=255)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class Supervisor1(models.Model):
    code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    Route_attached = models.CharField(max_length=255,null=True,blank=True)
    Route_attached1 = models.CharField(max_length=255,null=True,blank=True)
    Route_attached2 = models.CharField(max_length=255,null=True,blank=True)

    def _str_(self):
        return self.name

class Agent(models.Model):
    code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    Route_attached = models.CharField(max_length=255,null=True,blank=True)
    Route_attached1 = models.CharField(max_length=255,null=True,blank=True)
    Route_attached2 = models.CharField(max_length=255,null=True,blank=True)
    remove = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.name

class Agent1(models.Model):
    code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    Route_attached = models.CharField(max_length=255,null=True,blank=True)
    Route_attached1 = models.CharField(max_length=255,null=True,blank=True)
    Route_attached2 = models.CharField(max_length=255,null=True,blank=True)

    def _str_(self):
        return self.name

class Village(models.Model):
    code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    Route_attached = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.name

class Milktype(models.Model):
    code = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.code

class Milktype1(models.Model):
    code = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)
    #remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.code

class Category(models.Model):
    code = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.code
class Category1(models.Model):
    code = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)
    #remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.code

class Formulae(models.Model):
    name = models.CharField(max_length=255,unique=True)
    desc = models.CharField(max_length=255,unique=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name
class Formulae1(models.Model):
    name = models.CharField(max_length=255,unique=True)
    desc = models.CharField(max_length=255,unique=True)
   # remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name
class Role(models.Model):
    rcode = models.CharField(max_length=255,unique=True)
    rname = models.CharField(max_length=255,null=True,blank=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.rcode
class Role1(models.Model):
    rcode = models.CharField(max_length=255,unique=True)
    rname = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.rcode

class Office(models.Model):
    ocode = models.CharField(max_length=255,unique=True)
    oname = models.CharField(max_length=255,unique=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.ocode
class Office1(models.Model):
    ocode = models.CharField(max_length=255,unique=True)
    oname = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.ocode
class Department(models.Model):
    dcode = models.CharField(max_length=255,unique=True)
    dname = models.CharField(max_length=255,unique=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.dcode

class Department1(models.Model):
    dcode = models.CharField(max_length=255,unique=True)
    dname = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.dcode
#class Village(models.Model):
#    name = models.CharField(max_length=255,null=True,blank=True)

#    def __str__(self):
#        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    fullname= models.CharField(max_length=255,null=True,blank=True)
    branch   = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.fullname
class Bank1(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    fullname= models.CharField(max_length=255,null=True,blank=True)
    branch   = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    #remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.fullname
        
class Branch(models.Model):
    code = models.CharField(max_length=255,unique = True)
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    pin = models.IntegerField(default=1,null=True, blank=True)
    contno = models.BigIntegerField(default=1,null=True, blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    remove = models.CharField(max_length=255,null=True,blank=True)
    active =models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class Branch1(models.Model):
    code = models.CharField(max_length=255,null=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    pin = models.IntegerField(default=1,null=True, blank=True)
    contno = models.BigIntegerField(default=1,null=True, blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    active =models.CharField(max_length=255,null=True,blank=True)
    creaated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='lccrreate')
    crreaatedd = models.DateTimeField(default=timezone.now,null=True)
    code1 = models.CharField(max_length=255,null=True)
    name1 = models.CharField(max_length=255,null=True,blank=True)
    address1 = models.CharField(max_length=255,null=True,blank=True)
    pin1 = models.IntegerField(default=1,null=True, blank=True)
    contno1 = models.BigIntegerField(default=1,null=True, blank=True)
    email1 = models.CharField(max_length=255,null=True,blank=True)
    active1 =models.CharField(max_length=255,null=True,blank=True)
    uppt_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='luupdattte')
    updaatedd = models.DateTimeField(default=timezone.now,null=True)
    #remove = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class Branchlog(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    pin = models.IntegerField(default=1,null=True, blank=True)
    contno = models.BigIntegerField(default=1,null=True, blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    active =models.CharField(max_length=255,null=True,blank=True)
    creaated_by = models.CharField(max_length=255,null=True,blank=True)
    crreaatedd = models.DateTimeField(default=timezone.now,null=True)
    code1 = models.CharField(max_length=255,null=True)
    name1 = models.CharField(max_length=255,null=True,blank=True)
    address1 = models.CharField(max_length=255,null=True,blank=True)
    pin1 = models.IntegerField(default=1,null=True, blank=True)
    contno1 = models.BigIntegerField(default=1,null=True, blank=True)
    email1 = models.CharField(max_length=255,null=True,blank=True)
    active1 =models.CharField(max_length=255,null=True,blank=True)
    uppt_by = models.CharField(max_length=255,null=True,blank=True)
    updaatedd = models.DateTimeField(default=timezone.now,null=True)


    def __str__(self):
        return self.name


class DokQC_Entry(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    centercode  = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    sour = models.CharField(max_length=255, null=True, blank=True)
    Quantity = models.FloatField(default=0.00,null=True, blank=True)
    cans = models.IntegerField(default=0,null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)
    samplecode =  models.IntegerField(default=0)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
  
    def _str_(self):
        return self. branch

class DokQC_Create(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    center_name = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    sour = models.CharField(max_length=255, null=True, blank=True)
    Quantity = models.FloatField(default=0.00,null=True, blank=True)
    cans = models.IntegerField(default=0)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)
    samplecode =  models.CharField(max_length=255, null=True, blank=True)
    branch1 =  models.CharField(max_length=255, null=True, blank=True)
    date1 = models.DateField(null=True,blank=True)
    shift1 = models.CharField(max_length=255, null=True, blank=True)
    code1  = models.CharField(max_length=255, null=True, blank=True)
    center_name1 = models.CharField(max_length=255, null=True, blank=True)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    sour1 = models.CharField(max_length=255, null=True, blank=True)
    Quantity1 = models.FloatField(default=0.00,null=True, blank=True)
    cans1 = models.IntegerField(default=0)
    routecode1 = models.CharField(max_length=255, null=True, blank=True)
    remove1 = models.CharField(max_length=255, null=True, blank=True)
    samplecode1 =  models.CharField(max_length=255, null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    creeated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='lccrreatee')
    create = models.DateTimeField(default=timezone.now,null=True)
    updatedt_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='uipdate')
    updatee = models.DateTimeField(default=timezone.now,null=True)
    #upt_byyy = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='uupdattte')
  # created_by1 = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='ccrreate')
   # updatedd1 = models.DateTimeField(default=timezone.now)
   # crreatedd1 = models.DateTimeField(default=timezone.now)   
    

    def _str_(self):
        return self. branch
    def save(self, *args, **kwargs):
        self.snf=(float(self.clr))/4 +(0.21*float(self.fat))+0.36;
        super(DokQC_Create, self).save(*args, **kwargs)






class Logdokqc(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    samplecode =  models.CharField(max_length=255, null=True, blank=True)
    Quantity = models.FloatField(default=0.00,null=True, blank=True)
    cans = models.IntegerField(default=0)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    samplecode1 =  models.CharField(max_length=255, null=True, blank=True)
    Quantity1 = models.FloatField(default=0.00,null=True, blank=True)
    cans1 = models.IntegerField(default=0)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    creeated_by =models.CharField(max_length=255, null=True, blank=True)
    icreate = models.DateTimeField(default=timezone.now,null=True)
    updatedt_by =models.CharField(max_length=255, null=True, blank=True)
    iupdatee = models.DateTimeField(default=timezone.now,null=True)
    remove1 = models.CharField(max_length=255, null=True, blank=True)
    code1  = models.CharField(max_length=255, null=True, blank=True)

    def _str_(self):
        return self. branch
    def save(self, *args, **kwargs):
        self.snf=(float(self.clr))/4 +(0.21*float(self.fat))+0.36;
        super(DokQC_Create, self).save(*args, **kwargs)

#cCode   rCode   branch  cName   aName   vName   ContactNo   BankAcNo    BKCode
#class CentreMaster(models.Model):
#    cCode = models.CharField(unique = True,max_length=15)
#    rCode = models.CharField(max_length=10)
#    branch = models.CharField(max_length=15,null=True,blank=True)
#    cName = models.CharField(max_length=100,null=True,blank=True)
#    aName = models.CharField(max_length=100,null=True,blank=True)
#    vName = models.CharField(max_length=100,null=True,blank=True)
#    mobile = models.CharField(max_length=25,null=True,blank=True)
#    bankno = models.CharField(max_length=50,null=True,blank=True)
#    bkCode = models.IntegerField(null=True,blank=True)

#    def __str__(self):
#        return self.cCode
    
class Center(models.Model):
    centre_code = models.CharField(unique = True,max_length=255)
    name = models.CharField(max_length=255)
    milk_type = models.CharField(max_length=255,null=True,blank=True)
    category = models.CharField(max_length=255,null=True,blank=True)
    Formula = models.CharField(max_length=255,null=True,blank=True)
    #name = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255,null=True,blank=True)
    supervisor = models.CharField(max_length=255,null=True,blank=True)
    #route_number  = models.IntegerField(null=True,blank=True)
    #
    village_name = models.CharField(max_length=255,null=True,blank=True)
    mobile = models.CharField(max_length=255,null=True,blank=True)
    address =  models.TextField(null=True,blank=True)
    actholdername = models.CharField(max_length=255,null=True,blank=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    bankname = models.CharField(max_length=255,null=True,blank=True)
    BankBranch = models.CharField(max_length=255,null=True,blank=True)
    Distance = models.IntegerField(null=True,blank=True)
    Email = models.CharField(max_length=225,null=True,blank=True)
    Branchname=models.CharField(max_length=255,null=True,blank=True)
    #ifsc=models.CharField(max_length=255,null=True,blank=True)
    #kilo = models.IntegerField(null=True,blank=True)
    BM_Comm_unit = models.CharField(max_length=255,null=True,blank=True)
    CM_Comm_unit = models.CharField(max_length=255,null=True,blank=True)
    BM_Cartage_unit = models.CharField(max_length=255,null=True,blank=True)
    CM_Cartage_unit =  models.CharField(max_length=255,null=True,blank=True)
    Fat = models.CharField(max_length=255,null=True,blank=True)
    Document = models.FileField(upload_to='centerimage',null=True,blank=True)
    active = models.BooleanField(default=True) 
    BM_comm_amount = models.IntegerField(default=0.0,null=True,blank=True)
    BM_Cartage_amount = models.IntegerField(default=0.0,null=True,blank=True)
    #cm = models.CharField(max_length=255,null=True,blank=True)
    CM_comm_amount = models.FloatField(default=0.0,null=True,blank=True)
    CM_Cartage_amount = models.IntegerField(default=0.0,null=True,blank=True)
    route_number  = models.CharField(max_length=255,null=True,blank=True)
    #bm_cartage = models.CharField(max_length=255,null=True,blank=True)
    #bm_cartage_amount = models.IntegerField(null=True,blank=True)
    #cm_cartage =  models.CharField(max_length=255,null=True,blank=True)
    #cm_cartage_amount = models.IntegerField(null=True,blank=True)
    #fat = models.CharField(max_length=255,null=True,blank=True)
    #document = models.FileField(upload_to='centerimage',null=True,blank=True)
    #active = models.BooleanField(default=True) 
    ifsc=models.CharField(max_length=255,null=True,blank=True)
    bankname1 = models.CharField(max_length=255,null=True,blank=True)
    BankBranch1 = models.CharField(max_length=255,null=True,blank=True)
    ifsc1=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name
        
class CowMilkCategory(models.Model):
    # centercode =  models.ForeignKey(Center,blank=True, null=True,on_delete=models.CASCADE)
    category = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0, null=True, blank=True)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0, null=True, blank=True)
    min_rate = models.FloatField(default=0.0, null=True, blank=True)
    sour_milkrate = models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return self.category

class CowMilkCenter(models.Model):
    centercode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self):
        return self.centercode


class CowMilkRoute(models.Model):
    Routecode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self):
        return self.Routecode
class BufalloMilkCategory(models.Model):
    # centercode =  models.ForeignKey(Center,blank=True, null=True,on_delete=models.CASCADE)
    category = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0, null=True, blank=True)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0, null=True, blank=True)
    min_rate = models.FloatField(default=0.0, null=True, blank=True)
    sour_milkrate = models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return self.category

class BufalloMilkCenter(models.Model):
    centercode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self):
        return self.centercode

class BufalloMilkRoute(models.Model):
    Routecode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    # min_fat = models.FloatField(default=0.0,null=True,blank=True)
    # max_fat = models.FloatField(default=0.0,null=True,blank=True)
    # min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    # rate = models.FloatField(default=0.0,null=True,blank=True)
    # commission = models.FloatField(default=0.0,null=True,blank=True)
    snf_deduction = models.CharField(max_length=255, null=True, blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self):
        return self.Routecode

class rpt_bufallomilk(models.Model):
    category = models.CharField(max_length=255,null=True,blank=True)
    centercode = models.CharField(max_length=255,null=True,blank=True)
    Routecode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    min_fat = models.FloatField(default=0.0,null=True,blank=True)
    max_fat = models.FloatField(default=0.0,null=True,blank=True)
    min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    tsrate = models.FloatField(default=0.0,null=True,blank=True)
    categoryid = models.IntegerField(default=0,null=True,blank=True)
    routeid = models.IntegerField(default=0,null=True,blank=True)
    centerid = models.IntegerField(default=0,null=True,blank=True)
    brid = models.IntegerField(default=0,null=True,blank=True)
    bcenterid = models.IntegerField(default=0,null=True,blank=True)
    bcategoryid = models.IntegerField(default=0,null=True,blank=True)
    bfrom_date = models.DateField(null=True,blank=True)
    bto_date = models.DateField(null=True,blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    snf_deduction = models.FloatField(default=0.0,null=True,blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)


    def __str__(self):
        return self.Routecode

class rpt_cowmilk(models.Model):
    category = models.CharField(max_length=255,null=True,blank=True)
    centercode = models.CharField(max_length=255,null=True,blank=True)
    Routecode = models.CharField(max_length=255,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    rate_calculation  = models.CharField(max_length=255, null=True, blank=True)
    commission_type = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    min_fat = models.FloatField(default=0.0,null=True,blank=True)
    max_fat = models.FloatField(default=0.0,null=True,blank=True)
    min_SNF = models.FloatField(default=0.0,null=True,blank=True)
    max_SNF = models.FloatField(default=0.0,null=True,blank=True)
    tsrate = models.FloatField(default=0.0,null=True,blank=True)
    categoryid = models.IntegerField(default=0,null=True,blank=True)
    routeid = models.IntegerField(default=0,null=True,blank=True)
    centerid = models.IntegerField(default=0,null=True,blank=True)
    crid = models.IntegerField(default=0,null=True,blank=True)
    ccenterid = models.IntegerField(default=0,null=True,blank=True)
    ccategoryid = models.IntegerField(default=0,null=True,blank=True)
    cfrom_date = models.DateField(null=True,blank=True)
    cto_date = models.DateField(null=True,blank=True)
    fixed_value = models.FloatField(default=0.0,null=True,blank=True)
    snf_value = models.CharField(max_length=255, null=True, blank=True)
    snf_deduction = models.FloatField(default=0.0,null=True,blank=True)
    fat_from = models.FloatField(default=0.0,null=True,blank=True)
    fat_to = models.FloatField(default=0.0,null=True,blank=True)
    penalty_in_RS = models.FloatField(default=0.0,null=True,blank=True)
    deduction_calculation = models.CharField(max_length=255, null=True, blank=True)
    premium = models.FloatField(default=0.0,null=True,blank=True)
    amount = models.FloatField(default=0.0,null=True,blank=True)
    sour_milk = models.CharField(max_length=255, null=True, blank=True)
    curd = models.FloatField(default=0.0,null=True,blank=True)
    min_rate = models.FloatField(default=0.0,null=True,blank=True)
    sour_milkrate = models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self):
        return self.Routecode


class MinMaxFat(models.Model):    
    min_fat = models.FloatField(default=0.00,null=True,blank=True)
    max_fat = models.FloatField(default=0.00,null=True,blank=True)
    min_SNF = models.FloatField(default=0.00,null=True,blank=True)
    max_SNF = models.FloatField(default=0.00,null=True,blank=True)
    tsrate = models.FloatField(default=0.00,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
   # commission = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    routecode =  models.ForeignKey(CowMilkRoute,blank=True, null=True,on_delete=models.CASCADE)
    centercode =  models.ForeignKey(CowMilkCenter,blank=True, null=True,on_delete=models.CASCADE)
    category =  models.ForeignKey(CowMilkCategory,blank=True, null=True,on_delete=models.CASCADE)
    category1 = models.CharField(max_length=255,null=True,blank=True)
    routecode1 = models.CharField(max_length=255,null=True,blank=True)
    centercode1 = models.CharField(max_length=255,null=True,blank=True)
    def __int__(self):
        return self.min_fat

class MinMaxBuff(models.Model):    
    min_fat = models.FloatField(default=0.00,null=True,blank=True)
    max_fat = models.FloatField(default=0.00,null=True,blank=True)
    min_SNF = models.FloatField(default=0.00,null=True,blank=True)
    max_SNF = models.FloatField(default=0.00,null=True,blank=True)
    tsrate = models.FloatField(default=0.00,null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    #commission = models.FloatField(default=0.0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    routecode =  models.ForeignKey(BufalloMilkRoute,blank=True, null=True,on_delete=models.CASCADE)
    centercode =  models.ForeignKey(BufalloMilkCenter,blank=True, null=True,on_delete=models.CASCADE)
    category =  models.ForeignKey(BufalloMilkCategory,blank=True, null=True,on_delete=models.CASCADE)
    category1 = models.CharField(max_length=255,null=True,blank=True)
    routecode1 = models.CharField(max_length=255,null=True,blank=True)
    centercode1 = models.CharField(max_length=255,null=True,blank=True)
    
    def __int__(self):
        return self.min_fat

class Transcation(models.Model):
    date = models.DateField(null=True,blank=True)
    time = models.CharField(max_length=255, null=True, blank=True)
    good_sour = models.CharField(max_length=255, null=True, blank=True)
    centre_code = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    can = models.IntegerField(null=True,blank=True, default=1)
    qty = models.FloatField(default=0.0)
    exp = models.FloatField(default=0.0,null=True,blank=True)
    rate = models.FloatField(default=0.0,null=True,blank=True)
    fat = models.FloatField(default=0.0,null=True,blank=True)
    cartage =  models.FloatField(default=0.0,null=True,blank=True)
    pen = models.FloatField(default=0.0)
    clr = models.FloatField(default=0.0)
    amount = models.FloatField(default=0.0)
    total_amount = models.FloatField(default=0.0)
    snf = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.milk_type 



class Matchlog(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    can = models.IntegerField(default=0,null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    code1  = models.CharField(max_length=255, null=True, blank=True)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    can1 = models.IntegerField(default=0,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    hcreated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='hccrreate')
    hupdatedd = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self. branch  


class Logmatch(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    can = models.IntegerField(default=0,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    code1  = models.CharField(max_length=255, null=True, blank=True)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    can1 = models.IntegerField(default=0,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    hcreated_by = models.CharField(max_length=255, null=True, blank=True)
    hupdatedd = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self. branch  


class QC_Entry(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    samplecode = models.CharField(max_length=255, null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self. branch
    def save(self, *args, **kwargs):
        self.snf=(float(self.clr))/4 +(0.21*float(self.fat))+0.36;
        super(QC_Entry, self).save(*args, **kwargs)
class QC_Bank(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    samplecode = models.CharField(max_length=255, null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self. branch
    def save(self, *args, **kwargs):
        self.snf=(float(self.clr))/4 +(0.21*float(self.fat))+0.36;
        super(QC_Bank, self).save(*args, **kwargs)
class Logfilee(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    uupdaated_by = models.CharField(max_length=255, null=True, blank=True)
    ccreated_by = models.CharField(max_length=255, null=True, blank=True)
    uupdatedd = models.DateTimeField(default=timezone.now)
    ccrreatedd = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self. shift



class QC_Create(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    samplecode = models.CharField(max_length=255, null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)
    branch1 =  models.CharField(max_length=255, null=True, blank=True)
    date1 = models.DateField(null=True,blank=True)
    shift1 = models.CharField(max_length=255, null=True, blank=True)
    samplecode1 = models.CharField(max_length=255, null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    remove1 = models.CharField(max_length=255, null=True, blank=True)
    upt_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='uupdattte')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='ccrreate')
    updatedd = models.DateTimeField(default=timezone.now)
    crreatedd = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self. branch
    def save(self, *args, **kwargs):
        self.snf=(float(self.clr))/4 +(0.21*float(self.fat))+0.36;
        super(QC_Create, self).save(*args, **kwargs)

class DoK_Entry(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    center_name = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    sour = models.CharField(max_length=255, null=True, blank=True)
    Quantity = models.FloatField(default=0.00,null=True, blank=True)
    cans = models.IntegerField(default=0,null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)
    samplecode =  models.IntegerField(default=0)

    def __str__(self):
        return self. branch




class Logfile(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    Quantity = models.FloatField(default=0.00,null=True, blank=True)
    cans = models.IntegerField(default=0)
    crreateddd_by = models.CharField(max_length=255, null=True, blank=True)
    crreatedddd = models.DateTimeField(default=timezone.now)
    Quantity1 = models.FloatField(default=0.00,null=True, blank=True)
    cans1 = models.IntegerField(default=0)
    uppdated_by = models.CharField(max_length=255, null=True, blank=True)
    upppdated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self. code


class DoK_Create(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255, null=True, blank=True)
    code  = models.CharField(max_length=255, null=True, blank=True)
    center_name = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    sour = models.CharField(max_length=255, null=True, blank=True)
    Quantity = models.FloatField(default=0.00,null=True, blank=True)
    cans = models.IntegerField(default=0)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    remove = models.CharField(max_length=255, null=True, blank=True)
    samplecode =  models.CharField(max_length=255, null=True, blank=True)
    branch1 =  models.CharField(max_length=255, null=True, blank=True)
    date1 = models.DateField(null=True,blank=True)
    shift1 = models.CharField(max_length=255, null=True, blank=True)
    code1  = models.CharField(max_length=255, null=True, blank=True)
    center_name1 = models.CharField(max_length=255, null=True, blank=True)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    sour1 = models.CharField(max_length=255, null=True, blank=True)
    Quantity1 = models.FloatField(default=0.00,null=True, blank=True)
    cans1 = models.IntegerField(default=0)
    routecode1 = models.CharField(max_length=255, null=True, blank=True)
    remove1 = models.CharField(max_length=255, null=True, blank=True)
    samplecode1 =  models.CharField(max_length=255, null=True, blank=True)
    createddd_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='updattee')
    up_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='cupdate')
    updated = models.DateTimeField(default=timezone.now)
    create= models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self. branch
    def save(self, *args, **kwargs):
        super(DoK_Create, self).save(*args, **kwargs)    
class Excelextraction(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
  
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    centercode = models.CharField(max_length=255) 
    bankno = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.0)
    Ltrs=models.FloatField(default=0.0)
    Fat=models.FloatField(default=0.0)
    Snf=models.FloatField(default=0.0)
    RateLTR=models.FloatField(default=0.0)
    Netamount=models.FloatField(default=0.0)
    PiExp=models.FloatField(default=0.0)
    Total=models.FloatField(default=0.0)


    def __str__(self):
        return self.bankno 

class Daily_trans(models.Model):
    date = models.DateField(null=True,blank=True)
    time = models.CharField(max_length=255,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    can  = models.FloatField(default=0.0)
    qty = models.FloatField(default=0.0)
    fat = models.FloatField(default=0.0)
    snf = models.FloatField(default=0.0)
    clr  = models.FloatField(default=0.0)

    def __str__(self):
        return self. centercode


class Logfileee(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    crea_by = models.CharField(max_length=255, null=True, blank=True)
    crb = models.DateTimeField(default=timezone.now)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    can1  = models.FloatField(default=0.00,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1  = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    updatedd_by = models.CharField(max_length=255, null=True, blank=True)
    updateddd = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self. centercode


class Loogfileee(models.Model):
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    net  = models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True)
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    crrea_by = models.CharField(max_length=255, null=True, blank=True)
    crb = models.DateTimeField(default=timezone.now)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    can1  = models.FloatField(default=0.00,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1  = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    ltrs1 = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate1  = models.FloatField(default=0.00,null=True, blank=True)
    net1  = models.FloatField(default=0.00,null=True, blank=True)
    pel1 = models.FloatField(default=0.00,null=True, blank=True) 
    amount1  = models.FloatField(default=0.00,null=True, blank=True)
    csv_file=models.CharField(max_length=255,null=True)
    uppdatedd_by = models.CharField(max_length=255, null=True, blank=True)
    updateddd = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self. centercode

class Daily_dataaa(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    sampno =  models.IntegerField(default=0)
    sampno2 =  models.IntegerField(default=0)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate = models.FloatField(default=0.00,null=True, blank=True)
    comm  = models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    net  = models.FloatField(default=0.00,null=True, blank=True)
    branch1 =  models.CharField(max_length=255, null=True, blank=True)
    routecode1 = models.CharField(max_length=255, null=True, blank=True)
    centercode1 = models.CharField(max_length=255, null=True, blank=True)
    date1 = models.DateField(null=True,blank=True)
    shift1 = models.CharField(max_length=255,null=True,blank=True)
    sampno1 =  models.IntegerField(default=0)
    sampno21 =  models.IntegerField(default=0)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    can1  = models.FloatField(default=0.00,null=True, blank=True)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    ltrs1 = models.FloatField(default=0.00,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate1 = models.FloatField(default=0.00,null=True, blank=True)
    comm1  = models.FloatField(default=0.00,null=True, blank=True)
    pel1 = models.FloatField(default=0.00,null=True, blank=True) 
    amount1  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate1  = models.FloatField(default=0.00,null=True, blank=True)
    net1  = models.FloatField(default=0.00,null=True, blank=True)
    csv_file=models.CharField(max_length=255,null=True)
    crrea_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='crear')
    updar_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='updar')
    updar = models.DateTimeField(default=timezone.now)
    crbb = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self. centercode
    def save(self, *args, **kwargs):
        super(Daily_dataaa, self).save(*args, **kwargs)

class Daily_dataa(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    sampno =  models.IntegerField(default=0)
    sampno2 =  models.IntegerField(default=0)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate = models.FloatField(default=0.00,null=True, blank=True)
    comm  = models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    net  = models.FloatField(default=0.00,null=True, blank=True)
    branch1 =  models.CharField(max_length=255, null=True, blank=True)
    routecode1 = models.CharField(max_length=255, null=True, blank=True)
    centercode1 = models.CharField(max_length=255, null=True, blank=True)
    date1 = models.DateField(null=True,blank=True)
    shift1 = models.CharField(max_length=255,null=True,blank=True)
    sampno1 =  models.IntegerField(default=0)
    sampno21 =  models.IntegerField(default=0)
    milk_type1 = models.CharField(max_length=255, null=True, blank=True)
    can1  = models.FloatField(default=0.00,null=True, blank=True)
    qty1 = models.FloatField(default=0.00,null=True, blank=True)
    ltrs1 = models.FloatField(default=0.00,null=True, blank=True)
    fat1 = models.FloatField(default=0.00,null=True, blank=True)
    snf1 = models.FloatField(default=0.00,null=True, blank=True)
    clr1  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate1 = models.FloatField(default=0.00,null=True, blank=True)
    comm1  = models.FloatField(default=0.00,null=True, blank=True)
    pel1 = models.FloatField(default=0.00,null=True, blank=True) 
    amount1  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate1  = models.FloatField(default=0.00,null=True, blank=True)
    net1  = models.FloatField(default=0.00,null=True, blank=True)
    
    crea_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='ugpdattee')
    updatedd_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='klupdatee')
    updateddd = models.DateTimeField(default=timezone.now)
    crb = models.DateTimeField(default=timezone.now)
   
   # active = models.BooleanField(default=True)

    def __str__(self):
        return self. centercode
    def save(self, *args, **kwargs):
        super(Daily_dataa, self).save(*args, **kwargs)


class Daily_data(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    sampno =  models.IntegerField(default=0)
    sampno2 =  models.IntegerField(default=0)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate = models.FloatField(default=0.00,null=True, blank=True)
    comm  = models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    ltrtsrate  = models.FloatField(default=0.00,null=True, blank=True)
    net  = models.FloatField(default=0.00,null=True, blank=True)
    routename =  models.CharField(max_length=255, null=True, blank=True)
    centername =  models.CharField(max_length=255, null=True, blank=True)
    remove = models.CharField(max_length=255,null=True,blank=True)

    #sour = models.CharField(max_length=255, null=True, blank=True)
   # active = models.BooleanField(default=True)

    def __str__(self):
        return self. centercode


        
class RPT_Daywisesreport(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True) 
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    #can  = models.FloatField(default=0.0,null=True, blank=True)
    #scan  = models.FloatField(default=0.0,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True) 
    sqty = models.FloatField(default=0.00,null=True, blank=True)
    sltrs = models.FloatField(default=0.00,null=True, blank=True)
    afat = models.FloatField(default=0.00,null=True, blank=True)
    asnf = models.FloatField(default=0.00,null=True, blank=True)
    kfat = models.FloatField(default=0.00,null=True, blank=True)
    ksnf = models.FloatField(default=0.00,null=True, blank=True) 
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    gamount  = models.FloatField(default=0.00,null=True, blank=True)
    
    

    def __str__(self):
        return self. centercode

class Loanbillsdata(models.Model):
   # sdate = models.DateField(null=True,blank=True)
    idate = models.DateField(null=True,blank=True)
   # loanno =models.FloatField(default=0.0,null=True, blank=True)
    #time = models.CharField(max_length=255,null=True,blank=True)
    #routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    loanid =  models.ForeignKey(Cloan,null = True,blank = True,on_delete=models.CASCADE)
    installment_amt  = models.FloatField(default=0.0,null=True, blank=True)
    installment_principle_amt = models.FloatField(default=0.00,null=True, blank=True)
    interest_amt = models.FloatField(default=0.00,null=True, blank=True)
    total = models.FloatField(default=0.00,null=True, blank=True)
    noofinstallments = models.FloatField(default=0.00,null=True, blank=True)
   # clr  = models.FloatField(default=0.0)

    def _str_(self):
        return self. centercode

class rpt_loan(models.Model):
    date = models.DateField(null=True,blank=True)
    loan_no = models.CharField(max_length=255,null=True,blank=True)
    route = models.CharField(max_length=255,null=True,blank=True)
    center = models.CharField(max_length=255,null=True,blank=True)
    loan_date = models.DateField(null=True,blank=True)
    noofinstallments = models.IntegerField(null=True,blank=True)
    billperiod = models.FloatField(default=0.00,null=True, blank=True)
    flat_deminished = models.CharField(max_length=255,null=True,blank=True)
    interest_rate = models.FloatField(default=0.00)
    installment_principle_amt = models.IntegerField(null=True,blank=True)
    interest_amt = models.FloatField(default=0.00,null=True, blank=True)
    total = models.FloatField(default=0.00,null=True, blank=True)
    outstandingamount= models.FloatField(default=0.00,null=True, blank=True)
    closingdate=models.DateField(null=True,blank=True)
    installment_amt=models.IntegerField(null=True,blank=True)
    status=models.CharField(max_length=255,null=True,blank=True)

    def _str_(self):
        return self.loan_no


class rpt_dailydata(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255, null=True, blank=True)
    centercode = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    shift = models.CharField(max_length=255,null=True,blank=True)
    sampno =  models.IntegerField(default=0,null=True,blank=True)
    sampno2 =  models.IntegerField(default=0,null=True,blank=True)
    milk_type = models.CharField(max_length=255, null=True, blank=True)
    can  = models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    ltrs = models.FloatField(default=0.00,null=True, blank=True)
    fat = models.FloatField(default=0.00,null=True, blank=True)
    snf = models.FloatField(default=0.00,null=True, blank=True)
    clr  = models.FloatField(default=0.00,null=True, blank=True)
    tsrate = models.FloatField(default=0.00,null=True, blank=True)
    comm  = models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    ltrtsrate  = models.FloatField(default=0.00,null=True, blank=True)
    net  = models.FloatField(default=0.00,null=True, blank=True)
    routename =  models.CharField(max_length=255, null=True, blank=True)
    centername =  models.CharField(max_length=255, null=True, blank=True)
   # active = models.BooleanField(default=True)

    def _str_(self):
        return self.centercode

class RPT_consolidated(models.Model):
    branch =  models.CharField(max_length=255, null=True, blank=True)
    date=models.DateField(null=True,blank=True)
    Shift = models.CharField(max_length=255)
    centercode = models.CharField(max_length=255) 
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00,null=True, blank=True)
    Ltrs=models.FloatField(default=0.00,null=True, blank=True)
    afat = models.FloatField(default=0.00,null=True, blank=True)
    asnf = models.FloatField(default=0.00,null=True, blank=True)
    Fat=models.FloatField(default=0.00,null=True, blank=True)
    Snf=models.FloatField(default=0.00,null=True, blank=True)
    RateLTR=models.FloatField(default=0.00,null=True, blank=True)
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    gamount  = models.FloatField(default=0.00,null=True, blank=True)

    
    def _str_(self):
        return self. centercode


class RPT_Daywiseabstract(models.Model):
    date=models.DateField(null=True,blank=True)
    routecode = models.CharField(max_length=255,null= True,blank=True)
    centercode = models.CharField(max_length=255)
    Shift = models.CharField(max_length=255,null=True, blank=True) 
    Milktype=models.CharField(max_length=255)
    kgs=models.FloatField(default=0.00,null=True, blank=True)
    Ltrs=models.FloatField(default=0.00,null=True, blank=True)
    fatkgs = models.FloatField(default=0.00,null=True, blank=True)
    snfkgs = models.FloatField(default=0.00,null=True, blank=True)
    Fat=models.FloatField(default=0.00,null=True, blank=True)
    Snf=models.FloatField(default=0.00,null=True, blank=True)
    tsrate=models.FloatField(default=0.00,null=True, blank=True)
    amount = models.FloatField(default=0.00,null=True, blank=True) 
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    comm = models.FloatField(default=0.00,null=True, blank=True) 
    #cartage = models.FloatField(default=0.00,null=True, blank=True) 
   # incentive = models.FloatField(default=0.00,null=True, blank=True) 
    net = models.FloatField(default=0.00,null=True, blank=True) 
    rate = models.FloatField(default=0.00,null=True, blank=True) 
    gamount  = models.FloatField(default=0.00,null=True, blank=True)

    
    def _str_(self):
        return self. centercode

class RPT_Routewisebillabstract(models.Model):
    date=models.DateField(null=True,blank=True)
    routecode = models.CharField(max_length=255,null= True,blank=True)
    centercode = models.CharField(max_length=255,null= True,blank=True)  
    qty = models.FloatField(default=0.00,null=True, blank=True)
    Ltrs=models.FloatField(default=0.00,null=True, blank=True)
    aarrears = models.FloatField(default=0.00,null=True, blank=True)
    total = models.FloatField(default=0.00,null=True, blank=True)
    fatkgs = models.FloatField(default=0.00,null=True, blank=True)
    afat = models.FloatField(default=0.00)
    snfkgs = models.FloatField(default=0.00,null=True, blank=True)
    asnf = models.FloatField(default=0.00)
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    Snf1=models.FloatField(default=0.00,null=True, blank=True)
    comm = models.FloatField(default=0.00,null=True, blank=True) 
    exsamt = models.FloatField(default=0.00,null=True, blank=True)
    cartage = models.FloatField(default=0.00)
    aothers = models.FloatField(default=0.00)
    gamount  = models.FloatField(default=0.00,null=True, blank=True)
    loan_no = models.CharField(max_length=255,null=True,blank=True)
    stores=models.FloatField(default=0.00)
    rothers = models.FloatField(default=0.00)
    net = models.FloatField(default=0.00,null=True, blank=True) 
    def _str_(self):
        return self. routecode

class  RPT_Milkbillreport(models.Model):
   
    centercode = models.CharField(max_length=255, null=True, blank=True)
    

    def __str__(self):
        return self. centercode


class  RPT_Milkbillvoucher(models.Model):
   # branch =  models.CharField(max_length=255, null=True, blank=True)
    routecode = models.CharField(max_length=255,null= True,blank=True)
    routename = models.CharField(max_length=255,null= True,blank=True)
    centre_code = models.CharField(max_length=255,null= True,blank=True)
    branch = models.CharField(max_length=255,null=True, blank=True)
    centername = models.CharField(max_length=255,null=True, blank=True)
    centercode = models.CharField(max_length=255,null= True,blank=True)
    Shift = models.CharField(max_length=255,null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    milk_type=models.CharField(max_length=255,null=True, blank=True)
    kgs=models.FloatField(default=0.00,null=True, blank=True)
    ltrs=models.FloatField(default=0.00,null=True, blank=True)
    amount  = models.FloatField(default=0.00,null=True, blank=True)
    ltrrate  = models.FloatField(default=0.00,null=True, blank=True)
    fat=models.FloatField(default=0.00,null=True, blank=True)
    snf=models.FloatField(default=0.00,null=True, blank=True)
    qty = models.FloatField(default=0.00,null=True, blank=True)
    #center = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.BigIntegerField(blank=True,  null=True)
    bankno = models.CharField(max_length=255,null=True,blank=True)
    bank_branch = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    bankname = models.CharField(max_length=255,null=True,blank=True)
    comm = models.FloatField(default=0.00,null=True, blank=True) 
    pel = models.FloatField(default=0.00,null=True, blank=True) 
    net=models.FloatField(default=0.00,null=True, blank=True)
    agent_name=models.CharField(max_length=255)
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    pin = models.IntegerField(null=True,blank=True)
    sdate = models.DateField(null=True,blank=True)
    idate = models.DateField(null=True,blank=True)
    installment_amt  = models.FloatField(default=0.00)
    interest_amt = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00,null=True, blank=True)
    payable = models.FloatField(default=0.00,null=True, blank=True)
    adate = models.DateField(null=True,blank=True)
    cartage = models.FloatField(default=0.00)
    cattlefeed = models.FloatField(default=0.00)
    acentercode = models.FloatField(default=0.00)
    autofine = models.FloatField(default=0.00)
    stores=models.FloatField(default=0.00)
    aarrears = models.FloatField(default=0.00) 
    medicine =  models.FloatField(default=0.00)
    aothers = models.FloatField(default=0.00)
    stationary = models.FloatField(default=0.00)
    commission = models.FloatField(default=0.00)
    emtcharges = models.FloatField(default=0.00)
    seed = models.FloatField(default=0.00)
    insurance =  models.FloatField(default=0.00)
    rarrears = models.FloatField(default=0.00)
    rothers = models.FloatField(default=0.00)


   # active = models.BooleanField(default=True)

    def str(self):
        return self. centercode