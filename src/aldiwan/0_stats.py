import ujson
import pandas as pd
from bidi.algorithm import get_display
from tabulate import tabulate

if __name__ == '__main__':
    with open('../../data/aldiwan.json', encoding='utf-8') as file:
        data = ujson.load(file)

        poems = []
        for pt in data:
            for pm in pt['poems']:
                poems.append({
                    'poet_uid': pt['uid'],
                    'poem_uid': pm['uid'],
                    'era': pt['era'],
                    'genre': pm['genre'],
                    'meter': pm['meter'],
                    'lines': int(len(pm['halves']) / 2),
                })
        df = pd.DataFrame(poems)

        eras = [
            'جاهلي',
            'مخضرم',
            'أموي',
            'عباسي',
            'أندلسي',
            'أيوبي',
            'مملوكي',
            'عثماني',
        ]
        genres = [
            'هجاء',
            'رثاء',
            'مدح',
            'عتاب',
            'غزل',
            'حزينة',
            'رومنسية',
            'دينية',
            'ذم',
            'شوق',
            'فراق',
            'وطنية',
            'سياسية',
            'اعتذار',
        ]

        print()
        print('##### METER BY ERA')
        for era in eras:
            print()
            meter_era = pd.crosstab(df['meter'], df['era'])\
                .sort_values(by=era, ascending=False)[[era]].transpose()
            print(tabulate(meter_era, tablefmt="pipe", headers="keys"))

        print()
        print('##### METER BY GENRE')
        for genre in genres:
            print()
            meter_genre = pd.crosstab(df['meter'], df['genre'])\
                .sort_values(by=genre, ascending=False)[[genre]].transpose()
            print(tabulate(meter_genre, tablefmt="pipe", headers="keys"))
