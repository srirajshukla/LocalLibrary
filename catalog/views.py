from django.shortcuts import render

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre, Language

def index(request):
    """View function for home page of site"""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()

    #Available books (status = 'a')
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()

    # the 'all()' is implied by defualut
    num_authors = Author.objects.count()

    # finding a particular instance of word in genre and books
    num_instance_of_word = Genre.objects.filter(name__contains='fantasy').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instance,
        'num_instances_available': num_instance_available,
        'num_authors': num_authors,
        'num_instance_of_word': num_instance_of_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic


class BookListView(generic.ListView):
    model = Book
    paginate_by = 1
    # context_object_name = 'my_book_list'    # your own name for the list as template variable
    # queryset = Book.objects.filter(title__icontains='harry')[:3]
    # template_name = 'books/my_arbitrary_template_name_list.html' # my own template name / location


class BookDetailView(generic.DetailView):
    model = Book