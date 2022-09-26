from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
import subprocess
from django.conf import settings
from django.templatetags.static import static
import xml.etree.ElementTree as ET
from zipfile import ZipFile, ZIP_DEFLATED
from os.path import basename

# Create your views here.
def home(request):
    if request.method == 'POST':
        error = ""
        data = {}
        input_files =  request.FILES.getlist('tex_file_input')
        if len(input_files)!=2:
            error += "Obtained files doesn't match the expected count (2)"
            print(error)
        else:
            tex_file_input = ""
            bib_file_input = ""
            for f in input_files:
                if f.name.split(".")[-1]=="tex":
                    tex_file_input = f
                elif f.name.split(".")[-1]=="bib":
                    bib_file_input = f
                else:
                    error += "Received files with invalid extensions."
            if error=="":
                try:
                    texfilename = "input.tex"
                    tex_file_path = os.path.join(settings.MEDIA_ROOT, "XML_Pipeline/static/"+texfilename)
                    if os.path.exists(tex_file_path):
                        os.remove(tex_file_path)
                    fs = FileSystemStorage()
                    tex_file_name = fs.save("XML_Pipeline/static/input.tex", tex_file_input)
                    xmL_output_file_path = 'XML_Pipeline/static/journal.xml'
                    command = 'pandoc ' + tex_file_name + ' -f latex -t jats -s -o ' + xmL_output_file_path
                    #os.system(command)
                    subprocess.call(command.split(" "))
                    print("Conversion Done...")
                    # tree = ET.parse('XML_Pipeline/static/journal.xml')
                    # root = tree.getroot()
                    # make_conflict_of_interest(root)
                    # tree.write('XML_Pipeline/static/journal.xml')
                    with ZipFile(file='XML_Pipeline/static/output.zip',mode='w',compression=ZIP_DEFLATED) as zip:
                        zip.write(xmL_output_file_path,basename(xmL_output_file_path))
                        zip.write("XML_Pipeline/static/input.tex",basename("XML_Pipeline/static/input.tex"))
                    data['file_name'] = "output.zip"
                    data['file_path'] = "XML_Pipeline/static/output.zip"
                except Exception as e:
                    print(e)
                    error += "Unable to convert the file"
        if error=="":
            print(data)
            return render(request,'converter/index.html',data)
        return render(request,'converter/index.html', {'error': error})
    return render(request,'converter/index.html')