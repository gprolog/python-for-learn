import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=40&page_start=0'
class MovieCollection(object):
    header='编号 评分 电影名称 电影id'.split

    def __init__(self,rows):
        self._rows=rows

        def __len__(self):
            return len(self._rows)
        
    def movies(self):
        for idx,row in emumerrate(self._rows):
            rating=row.get('rating')

            #douban score
            score='{:.1f}'.format(rating.get('value')) if rating else '暂无'
            infos=row['info'].split('/')
            if re.match('\d', infos[-1]):
                time = infos[-1:]
                infos = '/'.join(infos[:-1])
            else:
                time = infos[-2:]
                infos = '/'.join(infos[:-2])
            m = [
                idx + 1,
                '\n'.join([
                    colored.green(row['title']),
                    colored.red(time[0][:10]),
                ]),
                infos,
                score
            ]
            yield m
            
    def _get_movie_summary(self,num):
        url=self._rows[num - 1].get('url')
        r=requests.get(url)
        soup=BeautifulSoup(r.text,'html.parser')
        s=re.sub(r'\s+', '', soup.find(property="v:summary").text)
        print(textwrap.fill(colored.green(s), 40, initial_indent=''))


    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for m in self.movies:
            pt.add_row(m)
        print(pt)

def query():
    r=requests.get(url)
    try:
        rows = r.json()['subject_collection_items']
    except (IndexError, TypeError):
        rows = []

    return MoviesCollection(rows)

if __name__=='__main__':
    query()
