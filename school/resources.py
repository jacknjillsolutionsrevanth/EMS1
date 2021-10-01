from import_export import resources
from school.models import Excelupload,dailydataExcelupload,tsratesexcelupload,Centermasterdataexcelupload,Ifscexcelupload,ExtractEMSData,ExtractPlantData,Proc_Data_EE


class ExceluploadReource(resources.ModelResource):
    class meta: 
        model = Excelupload

class dailydataExceluploadReource(resources.ModelResource):
    class meta: 
        model = dailydataExcelupload
class ExtractPlantDataReource(resources.ModelResource):
    class meta: 
        model = ExtractPlantData
 #ExtractEMSData
class ExtractEMSDataReource(resources.ModelResource):
    class meta: 
    	model = ExtractEMSData

class Proc_Data_EEReource(resources.ModelResource):
    class meta:
        model = Proc_Data_EE


class IfscexceluploadReource(resources.ModelResource):
    class meta: 
        model = Ifscexcelupload

class CentermasterdataexceluploadReource(resources.ModelResource):
    class meta: 
        model = Centermasterdataexcelupload

class tsratesexceluploadReource(resources.ModelResource):
    class meta: 
        model = tsratesexcelupload