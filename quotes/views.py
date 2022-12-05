from django.http import HttpResponse
from django.shortcuts import redirect, render
from quotes.models import Quote
from quotes.forms import QuoteForm
from django.contrib import messages

# Create your views here.

def add_quote(request):
    context = {
        'quoteform':QuoteForm()
    }
    return render(request,'addquote.html',context)

def all_quotes(request):
    quotes_list = Quote.objects.all()
    context = {
        'quotes_list': quotes_list,
    }
    return render(request,'quotes.html',context)

def add_quote_action(request):
    quoteform = QuoteForm(request.POST, request.FILES)
    if quoteform.is_valid():
        quoteform.save()
        messages.success(request,'Added Successfully')
        return redirect('quotes:all_quotes')
    context = {
            'quoteform': quoteform,
        }
    return render(request, 'addquote.html', context)

def quote_details(request, pk):
    single_quote = Quote.objects.get(id=pk)
    context = {
        'single_quote': single_quote
    }
    return render(request,'quote_details.html',context)

def edit_quote(request,pk):
    quote = Quote.objects.get(id=pk)
    if request.POST:
        quote.title = request.POST.get('title')
        quote.quoted_by = request.POST.get('quoted_by')
        quote.description = request.POST.get('description')
        quote.type = request.POST.get('type')
        quote.image = request.POST.get('image')
        try:
            quote.save()
            messages.success(request, 'Saved Successfully')
            return redirect('quotes:quote_details', quote.id)
        except:
            messages.error(request, 'Could not save, wrong values provided')
            quote = Quote.objects.get(id=pk)
    context = {
            'quote':quote,
            'edit_quote':True,
            'types': ['General', 'Love', 'Economy', 'Education']
        }
    return render(request,'quote_details.html',context)    

def delete(request,pk):
    quote_to_delete = Quote.objects.get(id=pk)
    quote_to_delete.delete()
    messages.success(request,'quote deleted')
    return redirect('quotes:all_quotes')

def search_quote(request):
    if 'word' in request.GET:
        found_quote = request.GET['word']
        quotes_list = Quote.objects.filter(title__icontains = found_quote)
        context = {
                'quotes_list':quotes_list
            }
    return render(request,'quotes.html',context)