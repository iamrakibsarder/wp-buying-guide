from requests import post
import os
from dotenv import load_dotenv

from functions import openai_ans, heading2, pixabay_image, media_from_url, wp_posting, wp_headers, paragraph
with open('keywords.txt', 'r+') as file:
    keyword_lists = file.readlines()

for keyword in keyword_lists:
    main_keyword = keyword.strip()
    title = f'Best {main_keyword} buying guide 2022'
    description = paragraph(openai_ans(f'Write short intro about {main_keyword}'))
    first_heading = heading2(f'Importance of {main_keyword} in our daily life?')
    first_img = media_from_url(pixabay_image(main_keyword)[0], main_keyword)
    first_para = paragraph(openai_ans(f'Why {main_keyword} is important in our daily life? Write a paragraph'))
    second_heading = heading2(f'How to choose the best {main_keyword}?')
    second_img = media_from_url(pixabay_image(main_keyword)[1], main_keyword)
    second_para = paragraph(openai_ans(f'How to choose best {main_keyword}? Write effective reasons for choosing it in paragraph.'))
    third_heading = heading2(f'Features you should know while buying {main_keyword}')
    third_img = media_from_url(pixabay_image(main_keyword)[2], main_keyword)
    third_para = paragraph(openai_ans(f'What features should be consider while buying {main_keyword} and why? Explain it as a paragraph.'))
    last_heading = heading2('Conclusion')
    last_para = paragraph(openai_ans(f'write a conclusion about why should I buy a {main_keyword}.'))
    slug = title.strip().lower().replace(' ', '-')
    content = description + first_heading + first_img + first_para + second_heading + second_img + second_para + third_heading + third_img + third_para + last_heading + last_para
    load_dotenv()
    site_pass = os.getenv('WEBSITE_PASS')
    headers = wp_headers('admin', site_pass)

    wp_posting(headers, title, slug, content, description)



# title - Laptop buying guide
# description = Write short intro about laptop
# Why laptop is important in our daily life?
# How to choose best Laptop
# What features should be consider while buying Laptop and why? Explain it.
# conclusion about why should I buy a Laptop.
