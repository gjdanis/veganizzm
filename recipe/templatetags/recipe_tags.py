from django import template
import fractions

register = template.Library()

@register.filter
def format_measure(measure):
    # Used to display decimals as mixed numbers.
    if '-' in measure or '/' in measure or 'x' in measure or not measure:
        return measure

    frac = fractions.Fraction(measure)
    num, den = frac.numerator, frac.denominator
    if den == 1:
        return num
    return '%d %d/%d' % (num // den, num % den, den)

