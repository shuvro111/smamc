from datetime import date
import bangla


def get_dates():
    english_months = ["জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে",
                      "জুন", "জুলাই", "আগস্ট", "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর", "ডিসেম্বর"]

    today = date.today()

    current_english_day = bangla.convert_english_digit_to_bangla_digit(
        today.day)

    current_english_month = english_months[today.month+1]

    current_english_year = bangla.convert_english_digit_to_bangla_digit(
        today.year)

    current_bangla_day = bangla.get_date().get('date')
    current_bangla_month = bangla.get_date().get('month')
    current_bangla_year = bangla.get_date().get('year')

    english_date = '{} {}, {}'.format(
        current_english_day, current_english_month, current_english_year)
    bangla_date = '{} {}, {}'.format(
        current_bangla_day, current_bangla_month, current_bangla_year)

    return {'english_date': english_date, 'bangla_date': bangla_date}
