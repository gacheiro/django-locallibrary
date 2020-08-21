from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)

from catalog.models import Book, BookInstance, Author, Genre
from catalog.forms import RenewBookForm


def home(request):
    """View function for the home page of the site."""

    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authos = Author.objects.count()

    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authos,
        'num_visits': num_visits,
    }

    return render(request, 'catalog/home.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'catalog.can_manage_authors'
    model = Author
    fields = '__all__'


class AuthorUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'catalog.can_manage_authors'
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class AuthorDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'catalog.can_manage_authors'
    model = Author
    success_url = reverse_lazy('authors')


class LoanedBooksView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan"""
    permission_required = 'catalog.can_mark_returned'
    model = BookInstance
    template_name = 'catalog/bookinstance_list_loaned.html'
    paginate_by = 2

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o') \
                                   .order_by('due_back')


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 2

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user) \
                           .filter(status__exact='o').order_by('due_back')


class RenewBookView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'catalog.can_mark_returned'
    model = BookInstance
    form_class = RenewBookForm
    template_name_suffix = '_renewal_form'
    success_url = reverse_lazy('all-borrowed')
