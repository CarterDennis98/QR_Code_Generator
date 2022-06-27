import pandas
import qrcode

df = pandas.read_excel('data.xlsx')

for ind in df.index:
    img = qrcode.make('https://www.google.com/maps/place/' + str(df['lat'][ind]) + ',' + str(df['long'][ind]))
    img.save('codes/' + df['name'][ind] + '.png')
