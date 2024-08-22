from django.shortcuts import render
from Super_Dashboard.models import Tracking, Document, Officers
from django.contrib.auth.decorators import login_required  # Import to restrict view access to logged-in users

# View function to handle the Super Dashboard
def Super_View(request, OID):
    # Count the number of documents in each status category ("S1", "S2", "S3", "S4")
    S1 = Tracking.objects.filter(status="S1").count()
    S2 = Tracking.objects.filter(status="S2").count()
    S3 = Tracking.objects.filter(status="S3").count()
    S4 = Tracking.objects.filter(status="S4").count()
    
    # Fetch all documents associated with specific departments (DT1, DT2, DT3)
    D1 = Document.objects.filter(depart_id="DT1")
    D2 = Document.objects.filter(depart_id="DT2")
    D3 = Document.objects.filter(depart_id="DT3")
    
    # Fetch all officers from the Officers table (though not used in the current context)
    Olist = Officers.objects.all()
    
    # Store the officer ID passed in the URL
    ID = OID
    
    # Prepare the context dictionary to pass data to the template
    context = {
        'Data': [S1, S2, S3, S4],  # Status counts
        'D1': D1,  # Documents from department DT1
        'D2': D2,  # Documents from department DT2
        'D3': D3,  # Documents from department DT3
        'OID': ID  # Officer ID
    }
    
    # Render the 'Super_Dashboard.html' template with the provided context data
    return render(request, 'Super_Dashboard.html', context)
