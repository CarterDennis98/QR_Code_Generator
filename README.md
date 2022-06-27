# QR Code Generator
Converts lat long coordinates from a spreadsheet into QR codes that link to Google Maps

Your spreadsheet should be named ```data.xlsx``` and stored in the root of the repository.
Make sure your spreadsheet is in the following format (case sensitive):

| name | lat | long |
|------|-----|------|
|test  |35.48|-97.50|

This will generate a single QR code with the name ```test.png``` that will take you to the specified coordinates on Google Maps.