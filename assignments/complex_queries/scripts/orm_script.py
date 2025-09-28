from complex_queries.models import Restaurant, Sale
from django.db.models import Q, F
from datetime import timedelta
from django.utils import timezone


def run():
    italian_q = Q(restaurant_type=Restaurant.TypeChoices.ITALIAN)
    mexican_q = Q(restaurant_type=Restaurant.TypeChoices.MEXICAN)
    italian_mexican_q = italian_q | mexican_q

    thirty_days_ago = timezone.now() - timedelta(days=30)
    recently_opened_q = Q(date_opened__gte=thirty_days_ago)
    not_recently_opened_q = ~recently_opened_q

    name_contains_grill_q = Q(name__icontains='grill')
    name_ends_cafe_q = Q(name__endswith='Cafe')

    name_has_digit_q = Q(name__regex=r'\d+')
    restaurant_name_has_digit_q = Q(restaurant__name__regex=r'\d+')

    profitable_q = Q(income__gt=F('expenditure'))
    sale_profitable_or_digit_restaurant_q = profitable_q | restaurant_name_has_digit_q

    # a. Italian OR Mexican
    a = Restaurant.objects.filter(italian_mexican_q)
    print("a (Italian or Mexican):", a)
    print("SQL:", str(a.query))

    # b. NOT opened in last 30 days
    b = Restaurant.objects.filter(not_recently_opened_q)
    print("b (Not recently opened):", b)
    print("SQL:", str(b.query))

    # c. Italian/Mexican OR opened in last 30 days
    c = Restaurant.objects.filter(italian_mexican_q | recently_opened_q)
    print("c (Italian/Mexican or recent):", c)
    print("SQL:", str(c.query))

    # Pattern: contains 'grill'
    d = Restaurant.objects.filter(name_contains_grill_q)
    print("d (Name contains grill):", d)
    print("SQL:", str(d.query))

    # Pattern: ends with 'Cafe'
    e = Restaurant.objects.filter(name_ends_cafe_q)
    print("e (Name ends with Cafe):", e)
    print("SQL:", str(e.query))

    # Regex: name contains digits
    f = Restaurant.objects.filter(name_has_digit_q)
    print("f (Name has digits):", f)
    print("SQL:", str(f.query))

    # Sales: profitable OR restaurant name has digit, with select_related
    g = Sale.objects.select_related('restaurant').filter(
        sale_profitable_or_digit_restaurant_q)
    print("g (Profitable sales or digit in restaurant name):", g)
    print("SQL:", str(g.query))
