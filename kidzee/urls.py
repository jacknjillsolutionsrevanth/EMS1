"""kidzee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from school.views import GeneratePdfemspnd_report,Generatepdf_emsareareport,GeneratePdfemsplanttype_report,GeneratePdfemspnd_report,Generatepdf_irrigationreport,GeneratePdfemsfertiliser_report,Generatepdf_harvestingreport,Generatepdf_noticereport,GeneratePdfversionreport,GeneratePdfLoanschdeulereport,GeneratePdfCensus_report,GeneratePdfEmsSmryAreaBlock,GeneratePdfEmsSmryTreeHealth,GeneratePdf,GeneratePdfRefundreport,GeneratePdfMilkCollection,GeneratePdfAdditions_report,GeneratePdfConsolidated,GeneratePdfDepositreport,GeneratePdfUserdata_report,GeneratePdfRoutewisebillabstract,GeneratePdfDaywiseabstract,GeneratePdfLoanreport, GeneratePdfMilkbillcenter,GeneratePdfDaily,GeneratePdfMilk,GeneratePdfBank_wise,GeneratePdfBank_report,GeneratePdfCenter_report,GeneratePdfBmCenter_report,GeneratePdfBmCategory_report,GeneratePdfBmRoute_report,GeneratePdfCmCenter_report,GeneratePdfCmCategory_report,GeneratePdfCmRoute_report,GeneratePdfBranch_report,GeneratePdfRoute_report,GeneratePdfSupervisor_report,GeneratePdfAgent_report,GeneratePdfDepartment_report,GeneratePdfRole_report,GeneratePdfOffice_report,GeneratePdfVillage_report,GeneratePdfMilktype_report,GeneratePdfCategory_report,GeneratePdfFormula_report,GeneratePdfCenter_reportbank

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^emsareareport/pdf/(?P<slug>.*)/$',Generatepdf_emsareareport.as_view()),
    url(r'^noticereport/pdf/(?P<slug>.*)/$', Generatepdf_noticereport.as_view()),
    url(r'^emsplanttypereport/pdf/(?P<slug>.*)/$', GeneratePdfemsplanttype_report.as_view()),
    url(r'^harvestingreport/pdf/(?P<slug>.*)/$',Generatepdf_harvestingreport.as_view()),
    url(r'^irrigationreport/pdf/(?P<slug>.*)/$',Generatepdf_irrigationreport.as_view()),
    url(r'^emsfertiliserreport/pdf/(?P<slug>.*)/$', GeneratePdfemsfertiliser_report.as_view()),
    url(r'^emspndreport/pdf/(?P<slug>.*)/$', GeneratePdfemspnd_report.as_view()),
    url(r'^emspndreport/pdf/(?P<slug>.*)/$', GeneratePdfemspnd_report.as_view()),
    url(r'^versionreport/pdf/(?P<slug>.*)/$', GeneratePdfversionreport.as_view()),
    url(r'^pdf/(?P<slug>.*)/$', GeneratePdf.as_view()),
    url(r'^daily/pdf1/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/$', GeneratePdfDaily.as_view()),
  #  url(r'^down/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$', GeneratePdf_date.as_view()),
    url(r'^milk/pdf1/$', GeneratePdfMilk.as_view()),
   # url(r'^day/pdf1/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/$', GeneratePdfDay.as_view()),
    url(r'^bankreport/pdf1/(?P<slug>.*)/$',GeneratePdfBank_report.as_view()),
    url(r'^bankwise/pdf1/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/$', GeneratePdfBank_wise.as_view()),
    url(r'^centerreport/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$', GeneratePdfCenter_report.as_view()),
    url(r'^centerreportbank/pdf/(?P<slug>.*)/(?P<slug1>.*)/$', GeneratePdfCenter_reportbank.as_view()),
    url(r'^bmcenterreport/pdf/(?P<slug3>.*)/(?P<slug4>.*)/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$', GeneratePdfBmCenter_report.as_view()),
    url(r'^bmcategoryreport/pdf/(?P<slug3>.*)/(?P<slug4>.*)/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$', GeneratePdfBmCategory_report.as_view()),
    url(r'^bmroutereport/pdf/(?P<slug3>.*)/(?P<slug4>.*)/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$', GeneratePdfBmRoute_report.as_view()),
    url(r'^cmcenterreport/pdf/(?P<slug3>.*)/(?P<slug4>.*)/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$', GeneratePdfCmCenter_report.as_view()),
    url(r'^cmcategoryreport/pdf/(?P<slug3>.*)/(?P<slug4>.*)/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$', GeneratePdfCmCategory_report.as_view()),
    url(r'^cmroutereport/pdf/(?P<slug3>.*)/(?P<slug4>.*)/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$', GeneratePdfCmRoute_report.as_view()),
    url(r'^branchreport/pdf/(?P<slug>.*)/$', GeneratePdfBranch_report.as_view()),
    url(r'^routereport/pdf/(?P<slug>.*)/$', GeneratePdfRoute_report.as_view()),
    url(r'^censusreport/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/(?P<slug4>.*)/$', GeneratePdfCensus_report.as_view()),
    url(r'^EmsSmryAreaBlock/pdf1/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/(?P<slug4>.*)/(?P<slug5>.*)/$', GeneratePdfEmsSmryAreaBlock.as_view()),
    url(r'^EMSSmryTreeHealth/pdf1/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/(?P<slug4>.*)/(?P<slug5>.*)/$', GeneratePdfEmsSmryTreeHealth.as_view()),
    url(r'^supervisorreport/pdf/(?P<slug>.*)/$', GeneratePdfSupervisor_report.as_view()),
    #url(r'^centerwise/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$', GeneratePdfCenterwisereport.as_view()),
    url(r'^agentreport/pdf/(?P<slug>.*)/$', GeneratePdfAgent_report.as_view()),
    url(r'^departmentreport/pdf/(?P<slug>.*)/$', GeneratePdfDepartment_report.as_view()),
    url(r'^rolereport/pdf/(?P<slug>.*)/$', GeneratePdfRole_report.as_view()),
    url(r'^officereport/pdf/(?P<slug>.*)/$', GeneratePdfOffice_report.as_view()),
    url(r'^villagereport/pdf/(?P<slug>.*)/$', GeneratePdfVillage_report.as_view()),
    url(r'^milktypereport/pdf/(?P<slug>.*)/$', GeneratePdfMilktype_report.as_view()),
    url(r'^categoryreport/pdf/(?P<slug>.*)/$', GeneratePdfCategory_report.as_view()),
    url(r'^formulareport/pdf/(?P<slug>.*)/$', GeneratePdfFormula_report.as_view()),
    url(r'^milkbillcenter/pdf1/(?P<slug3>.*)/$', GeneratePdfMilkbillcenter.as_view()),
    url(r'^additionsreport/pdf/(?P<slug>.*)/$', GeneratePdfAdditions_report.as_view()),
    url(r'^loanreport/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/$', GeneratePdfLoanreport.as_view()),
    url(r'^loanschdeulereport/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/$', GeneratePdfLoanschdeulereport.as_view()),

    #url(r'^consolidated/pdf1/(?P<slug>.)/(?P<slug1>.)/(?P<slug2>.)/(?P<slug3>.)/(?P<slug4>.*)$',GeneratePdfConsolidated.as_view()),
    url(r'^consolidated/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/(?P<slug4>.*)/$',GeneratePdfConsolidated.as_view()),
    url(r'^milkcollection/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/(?P<slug4>.*)/$',GeneratePdfMilkCollection.as_view()),
    url(r'^daywiseabstract/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/(?P<slug4>.*)/$',GeneratePdfDaywiseabstract.as_view()),
    url(r'^routewisebillabstract/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/$',GeneratePdfRoutewisebillabstract.as_view()),
    url(r'^depositreport/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/$',GeneratePdfDepositreport.as_view()),
    url(r'^refundreport/pdf/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/(?P<slug3>.*)/$', GeneratePdfRefundreport.as_view()),
    url(r'^userreport/pdf/(?P<slug>.*)/(?P<slug1>.*)/$',GeneratePdfUserdata_report.as_view()),

    url(r'^', include("school.urls",namespace="school")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)