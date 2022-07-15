from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
import subprocess
from django.conf import settings
from django.templatetags.static import static
import xml.etree.ElementTree as ET

# Create your views here.
def home(request):
    if request.method == 'POST':
        file_input = request.FILES.get('file_input')
        if file_input=="" or file_input==None or file_input.name.split(".")[-1]!="tex":
            return render(request,'converter/index.html', {'error': 'Please choose a Latex (.tex) file'})
        else:
            print(file_input.name)
            try:
                imgname = "input.tex"
                file_path = os.path.join(settings.MEDIA_ROOT, "XML_Pipeline/static/"+imgname)
                if os.path.exists(file_path):
                    os.remove(file_path)
                fs = FileSystemStorage()
                file_name = fs.save("XML_Pipeline/static/input.tex", file_input)
                output_file_name = "output.xml"
                output_file_path = 'XML_Pipeline/static/'+output_file_name
                command = 'pandoc ' + file_name + ' -f latex -t jats -s -o ' + output_file_path
                #os.system(command)
                subprocess.call(command.split(" "))
                print("Conversion Done...")
                tree = ET.parse('XML_Pipeline/static/output.xml')
                return render(request,'converter/index.html',{'file_name':output_file_name,'file_path':output_file_path})
            except Exception as e:
                return render(request,'converter/index.html', {'error': "Unable to convert the file"})
    return render(request,'converter/index.html')