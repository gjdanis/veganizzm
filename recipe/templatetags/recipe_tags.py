from django import template
import fractions

register = template.Library()

@register.filter
def formatted_measure(measure):
    if '-' in measure or '/' in measure or not measure:
        return measure
    
    try:
        return int(measure)
    except:
        pass

    frac = fractions.Fraction(measure)
    num, den = frac.numerator, frac.denominator
    return '%d %d/%d' % (num // den, num % den, den)

