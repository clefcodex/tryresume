from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse


# from django.shortcuts import render
# from .models import ContactForm
# from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	if request.method == "POST":
		contact = Contact()
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		contact.name = name
		contact.email = email
		contact.phone = phone
		contact.message = message
		contact.save()
		return HttpResponse("<h2>Thanks for Contacting Us</h2>")
	return render(request, 'index.html')







# def index(request):
# 	if request.method == 'POST':
# 		contact = ContactForm()
# 		name = request.POST.get('name')
# 		email = request.POST.get('email')
# 		phone = request.POST.get('phone')
# 		message = request.POST.get('message')
# 		contact.save()
# 		print(name)
# 		return HttpResponseRedirect('/')
# 	return render(request, 'index.html', context)





























# # def index(request):
# # 	form = BookForm(request.POST)
# # 		if form.is_valid():
# # 			title = form.cleaned_data['title']
# # 			author = form.cleaned_data['author']
# # 			isbn = form.cleaned_data['isbn']
# # 			new_book = Book(title=title, author=author, isbn=isbn)
# # 			new_book.save()
# # 			return HttpResponseRedirect('/')
# # 	if request.method == 'POST':
# # 		contact = ContactForm(request.POST)
# # 		if contact.is_valid():
# # 			name = contact.cleaned_data['name']
# # 			email = contact.cleaned_data['email']
# # 			phone = contact.cleaned_data['phone']
# # 			message = contact.cleaned_data['message']
# # 			new_contact = ContactForm
# # 			contact.save()
# # 		print(contact)
# # 		return HttpResponse("<h1>Thanks for Contacting Us</h1>")
# # 	return render(request, 'index.html')