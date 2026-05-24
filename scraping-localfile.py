from bs4 import BeautifulSoup

with open('courses.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'lxml')

course_names = [
    row.find('td').get_text(strip=True)
    for row in soup.select('table tbody tr')
    if row.find('td')
]

print('Course names:')
for name in course_names:
    print('-', name)