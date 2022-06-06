import qrcode
import pandas

df = pandas.read_excel('links/QR_Link_Test.xlsx')

for ind in df.index:
    img = qrcode.make(df['GE link'][ind])
    type(img)
    img.save('codes/' + df['name'][ind] + '.png')