from django.shortcuts import render, get_object_or_404, redirect
from Document_Details.models import Document, Tracking, Officers, Status, Employee, Department
from django.utils import timezone  # Import timezone utility from Django
from django.contrib import messages

# Global variables to hold officer_id and comment (typically avoid global variables)
officer_id = ''
comment = ''
dict = {}

def Document_View(request, DocumentID, OID):
    # Retrieve document ID from the URL
    Id = DocumentID
    
    # Fetch the document details, tracking details, officers, status, employees, and departments from the database
    Details = Document.objects.filter(document_id=Id).values()
    Track = Tracking.objects.filter(document=Id).values().all()
    Officer = Officers.objects.values().all()
    Sta = Status.objects.values().all()
    Emp = Employee.objects.values().all()
    Dept = Department.objects.values()
    
    # Prepare context dictionary to pass data to the template
    context = {
        'Details': Details,
        'Track': Track,
        'Officer': Officer,
        'Status': Sta,
        'Employee': Emp,
        'Dept': Dept
    }
    
    # Store the last tracking entry in the dictionary `dict`
    for i in Track:
        dict = i
    
    # Check if the request method is POST (indicating form submission)
    if request.method == "POST":
        # Retrieve form data from the POST request
        document_id = request.POST.get("document_id")
        name = dict.get("full_name")  # Get the full name from the tracking details
        forwarded_to = request.POST.get("officer")  # Get the ID of the officer to whom the document is forwarded
        forwarded_by = OID  # The ID of the officer who is forwarding the document
        forwarded_date = timezone.now().strftime("%Y-%m-%d")  # Get the current date
        forwarded_time = timezone.now()  # Get the current time
        status = dict.get("status_id")  # Get the status ID from the tracking details
        comment = request.POST.get("comment")  # Get the comment from the form

        # Get instances of the required models
        document_instance = get_object_or_404(Document, document_id=document_id)
        officer_to_instance = get_object_or_404(Officers, officers_id=forwarded_to)
        officer_by_instance = get_object_or_404(Officers, officers_id=forwarded_by)
        status_instance = get_object_or_404(Status, status_id=status)

        # Debugging print statement to display captured values
        print(document_id, name, forwarded_to, forwarded_by, forwarded_date, forwarded_time, status, comment)
        
        # Create a new Tracking entry with the provided information
        Tr = Tracking(
            document=document_instance,
            full_name=name,
            forwarded_to=officer_to_instance,
            forwarded_by=officer_by_instance,
            forwarded_date=forwarded_date,
            forwarded_time=forwarded_time,
            status=status_instance,
            comment=comment
        )
        
        # Save the new Tracking entry to the database
        Tr.save()
    
    # Render the template 'Document_Details.html' with the context data
    return render(request, 'Document_Details.html', context)
