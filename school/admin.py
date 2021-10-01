from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from school.models import ExtractEMSData,Ifscexcelupload,tsratesexcelupload,Centermasterdataexcelupload,daily_data_excel,centerdata,Dashboard_branch,Logdokqc,sendanemail,Logmatch,Logfile,Branch1,Sendsms,Branchlog,Daily_dataaa,Logfileee,Loogfileee,Logfilee,Daily_dataa,centerbank,Groupsdata,Usersdata,Additions,RPT_Milkbillvoucher,rpt_cowmilk,rpt_bufallomilk,Loanbillsdata,Person,Excelupload,ExtractPlantData,dailydataExcelupload,Proc_Data_EE,milkdata,extendeduser,RPT_consolidatedreport,Role,Rfr,RPT_Daywisesreport,Referral,Department,Office,Signup,DoK_Create,QC_Create,QC_Bank,rpt_bankwise,BufalloMilkCenter,BufalloMilkCategory,BufalloMilkRoute,Dashboard,Cloan,Deposit,Refund,Address_Ledger,Route,Daily_data,Daily_trans,QC_Entry,DoK_Entry,Milktype,Branch,Supervisor,Category,Formulae,Village,Bank,Agent,Center,CowMilkCategory,CowMilkCenter, CowMilkRoute,Transcation,MinMaxFat,MinMaxBuff
# Register your models here.

@admin.register(Excelupload)
class ExceluploadAdmin(ImportExportModelAdmin):
    list_display = ('date','Shift', 'Milktype','kgs','Ltrs', 'Fat', 'Snf', 'RateLTR', 'Netamount', 'PiExp', 'Total','center','bank','ifsc', 'accholdername',  'routename') 

@admin.register(dailydataExcelupload)
class dailydataExceluploadAdmin(ImportExportModelAdmin):
    list_display = ('branch','date','Shift','CenterCode','MilkType','Good_Sour','SampleNo','Cans','Kgs','Fat','SNF','CLR','TSRATE','Rate','comm','amount')

#@admin.register(ExtractPlantData)
#class ExtractPlantDataAdmin(ImportExportModelAdmin):
#    list_display = ('blkCode','treeNo','plantDate','plantType','height','girth','leaveCnt','tcWeeType','tcWaterlog','tcMud','TCNet','WTRing','Waterpipe','PnDFung','PNDTermite','PNDChType','PNDDate','manurFType','ManureRate','ManureDate','Remarks')
@admin.register(ExtractPlantData)
class ExtractPlantDataAdmin(ImportExportModelAdmin):
    list_display = ('areaCode','blkCode','teraceNo','treeNo','plantDate','plantType','height','girth','leaveCnt','tcWeeType','tcWaterlog','tcMud','TCNet','WTRing','Waterpipe','PnDFung','PNDTermite','PNDChType','PNDDate','manurFType','ManureRate','ManureDate','Remarks','extdate','extUser','fileName')

@admin.register(ExtractEMSData)
class ExtractEMSDataAdmin(ImportExportModelAdmin):
    list_display = ('areaCode','blkCode','teraceNo','treeNo','plantDate','plantType','height','girth','leaveCnt','tcWeeType','tcWaterlog','tcMud','TCNet','WTRing','Waterpipe','PnDFung','PNDTermite','PNDChType','PNDDate','manurFType','ManureRate','ManureDate','Remarks','extdate','extUser','fileName')


@admin.register(Proc_Data_EE)
class Proc_Data_EEAdmin(ImportExportModelAdmin):
    list_display = ('RecNo','PDate','Shift','MilkType','CenterCode','Kgs','Fat','CLR','SNF','Cans') 

@admin.register(Ifscexcelupload)
class IfscexceluploadAdmin(ImportExportModelAdmin):
    list_display = ('SNO','BKCODE','IFSC','BKNAME','CITY','ADDRESS')

@admin.register(Centermasterdataexcelupload)
class CentermasterdataexceluploadAdmin(ImportExportModelAdmin):
    list_display = ('cCode','rCODE','branch','cName','aName','vName','mobile','bankno','bkCode')

@admin.register(tsratesexcelupload)
class tsratesexceluploadAdmin(ImportExportModelAdmin):
    list_display = ('Date_From','Date_To','Min_Fat','Max_Fat','Min_SNF','Max_SNF','Unit','TSRATE') 


admin.site.register(Dashboard)

admin.site.register( Dashboard_branch)

admin.site.register(Logdokqc)
admin.site.register(rpt_cowmilk)
admin.site.register(Sendsms)
admin.site.register(RPT_Milkbillvoucher)
admin.site.register(rpt_bufallomilk)
admin.site.register(Additions)
admin.site.register(Address_Ledger)
admin.site.register(daily_data_excel)
admin.site.register(Loanbillsdata)
admin.site.register(centerdata)
admin.site.register(milkdata)
admin.site.register(centerbank)
admin.site.register(Route)
admin.site.register(Deposit)
admin.site.register(RPT_consolidatedreport)
admin.site.register(Refund)
admin.site.register(Cloan)
admin.site.register(Signup)
admin.site.register(Supervisor)
admin.site.register(Category)
admin.site.register(Usersdata)
admin.site.register(Groupsdata)
admin.site.register(Formulae)
admin.site.register(Village)
admin.site.register(Bank)
admin.site.register(rpt_bankwise)
admin.site.register(Milktype)
admin.site.register(Branch)
admin.site.register(Agent)
admin.site.register(Center)
admin.site.register(Role)
admin.site.register(Referral)
admin.site.register(Rfr)
admin.site.register(Department)
admin.site.register(Office)
admin.site.register(DoK_Create)
admin.site.register(QC_Create)
admin.site.register(RPT_Daywisesreport)
admin.site.register(CowMilkCategory)
admin.site.register(CowMilkCenter)
admin.site.register(CowMilkRoute)
admin.site.register(BufalloMilkCenter)
admin.site.register(BufalloMilkRoute)
admin.site.register(BufalloMilkCategory)
admin.site.register(MinMaxBuff)
admin.site.register(Transcation)
admin.site.register(MinMaxFat)
admin.site.register(QC_Entry)
admin.site.register(DoK_Entry)
admin.site.register(QC_Bank)
admin.site.register(Logfile)
admin.site.register(Logfilee)
admin.site.register(Logfileee)
admin.site.register(Loogfileee)
admin.site.register(Logmatch)
admin.site.register(Branchlog)
admin.site.register(Daily_dataa)
admin.site.register(Daily_dataaa)
admin.site.register(Daily_trans)
admin.site.register(Branch1)
admin.site.register(Daily_data)
admin.site.register(extendeduser)
# admin.site.register(Dailyproc)