from django.shortcuts import render
from Depart_Dashboard.models import Document, Department

# This view handles the display of the department dashboard
def Depart_View(request, Depart, OID):
    # Fetch all documents associated with the given department ID
    D = Document.objects.filter(depart_id=Depart)
    
    # Fetch the department details using the provided department ID
    Dep = Department.objects.filter(depart_id=Depart)
    
    # Count the number of documents in each status category ("S1", "S2", "S3", "S4") for the given department
    S1 = Document.objects.filter(status="S1", depart_id=Depart).count()
    S2 = Document.objects.filter(status="S2", depart_id=Depart).count()
    S3 = Document.objects.filter(status="S3", depart_id=Depart).count()
    S4 = Document.objects.filter(status="S4", depart_id=Depart).count()
    
    # Store the officer ID provided in the URL
    ID = OID
    
    # Prepare context dictionary to pass data to the template
    context = {
        'Depart': Dep,       # Department details
        'D': D,              # All documents associated with the department
        'Data': [S1, S2, S3, S4],  # Count of documents in each status category
        'OID': ID            # Officer ID
    }
    
    # Render the 'Depart_Dashboard.html' template with the provided context data
    return render(request, 'Depart_Dashboard.html', context)
