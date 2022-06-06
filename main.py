import qrcode, pandas

df = pandas.read_excel('CRP_Spreadsheet.xlsx')

for ind in df.index:
    img = qrcode.make('google.com/maps/place/' + str(df['Latitude'][ind]) + ',' + str(df['Longitude'][ind]))
    img.save('codes/' + df['Farm and Tract No.'][ind] + '.png')